from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.record_filter import RecordFilter
from ...models.record_value_any_of import RecordValueAnyOf
from ...models.record_value_comparison import RecordValueComparison
from ...models.records_count_response_200 import RecordsCountResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    base_id: str | Unset = UNSET,
    view_id: str | Unset = UNSET,
    filters: list[RecordFilter] | Unset = UNSET,
    value_filters: list[RecordValueAnyOf | RecordValueComparison] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["baseId"] = base_id

    params["viewId"] = view_id

    json_filters: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(filters, Unset):
        json_filters = []
        for filters_item_data in filters:
            filters_item = filters_item_data.to_dict()
            json_filters.append(filters_item)

    params["filters"] = json_filters

    json_value_filters: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(value_filters, Unset):
        json_value_filters = []
        for value_filters_item_data in value_filters:
            value_filters_item: dict[str, Any]
            if isinstance(value_filters_item_data, RecordValueComparison):
                value_filters_item = value_filters_item_data.to_dict()
            else:
                value_filters_item = value_filters_item_data.to_dict()

            json_value_filters.append(value_filters_item)

    params["valueFilters"] = json_value_filters

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/records/count",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RecordsCountResponse200 | None:
    if response.status_code == 200:
        response_200 = RecordsCountResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RecordsCountResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    base_id: str | Unset = UNSET,
    view_id: str | Unset = UNSET,
    filters: list[RecordFilter] | Unset = UNSET,
    value_filters: list[RecordValueAnyOf | RecordValueComparison] | Unset = UNSET,
) -> Response[RecordsCountResponse200]:
    """Count records

     A real SQL COUNT — always the exact total, never a partial or capped number, so it's safe to render
    as a canonical figure (e.g. a dashboard summary tile). Plain `baseId` scoping is always cheap.
    Adding `viewId` and/or `filters` is exact too — provably-exact conditions (e.g. text
    equals/contains, not_empty/is_empty, checkbox is_true/is_false) stay a cheap SQL COUNT; everything
    else falls back to evaluating every matching row server-side, which is exact but not free on a large
    Base. Both `viewId` and `filters` require `baseId`.

    Args:
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404, not
            a 0. Omitting it counts every record in the space. Required as soon as `viewId`, `filters`
            or `valueFilters` is given — a field slug only means something within one Base.
        view_id (str | Unset): Count only what this saved View would display. Its filters apply;
            its sort is ignored, since a count has no order. Requires `baseId`.
        filters (list[RecordFilter] | Unset): Ad-hoc conditions, ANDed with the View's own when
            `viewId` is also given. Unlike `records.list`'s superset `filters`, the COUNT is exact
            either way — but a condition whose exactness cannot be proven makes the server read every
            candidate row instead of running one aggregate, so prefer `valueFilters` where it fits.
            Requires `baseId`.
        value_filters (list[RecordValueAnyOf | RecordValueComparison] | Unset): EXACT value
            comparisons, same shape as `records.list`'s. Always exact, so a count scoped only by these
            stays a single SQL count instead of reading every candidate row. Requires `baseId`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordsCountResponse200]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        view_id=view_id,
        filters=filters,
        value_filters=value_filters,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    base_id: str | Unset = UNSET,
    view_id: str | Unset = UNSET,
    filters: list[RecordFilter] | Unset = UNSET,
    value_filters: list[RecordValueAnyOf | RecordValueComparison] | Unset = UNSET,
) -> RecordsCountResponse200 | None:
    """Count records

     A real SQL COUNT — always the exact total, never a partial or capped number, so it's safe to render
    as a canonical figure (e.g. a dashboard summary tile). Plain `baseId` scoping is always cheap.
    Adding `viewId` and/or `filters` is exact too — provably-exact conditions (e.g. text
    equals/contains, not_empty/is_empty, checkbox is_true/is_false) stay a cheap SQL COUNT; everything
    else falls back to evaluating every matching row server-side, which is exact but not free on a large
    Base. Both `viewId` and `filters` require `baseId`.

    Args:
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404, not
            a 0. Omitting it counts every record in the space. Required as soon as `viewId`, `filters`
            or `valueFilters` is given — a field slug only means something within one Base.
        view_id (str | Unset): Count only what this saved View would display. Its filters apply;
            its sort is ignored, since a count has no order. Requires `baseId`.
        filters (list[RecordFilter] | Unset): Ad-hoc conditions, ANDed with the View's own when
            `viewId` is also given. Unlike `records.list`'s superset `filters`, the COUNT is exact
            either way — but a condition whose exactness cannot be proven makes the server read every
            candidate row instead of running one aggregate, so prefer `valueFilters` where it fits.
            Requires `baseId`.
        value_filters (list[RecordValueAnyOf | RecordValueComparison] | Unset): EXACT value
            comparisons, same shape as `records.list`'s. Always exact, so a count scoped only by these
            stays a single SQL count instead of reading every candidate row. Requires `baseId`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordsCountResponse200
    """

    return sync_detailed(
        client=client,
        base_id=base_id,
        view_id=view_id,
        filters=filters,
        value_filters=value_filters,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    base_id: str | Unset = UNSET,
    view_id: str | Unset = UNSET,
    filters: list[RecordFilter] | Unset = UNSET,
    value_filters: list[RecordValueAnyOf | RecordValueComparison] | Unset = UNSET,
) -> Response[RecordsCountResponse200]:
    """Count records

     A real SQL COUNT — always the exact total, never a partial or capped number, so it's safe to render
    as a canonical figure (e.g. a dashboard summary tile). Plain `baseId` scoping is always cheap.
    Adding `viewId` and/or `filters` is exact too — provably-exact conditions (e.g. text
    equals/contains, not_empty/is_empty, checkbox is_true/is_false) stay a cheap SQL COUNT; everything
    else falls back to evaluating every matching row server-side, which is exact but not free on a large
    Base. Both `viewId` and `filters` require `baseId`.

    Args:
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404, not
            a 0. Omitting it counts every record in the space. Required as soon as `viewId`, `filters`
            or `valueFilters` is given — a field slug only means something within one Base.
        view_id (str | Unset): Count only what this saved View would display. Its filters apply;
            its sort is ignored, since a count has no order. Requires `baseId`.
        filters (list[RecordFilter] | Unset): Ad-hoc conditions, ANDed with the View's own when
            `viewId` is also given. Unlike `records.list`'s superset `filters`, the COUNT is exact
            either way — but a condition whose exactness cannot be proven makes the server read every
            candidate row instead of running one aggregate, so prefer `valueFilters` where it fits.
            Requires `baseId`.
        value_filters (list[RecordValueAnyOf | RecordValueComparison] | Unset): EXACT value
            comparisons, same shape as `records.list`'s. Always exact, so a count scoped only by these
            stays a single SQL count instead of reading every candidate row. Requires `baseId`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordsCountResponse200]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        view_id=view_id,
        filters=filters,
        value_filters=value_filters,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    base_id: str | Unset = UNSET,
    view_id: str | Unset = UNSET,
    filters: list[RecordFilter] | Unset = UNSET,
    value_filters: list[RecordValueAnyOf | RecordValueComparison] | Unset = UNSET,
) -> RecordsCountResponse200 | None:
    """Count records

     A real SQL COUNT — always the exact total, never a partial or capped number, so it's safe to render
    as a canonical figure (e.g. a dashboard summary tile). Plain `baseId` scoping is always cheap.
    Adding `viewId` and/or `filters` is exact too — provably-exact conditions (e.g. text
    equals/contains, not_empty/is_empty, checkbox is_true/is_false) stay a cheap SQL COUNT; everything
    else falls back to evaluating every matching row server-side, which is exact but not free on a large
    Base. Both `viewId` and `filters` require `baseId`.

    Args:
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404, not
            a 0. Omitting it counts every record in the space. Required as soon as `viewId`, `filters`
            or `valueFilters` is given — a field slug only means something within one Base.
        view_id (str | Unset): Count only what this saved View would display. Its filters apply;
            its sort is ignored, since a count has no order. Requires `baseId`.
        filters (list[RecordFilter] | Unset): Ad-hoc conditions, ANDed with the View's own when
            `viewId` is also given. Unlike `records.list`'s superset `filters`, the COUNT is exact
            either way — but a condition whose exactness cannot be proven makes the server read every
            candidate row instead of running one aggregate, so prefer `valueFilters` where it fits.
            Requires `baseId`.
        value_filters (list[RecordValueAnyOf | RecordValueComparison] | Unset): EXACT value
            comparisons, same shape as `records.list`'s. Always exact, so a count scoped only by these
            stays a single SQL count instead of reading every candidate row. Requires `baseId`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordsCountResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            base_id=base_id,
            view_id=view_id,
            filters=filters,
            value_filters=value_filters,
        )
    ).parsed
