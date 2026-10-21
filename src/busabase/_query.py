"""Object and array query parameters in oRPC's bracket notation.

The Busabase spec declares every object- or array-valued query parameter
`style: deepObject, explode: true`, and the server reads them in oRPC's bracket
notation: `filters[0][fieldSlug]=company&sort[direction]=asc`.
openapi-python-client does not implement deepObject. Left alone, the generated
code sends a list of objects as `filters={'fieldSlug': ...}` (a 400) and spreads
an object into bare keys (`fieldSlug=n&direction=asc`), which the server
silently ignores — an unsorted page that looks like a sorted one.

`install()` wraps the `_get_kwargs` of exactly the generated modules listed in
`_operations.DEEP_OBJECT_QUERY_PARAMS` (emitted by `scripts/generate.py` from
`openapi.json`, so it cannot drift). The wrapper takes those arguments out,
lets the generated code build everything else, and appends them in bracket
notation. Patching the module attribute — which `sync`, `sync_detailed`,
`asyncio` and `asyncio_detailed` all look up at call time — covers the
`bb.<group>.<op>(...)` layer and direct calls into `busabase.generated.api`
alike: importing any generated module imports this package first.
"""

from __future__ import annotations

import functools
import math
from collections.abc import Callable, Mapping
from decimal import Decimal
from importlib import import_module
from typing import Any

from ._operations import DEEP_OBJECT_QUERY_PARAMS
from .generated.types import Unset


def _js_number(value: float) -> str:
    """`Number.prototype.toString()`: `2.0` -> `2`, `1e-7` -> `1e-7`, `1e21` -> `1e+21`."""
    if isinstance(value, int):
        if abs(value) < 10**21:
            return str(value)
        value = float(value)
    if math.isinf(value):
        return "Infinity" if value > 0 else "-Infinity"
    if value == int(value) and abs(value) < 1e21:
        return str(int(value))
    if abs(value) >= 1e21 or abs(value) < 1e-6:
        mantissa, _, exponent = f"{value!r}".partition("e")
        sign = "-" if exponent.startswith("-") else "+"
        return f"{mantissa}e{sign}{int(exponent.lstrip('+-'))}"
    return format(Decimal(repr(value)), "f")


def _escape(segment: str) -> str:
    return segment.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def _plain(value: Any) -> Any:
    """Generated models -> their JSON dicts; lists and dicts recursively."""
    to_dict = getattr(value, "to_dict", None)
    if callable(to_dict):
        return to_dict()
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    if isinstance(value, Mapping):
        return {str(key): _plain(item) for key, item in value.items()}
    return value


def bracket_notation(name: str, value: Any) -> list[tuple[str, str]]:
    """oRPC's `StandardBracketNotationSerializer.serialize` + the OpenAPI codec's leaf rule.

    Arrays add `[index]`, objects add `[key]` (with `\\`, `[` and `]` escaped),
    and only string / number / boolean leaves are sent — `null`, `NaN` and
    empty containers produce nothing, as in the TypeScript client.
    """
    pairs: list[tuple[str, str]] = []

    def walk(node: Any, path: str) -> None:
        if isinstance(node, list):
            for index, item in enumerate(node):
                walk(item, f"{path}[{index}]")
        elif isinstance(node, Mapping):
            for key, item in node.items():
                walk(item, f"{path}[{_escape(str(key))}]")
        elif isinstance(node, bool):
            pairs.append((path, "true" if node else "false"))
        elif isinstance(node, (int, float)):
            if not (isinstance(node, float) and math.isnan(node)):
                pairs.append((path, _js_number(node)))
        elif isinstance(node, str):
            pairs.append((path, node))

    walk(_plain(value), _escape(name))
    return pairs


def _wrap(original: Callable[..., dict[str, Any]], params: Mapping[str, str]) -> Callable[..., dict[str, Any]]:
    @functools.wraps(original)
    def _get_kwargs(*args: Any, **kwargs: Any) -> dict[str, Any]:
        deep = {name: kwargs.pop(name) for name in params if name in kwargs}
        request = original(*args, **kwargs)
        pairs = [
            pair
            for name, value in deep.items()
            if value is not None and not isinstance(value, Unset)
            for pair in bracket_notation(params[name], value)
        ]
        if pairs:
            request["params"] = {**(request.get("params") or {}), **dict(pairs)}
        return request

    _get_kwargs.__busabase_deep_object__ = True  # type: ignore[attr-defined]
    return _get_kwargs


def install() -> None:
    for module_path, params in DEEP_OBJECT_QUERY_PARAMS.items():
        module = import_module(f"{__package__}.generated.api.{module_path}")
        if not getattr(module._get_kwargs, "__busabase_deep_object__", False):
            module._get_kwargs = _wrap(module._get_kwargs, params)
