from __future__ import annotations

import importlib
import os
from collections.abc import Awaitable, Mapping
from types import ModuleType
from typing import Any, Self

import httpx

from . import generated
from ._errors import BusabaseError
from ._operations import OPERATIONS
from ._version import __version__
from .generated import api as _generated_api  # noqa: F401  (makes `generated.api` an attribute)
from .generated.client import AuthenticatedClient, Client

DEFAULT_BASE_URL = "https://busabase.com"
"""Busabase Cloud. Pass `base_url` (or set `BUSABASE_BASE_URL`) for a self-hosted server."""


def _env(name: str) -> str | None:
    value = os.environ.get(name)
    return value or None


def normalize_base_url(raw: str) -> str:
    """Accept the server root with or without `/api/v1` — the generated paths already carry it."""
    url = raw.rstrip("/")
    return url.removesuffix("/api/v1")


def _raise_for_status(response: httpx.Response) -> Awaitable[None] | None:
    """httpx response hook: turn every >= 400 into a `BusabaseError`.

    The generated functions return the parsed `Error` model (or `None`) for an
    error status instead of raising, which makes a failed write easy to miss.
    A hook fixes that once for every call, typed or not. The same `httpx_args`
    feed both the sync and the async httpx client, so the hook serves both: an
    async client awaits what it returns.
    """
    if isinstance(response.stream, httpx.AsyncByteStream):
        return _araise_for_status(response)
    if response.status_code >= 400:
        response.read()
        raise BusabaseError.from_response(response)
    return None


async def _araise_for_status(response: httpx.Response) -> None:
    if response.status_code >= 400:
        await response.aread()
        raise BusabaseError.from_response(response)


class _JsonBody:
    """Lets a plain dict stand in for a generated request-body model: they only call `.to_dict()`."""

    def __init__(self, data: Mapping[str, Any]) -> None:
        self._data = dict(data)

    def to_dict(self) -> dict[str, Any]:
        return self._data


def _prepare(kwargs: dict[str, Any]) -> dict[str, Any]:
    body = kwargs.get("body")
    if isinstance(body, Mapping):
        kwargs = {**kwargs, "body": _JsonBody(body)}
    return kwargs


class Operation:
    """One API operation bound to a client: `bb.records.list(base_id=...)`.

    Calls the generated module's `sync()` (or `asyncio()` via `.asyncio(...)`)
    and returns its parsed model. Arguments are the generated function's —
    path parameters positional or by name (`bb.nodes.get("nod_1")`), the rest
    by name; `body` may be a plain dict instead of the generated model.
    """

    def __init__(self, client: AuthenticatedClient | Client, module: ModuleType) -> None:
        self._client = client
        self.module = module
        self.__doc__ = module.sync.__doc__

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.module.sync(*args, client=self._client, **_prepare(kwargs))

    async def asyncio(self, *args: Any, **kwargs: Any) -> Any:
        return await self.module.asyncio(*args, client=self._client, **_prepare(kwargs))

    def __repr__(self) -> str:
        return f"<busabase operation {self.module.__name__.rsplit('.', 1)[1]}>"


class _Group:
    """A namespace of operations, e.g. `bb.records` or `bb.nodes.share` (paths from `_operations.py`)."""

    def __init__(self, client: AuthenticatedClient | Client, path: str) -> None:
        self._client = client
        self._path = path

    def __getattr__(self, name: str) -> Operation | _Group:
        if name.startswith("_"):
            raise AttributeError(name)
        return _resolve(self._client, f"{self._path}.{name}" if self._path else name)

    def __dir__(self) -> list[str]:
        start = f"{self._path}." if self._path else ""
        return sorted({path[len(start) :].split(".")[0] for path in OPERATIONS if path.startswith(start)})

    def __repr__(self) -> str:
        return f"<busabase group {self._path}: {', '.join(self.__dir__())}>"


def _resolve(client: AuthenticatedClient | Client, path: str) -> Operation | _Group:
    if path in OPERATIONS:
        return Operation(client, importlib.import_module(f"{generated.api.__name__}.{OPERATIONS[path]}"))
    if any(other.startswith(f"{path}.") for other in OPERATIONS):
        return _Group(client, path)
    raise AttributeError(f"Busabase has no API operation or group {path!r}")


class Busabase:
    """Client for the Busabase REST API — Busabase Cloud or a self-hosted server.

    Every argument falls back to an environment variable, the same ones the
    Busabase CLI and TypeScript SDK read:

    - `api_key`  -> `BUSABASE_API_KEY` (omit for an open local self-hosted server)
    - `base_url` -> `BUSABASE_BASE_URL`, then `https://busabase.com`
    - `space`    -> `BUSABASE_SPACE_ID`, sent as `x-busabase-space`; needed on
      Cloud when your key belongs to more than one space

    Operations are grouped like the API: `bb.bases.list()`,
    `bb.records.get(record_id=...)`, `bb.docs.create(body={...})`. Each is the
    generated function of the same name in `busabase.generated.api`, called
    with this client; use those directly (`records_list.sync(client=bb.client)`)
    when you want full static typing. Any status >= 400 raises `BusabaseError`.

    `headers` are sent with every request; `httpx_args` go to the underlying
    `httpx.Client` / `httpx.AsyncClient` (e.g. `transport`, `proxy`, `verify`).
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        space: str | None = None,
        *,
        timeout: float | httpx.Timeout = 30.0,
        headers: Mapping[str, str] | None = None,
        httpx_args: Mapping[str, Any] | None = None,
    ) -> None:
        self.api_key = api_key or _env("BUSABASE_API_KEY")
        self.base_url = normalize_base_url(base_url or _env("BUSABASE_BASE_URL") or DEFAULT_BASE_URL)
        self.space = space or _env("BUSABASE_SPACE_ID")

        all_headers = {
            # Recorded as the source channel on Change Requests and audit events.
            "x-busabase-channel": "sdk",
            "user-agent": f"busabase-python-sdk/{__version__}",
        }
        if self.space:
            all_headers["x-busabase-space"] = self.space
        all_headers.update(headers or {})

        extra = dict(httpx_args or {})
        hooks = dict(extra.pop("event_hooks", {}))
        hooks["response"] = [*hooks.get("response", []), _raise_for_status]
        options: dict[str, Any] = {
            "base_url": self.base_url,
            "headers": all_headers,
            "timeout": timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout),
            # Belt and braces: an undocumented 2xx/3xx raises instead of returning None.
            "raise_on_unexpected_status": True,
            "httpx_args": {**extra, "event_hooks": hooks},
        }
        # The generated client sets `Authorization: Bearer <token>`; a local
        # self-hosted server needs no key, and an empty bearer would be wrong.
        self.client: AuthenticatedClient | Client = (
            AuthenticatedClient(token=self.api_key, **options) if self.api_key else Client(**options)
        )

    def __getattr__(self, name: str) -> Operation | _Group:
        if name.startswith("_"):
            raise AttributeError(name)
        return _resolve(self.client, name)

    def __dir__(self) -> list[str]:
        return sorted(set(super().__dir__()) | set(_Group(self.client, "").__dir__()))

    def close(self) -> None:
        """Close the underlying HTTP connection pool."""
        self.client.get_httpx_client().close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def __repr__(self) -> str:
        return f"Busabase(base_url={self.base_url!r}, space={self.space!r}, api_key={'set' if self.api_key else None})"


__all__ = ["DEFAULT_BASE_URL", "Busabase", "BusabaseError", "Operation", "generated", "normalize_base_url"]
