"""Object and array query parameters go on the wire in oRPC's bracket notation.

The spec declares them `style: deepObject, explode: true`, which
openapi-python-client does not implement: left alone it sends a list of objects
as `filters={'fieldSlug': ...}` (a 400) and an object as its bare keys
(`fieldSlug=n&direction=asc`, which the server silently ignores). The server
parses `filters[0][fieldSlug]=company` — oRPC's `StandardBracketNotationSerializer`
— so that is what these assert, byte for byte.
"""

from __future__ import annotations

import asyncio
import importlib
import inspect
from collections.abc import Callable
from urllib.parse import unquote

import httpx
import pytest

from busabase import Busabase
from busabase._operations import DEEP_OBJECT_QUERY_PARAMS
from busabase._query import bracket_notation
from busabase.generated.api.change_requests import change_requests_list
from busabase.generated.api.records import records_count, records_list
from busabase.generated.client import Client
from busabase.generated.models import (
    RecordFilter,
    RecordsGroupByAggregatesItem,
    RecordsListPageDateRange,
    RecordSort,
    RecordValueAnyOf,
    RecordValueComparison,
)

RECORDS_PAGE = {"records": [], "nextCursor": None}


def recording(body: object) -> tuple[list[httpx.Request], Callable[[httpx.Request], httpx.Response]]:
    seen: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json=body)

    return seen, respond


def query(request: httpx.Request) -> str:
    return unquote(request.url.query.decode())


def make(body: object) -> tuple[Busabase, list[httpx.Request]]:
    seen, respond = recording(body)
    return Busabase(base_url="http://bb.test", httpx_args={"transport": httpx.MockTransport(respond)}), seen


def test_filters_value_filters_and_sort_through_the_wrapper() -> None:
    bb, seen = make(RECORDS_PAGE)
    bb.records.list(
        base_id="leads",
        filters=[
            RecordFilter(field_slug="company", operator="equals", value="Acme"),
            RecordFilter(field_slug="tags", operator="contains", value=["vip", "eu"]),
        ],
        value_filters=[
            RecordValueComparison(field_slug="n", operator="gte", value=2),
            RecordValueAnyOf(
                any_=[
                    RecordValueComparison(field_slug="n", operator="eq", value=1.5),
                    RecordValueComparison(field_slug="done", operator="eq", value=True),
                ]
            ),
        ],
        sort=RecordSort(field_slug="n", field_type="number", direction="desc"),
    )
    assert query(seen[-1]) == (
        "limit=50&baseId=leads&status=active"
        "&filters[0][fieldSlug]=company&filters[0][operator]=equals&filters[0][value]=Acme"
        "&filters[1][fieldSlug]=tags&filters[1][operator]=contains"
        "&filters[1][value][0]=vip&filters[1][value][1]=eu"
        "&valueFilters[0][fieldSlug]=n&valueFilters[0][operator]=gte&valueFilters[0][value]=2"
        "&valueFilters[1][any][0][fieldSlug]=n&valueFilters[1][any][0][operator]=eq"
        "&valueFilters[1][any][0][value]=1.5"
        "&valueFilters[1][any][1][fieldSlug]=done&valueFilters[1][any][1][operator]=eq"
        "&valueFilters[1][any][1][value]=true"
        "&sort[fieldSlug]=n&sort[fieldType]=number&sort[direction]=desc"
    )


def test_the_generated_module_called_directly_serializes_the_same_way() -> None:
    seen, respond = recording(RECORDS_PAGE)
    client = Client(base_url="http://bb.test", httpx_args={"transport": httpx.MockTransport(respond)})
    records_list.sync(client=client, base_id="leads", sort=RecordSort(field_slug="n"))
    assert query(seen[-1]) == "limit=50&baseId=leads&status=active&sort[fieldSlug]=n&sort[direction]=asc"


def test_async_and_plain_dicts() -> None:
    bb, seen = make({"total": 0})

    async def run() -> None:
        await bb.records.count.asyncio(
            base_id="leads",
            value_filters=[{"any": [{"fieldSlug": "n", "operator": "lt", "value": 0}]}],
        )

    asyncio.run(run())
    assert query(seen[-1]) == (
        "baseId=leads&valueFilters[0][any][0][fieldSlug]=n"
        "&valueFilters[0][any][0][operator]=lt&valueFilters[0][any][0][value]=0"
    )


def test_every_operation_with_object_or_array_query_params() -> None:
    bb, seen = make({"changeRequests": [], "nextCursor": None})
    bb.change_requests.list(status=["in_review", "merged"])
    assert query(seen[-1]) == "limit=50&status[0]=in_review&status[1]=merged"

    bb, seen = make({"records": [], "total": 0, "totalPages": 0, "page": 1, "pageSize": 50})
    bb.records.list_page(
        base_id="leads",
        date_range=RecordsListPageDateRange(field_slug="due", gte="2026-10-01", lt="2026-11-01"),
        sort=RecordSort(field_slug="due", field_type="date"),
    )
    assert query(seen[-1]) == (
        "baseId=leads&page=1&pageSize=50"
        "&dateRange[fieldSlug]=due&dateRange[gte]=2026-10-01&dateRange[lt]=2026-11-01"
        "&sort[fieldSlug]=due&sort[fieldType]=date&sort[direction]=asc"
    )

    bb, seen = make({"groups": [], "total": 0})
    bb.records.group_by(
        base_id="leads",
        aggregates=[RecordsGroupByAggregatesItem(fn="sum", field_slug="n")],
        filters=[RecordFilter(field_slug="done", operator="is_true")],
    )
    assert query(seen[-1]) == (
        "baseId=leads&bucketing=grid"
        "&aggregates[0][fn]=sum&aggregates[0][fieldSlug]=n"
        "&filters[0][fieldSlug]=done&filters[0][operator]=is_true"
    )


def test_unset_and_empty_values_send_nothing() -> None:
    seen, respond = recording({"total": 0})
    client = Client(base_url="http://bb.test", httpx_args={"transport": httpx.MockTransport(respond)})
    records_count.sync(client=client, base_id="leads", filters=[], value_filters=None)  # type: ignore[arg-type]
    assert query(seen[-1]) == "baseId=leads"
    seen, respond = recording({"changeRequests": [], "nextCursor": None})
    client = Client(base_url="http://bb.test", httpx_args={"transport": httpx.MockTransport(respond)})
    change_requests_list.sync(client=client)
    assert query(seen[-1]) == "limit=50"


def test_bracket_notation_mirrors_orpc() -> None:
    # Escaping of `[`, `]` and `\\` in keys; null leaves dropped; numbers as JS prints them.
    assert bracket_notation("f", {"a[b]": 1, "c\\d": None, "e": [2.0, False, 1e-7]}) == [
        ("f[a\\[b\\]]", "1"),
        ("f[e][0]", "2"),
        ("f[e][1]", "false"),
        ("f[e][2]", "1e-7"),
    ]


@pytest.mark.parametrize("module_path", sorted(DEEP_OBJECT_QUERY_PARAMS))
def test_index_matches_the_generated_signatures(module_path: str) -> None:
    module = importlib.import_module(f"busabase.generated.api.{module_path}")
    original = getattr(module._get_kwargs, "__wrapped__", None)
    assert original is not None, f"{module_path}._get_kwargs is not patched"
    params = inspect.signature(original).parameters
    for python_name in DEEP_OBJECT_QUERY_PARAMS[module_path]:
        assert python_name in params
