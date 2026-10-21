"""The hand-written layer (`busabase.Busabase`), against an in-process mock server.

Covers config resolution (args > env > defaults), the headers every request
carries, ergonomic `bb.<group>.<op>(...)` dispatch, and that every HTTP error —
through the ergonomic path, the generated typed path, sync and async — raises
`BusabaseError` with the server's `code` instead of returning `None`.
"""

from __future__ import annotations

import asyncio
import importlib
import json
from collections.abc import Callable

import httpx
import pytest

from busabase import DEFAULT_BASE_URL, Busabase, BusabaseError
from busabase._operations import OPERATIONS
from busabase.generated.api.records import records_get
from busabase.generated.client import AuthenticatedClient, Client
from busabase.generated.models import Base

ENV = ("BUSABASE_API_KEY", "BUSABASE_BASE_URL", "BUSABASE_SPACE_ID")

BASE_JSON = {
    "id": "bas_1",
    "nodeId": "nod_1",
    "slug": "leads",
    "name": "Leads",
    "description": "",
    "reviewPolicy": {"kind": "single", "requiredApprovals": 1},
    "createdAt": "2026-10-20T00:00:00.000Z",
    "fields": [
        {
            "id": "fld_1",
            "baseId": "bas_1",
            "slug": "company",
            "name": "Company",
            "type": "text",
            "required": False,
            "position": 0,
        }
    ],
}


@pytest.fixture(autouse=True)
def clean_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in ENV:
        monkeypatch.delenv(name, raising=False)


class Recorder:
    """A MockTransport handler that records requests and answers with a canned response."""

    def __init__(self, respond: Callable[[httpx.Request], httpx.Response]) -> None:
        self.respond = respond
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return self.respond(request)

    @property
    def last(self) -> httpx.Request:
        return self.requests[-1]


def make(respond: Callable[[httpx.Request], httpx.Response], **kwargs: object) -> tuple[Busabase, Recorder]:
    recorder = Recorder(respond)
    bb = Busabase(**kwargs, httpx_args={"transport": httpx.MockTransport(recorder)})  # type: ignore[arg-type]
    return bb, recorder


def ok(body: object) -> Callable[[httpx.Request], httpx.Response]:
    return lambda _request: httpx.Response(200, json=body)


def fail(status: int, body: object | None = None, text: str | None = None) -> Callable[[httpx.Request], httpx.Response]:
    if body is not None:
        return lambda _request: httpx.Response(status, json=body)
    return lambda _request: httpx.Response(status, text=text or "")


# ── Configuration ───────────────────────────────────────────────────────────


def test_reads_the_same_env_vars_as_the_cli_and_typescript_sdk(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BUSABASE_API_KEY", "bb_env_key")
    monkeypatch.setenv("BUSABASE_BASE_URL", "https://example.test/api/v1/")
    monkeypatch.setenv("BUSABASE_SPACE_ID", "spc_env")
    bb, recorder = make(ok([BASE_JSON]))

    bb.bases.list()

    request = recorder.last
    assert (request.url.host, request.url.path) == ("example.test", "/api/v1/bases")
    assert request.headers["authorization"] == "Bearer bb_env_key"
    assert request.headers["x-busabase-space"] == "spc_env"
    assert request.headers["x-busabase-channel"] == "sdk"
    assert request.headers["user-agent"].startswith("busabase-python-sdk/")
    assert isinstance(bb.client, AuthenticatedClient)


def test_arguments_win_over_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BUSABASE_API_KEY", "bb_env_key")
    monkeypatch.setenv("BUSABASE_SPACE_ID", "spc_env")
    bb, recorder = make(ok([]), api_key="bb_arg", base_url="http://localhost:15419", space="spc_arg")

    bb.bases.list()

    assert recorder.last.url.host == "localhost"
    assert recorder.last.headers["authorization"] == "Bearer bb_arg"
    assert recorder.last.headers["x-busabase-space"] == "spc_arg"


def test_defaults_to_busabase_cloud_and_sends_no_auth_without_a_key() -> None:
    bb, recorder = make(ok([]))

    bb.bases.list()

    assert bb.base_url == DEFAULT_BASE_URL == "https://busabase.com"
    assert str(recorder.last.url).startswith("https://busabase.com/api/v1/bases")
    assert "authorization" not in recorder.last.headers
    assert "x-busabase-space" not in recorder.last.headers
    assert isinstance(bb.client, Client)


# ── Calling operations ─────────────────────────────────────────────────────


def test_returns_generated_models() -> None:
    bb, _ = make(ok([BASE_JSON]))

    bases = bb.bases.list()

    assert [type(base) for base in bases] == [Base]
    assert bases[0].slug == "leads"
    assert bases[0].fields[0].type_ == "text"


def test_a_plain_dict_body_is_sent_as_is() -> None:
    body = {"name": "Notes", "slug": "notes", "body": "# Hi", "message": "Add notes"}
    bb, recorder = make(fail(409, {"error": "A Doc with this slug exists", "code": "CONFLICT"}))

    with pytest.raises(BusabaseError):
        bb.docs.create(body=body)

    assert recorder.last.method == "POST"
    assert recorder.last.url.path == "/api/v1/docs"
    assert json.loads(recorder.last.content) == body


def test_nested_groups_and_discovery() -> None:
    bb, recorder = make(ok([]))

    bb.nodes.share.list()

    assert recorder.last.url.path == "/api/v1/node-shares"
    assert {"bases", "records", "change_requests", "docs", "nodes", "search", "grep"} <= set(dir(bb))
    assert {"list", "get", "change_request", "list_page"} <= set(dir(bb.records))
    with pytest.raises(AttributeError, match="recordz"):
        _ = bb.recordz
    with pytest.raises(AttributeError, match="records.lisst"):
        _ = bb.records.lisst


def test_every_indexed_operation_resolves_to_a_generated_module() -> None:
    assert len(OPERATIONS) >= 120
    for module in OPERATIONS.values():
        loaded = importlib.import_module(f"busabase.generated.api.{module}")
        assert callable(loaded.sync) and callable(loaded.asyncio)


# ── Errors ─────────────────────────────────────────────────────────────────


def test_error_envelope_becomes_a_typed_error() -> None:
    bb, _ = make(fail(404, {"error": "Record not found", "code": "NOT_FOUND"}))

    with pytest.raises(BusabaseError) as caught:
        bb.records.get(record_id="rec_missing")

    error = caught.value
    assert (error.status, error.code, error.message) == (404, "NOT_FOUND", "Record not found")
    assert str(error) == "NOT_FOUND (404): Record not found"
    assert error.response is not None and error.response.status_code == 404


def test_validation_issues_are_spelled_out() -> None:
    body = {
        "error": "Input validation failed",
        "code": "BAD_REQUEST",
        "data": {"issues": [{"path": ["fields", 0, "slug"], "message": "Required"}]},
    }
    bb, _ = make(fail(400, body))

    with pytest.raises(BusabaseError) as caught:
        bb.bases.create(body={"name": "x", "fields": [{}]})

    assert caught.value.code == "BAD_REQUEST"
    assert caught.value.message == "Input validation failed — fields.0.slug: Required"
    assert caught.value.data == body["data"]


def test_a_non_json_error_still_raises() -> None:
    bb, _ = make(fail(502, text="Bad gateway"))

    with pytest.raises(BusabaseError) as caught:
        bb.bases.list()

    assert (caught.value.status, caught.value.code, caught.value.message) == (502, "HTTP_502", "Bad gateway")


def test_the_generated_typed_path_raises_too() -> None:
    bb, _ = make(fail(403, {"error": "No access to this space", "code": "FORBIDDEN"}))

    with pytest.raises(BusabaseError, match="FORBIDDEN"):
        records_get.sync(client=bb.client, record_id="rec_1")


def test_async_calls_parse_and_raise() -> None:
    async def run() -> None:
        bb, _ = make(ok([BASE_JSON]))
        bases = await bb.bases.list.asyncio()
        assert bases[0].name == "Leads"

        bb, _ = make(fail(404, {"error": "Record not found", "code": "NOT_FOUND"}))
        with pytest.raises(BusabaseError) as caught:
            await bb.records.get.asyncio(record_id="rec_missing")
        assert caught.value.code == "NOT_FOUND"

    asyncio.run(run())
