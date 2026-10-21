"""The committed generated code must be exactly what openapi.json produces.

`scripts/generate.py --check` regenerates into a temp dir with the pinned
openapi-python-client + ruff and compares byte-for-byte (plus `_operations.py`).
A hand edit under `src/busabase/generated/`, or an `openapi.json` update that
was not regenerated, fails here. (In the Busabase monorepo, CI separately
checks that `openapi.json` matches the API contract —
`packages/busabase-core/tests/openapi-sdk-spec.test.ts`.)
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_generated_code_matches_openapi_json() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate.py"), "--check"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
