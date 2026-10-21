#!/usr/bin/env python3
"""Regenerate `src/busabase/generated/` (and `_operations.py`) from `openapi.json` with openapi-python-client.

    uv run python scripts/generate.py            # regenerate in place
    uv run python scripts/generate.py --check    # exit 1 if the committed code is stale

`--export` first refreshes `openapi.json` from the Busabase API contract. That
step needs the Busabase monorepo (it runs the TypeScript exporter in
`packages/busabase-core`); in a standalone checkout of this SDK, `openapi.json`
is the source of truth and is used as-is. `--check --export` also fails when
`openapi.json` itself no longer matches the contract.

The generator and ruff are pinned in pyproject.toml's dev group, and the post
hooks run ruff with `--isolated`, so the same inputs give byte-identical output
on any machine — which is what makes `--check` meaningful.
"""

from __future__ import annotations

import argparse
import ast
import filecmp
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "openapi.json"
CONFIG = ROOT / "openapi-python-client.yaml"
TARGET = ROOT / "src" / "busabase" / "generated"
INDEX = ROOT / "src" / "busabase" / "_operations.py"
EXPORTER_DIR = ROOT.parent / "busabase-core"
EXPORTER = EXPORTER_DIR / "scripts" / "export-sdk-openapi.mts"


def export_spec(check: bool) -> None:
    if not EXPORTER.exists():
        sys.exit(f"--export needs the Busabase monorepo ({EXPORTER} not found)")
    args = ["npx", "--no-install", "tsx", str(EXPORTER), "--out", str(SPEC)]
    if check:
        args.append("--check")
    if subprocess.run(args, check=False, cwd=EXPORTER_DIR, stdin=subprocess.DEVNULL).returncode != 0:
        sys.exit(1)


def generate(out: Path) -> None:
    """Run openapi-python-client into `out` (which must not exist yet)."""
    bin_dir = Path(sys.executable).parent
    generator = bin_dir / "openapi-python-client"
    if not generator.exists():
        sys.exit(f"openapi-python-client is not installed next to {sys.executable}; run `uv sync` first")
    # The post hooks call `ruff`; make sure it is the pinned one from this environment.
    env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ.get('PATH', '')}"}
    result = subprocess.run(
        [
            str(generator),
            "generate",
            "--path",
            str(SPEC),
            "--config",
            str(CONFIG),
            "--meta",
            "none",
            "--output-path",
            str(out),
            "--fail-on-warning",
        ],
        check=False,
        env=env,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stdout + result.stderr)
        sys.exit("openapi-python-client failed (warnings count as failures)")


def snake(name: str) -> str:
    """`listPage` -> `list_page`, `Change Requests` -> `change_requests`."""
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return re.sub(r"[^a-zA-Z0-9]+", "_", name).strip("_").lower()


def kwargs_arguments(path: Path) -> list[str]:
    """The keyword argument names of a generated module's `_get_kwargs`."""
    for node in ast.parse(path.read_text(encoding="utf-8")).body:
        if isinstance(node, ast.FunctionDef) and node.name == "_get_kwargs":
            return [arg.arg for arg in node.args.args + node.args.kwonlyargs]
    sys.exit(f"{path} has no _get_kwargs — the generator's output layout changed; see busabase/_query.py")


def python_argument(wire: str, arguments: list[str], where: str) -> str:
    """The generator's Python name for query parameter `wire` (`valueFilters` -> `value_filters`)."""
    key = wire.replace("_", "").lower()
    matches = [arg for arg in arguments if arg.rstrip("_").replace("_", "").lower() == key]
    if len(matches) != 1:
        sys.exit(f"{where}: cannot map query parameter {wire!r} onto _get_kwargs({', '.join(arguments)})")
    return matches[0]


def operation_index(generated: Path) -> str:
    """Source of `busabase/_operations.py`.

    `OPERATIONS`: dotted Python path -> generated module. `Busabase` resolves
    `bb.change_requests.list` through this. The dotted path keeps the
    operationId's own group boundaries (`changeRequests.list` ->
    `change_requests.list`), which the flat module name (`change_requests_list`)
    has lost.

    `DEEP_OBJECT_QUERY_PARAMS`: generated module -> {Python argument: query
    parameter} for every `style: deepObject` query parameter, which
    `busabase/_query.py` re-serializes in oRPC's bracket notation (the generator
    does not implement deepObject).
    """
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    modules = {path.stem: path.parent.name for path in (generated / "api").glob("*/*.py") if path.stem != "__init__"}
    entries: dict[str, str] = {}
    deep_objects: dict[str, dict[str, str]] = {}
    for item in spec["paths"].values():
        for operation in item.values():
            dotted = ".".join(snake(part) for part in operation["operationId"].split("."))
            module = dotted.replace(".", "_")
            if module not in modules:
                sys.exit(f"no generated module {module}.py for operationId {operation['operationId']}")
            entries[dotted] = f"{modules[module]}.{module}"
            deep = [
                param["name"]
                for param in operation.get("parameters", [])
                if param.get("in") == "query" and param.get("style") == "deepObject"
            ]
            if deep:
                arguments = kwargs_arguments(generated / "api" / modules[module] / f"{module}.py")
                deep_objects[entries[dotted]] = {
                    python_argument(wire, arguments, entries[dotted]): wire for wire in deep
                }
    for dotted in entries:
        if any(other.startswith(f"{dotted}.") for other in entries):
            sys.exit(f"{dotted} is both an operation and a group — `bb.{dotted}` would be ambiguous")
    if len(entries) != len(modules):
        sys.exit(f"{len(modules)} generated modules but {len(entries)} operations in openapi.json")
    lines = "".join(f'    "{dotted}": "{module}",\n' for dotted, module in sorted(entries.items()))
    deep_lines = "".join(
        f'    "{module}": {{\n'
        + "".join(f"        {json.dumps(arg)}: {json.dumps(wire)},\n" for arg, wire in params.items())
        + "    },\n"
        for module, params in sorted(deep_objects.items())
    )
    return (
        "# Generated by scripts/generate.py from openapi.json — do not edit.\n"
        '"""Every API operation: its Python path on `Busabase` -> its module under `busabase.generated.api`.\n\n'
        "Plus, per module, its `style: deepObject` query parameters (Python argument -> wire name),\n"
        'which `busabase._query` sends in bracket notation."""\n\n'
        f"OPERATIONS: dict[str, str] = {{\n{lines}}}\n\n"
        f"DEEP_OBJECT_QUERY_PARAMS: dict[str, dict[str, str]] = {{\n{deep_lines}}}\n"
    )


def differences(expected: Path, actual: Path) -> list[str]:
    """Relative paths that differ between two trees, ignoring bytecode caches."""
    found: list[str] = []

    def walk(cmp: filecmp.dircmp[str], prefix: str) -> None:
        for name in cmp.left_only + cmp.right_only + cmp.diff_files + cmp.funny_files:
            found.append(f"{prefix}{name}")
        for name, sub in cmp.subdirs.items():
            walk(sub, f"{prefix}{name}/")

    walk(filecmp.dircmp(expected, actual, ignore=["__pycache__", ".ruff_cache"]), "")
    # dircmp compares by os.stat signature first; force a content comparison.
    for path in sorted(expected.rglob("*.py")):
        rel = path.relative_to(expected)
        other = actual / rel
        if other.exists() and path.read_bytes() != other.read_bytes() and str(rel) not in found:
            found.append(str(rel))
    return sorted(found)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail instead of writing when the code is stale")
    parser.add_argument("--export", action="store_true", help="refresh openapi.json from the contract first")
    args = parser.parse_args()

    if args.export:
        export_spec(check=args.check)

    with tempfile.TemporaryDirectory(prefix="busabase-sdk-gen-") as tmp:
        fresh = Path(tmp) / "generated"
        generate(fresh)
        index = operation_index(fresh)
        if args.check:
            if not TARGET.exists():
                sys.exit(f"{TARGET} does not exist — run scripts/generate.py")
            stale = differences(fresh, TARGET)
            if not INDEX.exists() or INDEX.read_text(encoding="utf-8") != index:
                stale.append(f"../{INDEX.name}")
            if stale:
                shown = "\n  ".join(stale[:20]) + ("\n  …" if len(stale) > 20 else "")
                sys.exit(
                    f"src/busabase/generated is out of date with openapi.json ({len(stale)} files):\n  {shown}\n"
                    "Run `uv run python scripts/generate.py` and commit the result."
                )
            print("src/busabase/generated is up to date with openapi.json")
            return
        shutil.rmtree(TARGET, ignore_errors=True)
        shutil.copytree(fresh, TARGET, ignore=shutil.ignore_patterns("__pycache__", ".ruff_cache"))
        INDEX.write_text(index, encoding="utf-8")
        print(f"regenerated {TARGET.relative_to(ROOT)} from {SPEC.name}")


if __name__ == "__main__":
    main()
