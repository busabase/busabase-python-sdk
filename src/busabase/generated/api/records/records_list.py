from http import HTTPStatus
from typing import Any, Literal

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.record_filter import RecordFilter
from ...models.record_sort import RecordSort
from ...models.record_value_any_of import RecordValueAnyOf
from ...models.record_value_comparison import RecordValueComparison
from ...models.records_list_response_200 import RecordsListResponse200
from ...models.records_list_status import RecordsListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    base_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    status: RecordsListStatus | Unset = "active",
    summary: Literal["false", "true"] | bool | Unset = UNSET,
    filters: list[RecordFilter] | Unset = UNSET,
    value_filters: list[RecordValueAnyOf | RecordValueComparison] | Unset = UNSET,
    sort: RecordSort | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["baseId"] = base_id

    params["cursor"] = cursor

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_summary: Literal["false", "true"] | bool | Unset
    if isinstance(summary, Unset):
        json_summary = UNSET
    else:
        json_summary = summary
    params["summary"] = json_summary

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

    json_sort: dict[str, Any] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.to_dict()
    if not isinstance(json_sort, Unset):
        params.update(json_sort)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/records",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RecordsListResponse200 | None:
    if response.status_code == 200:
        response_200 = RecordsListResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RecordsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    base_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    status: RecordsListStatus | Unset = "active",
    summary: Literal["false", "true"] | bool | Unset = UNSET,
    filters: list[RecordFilter] | Unset = UNSET,
    value_filters: list[RecordValueAnyOf | RecordValueComparison] | Unset = UNSET,
    sort: RecordSort | Unset = UNSET,
) -> Response[RecordsListResponse200]:
    """List records

    Args:
        limit (int | Unset): Records per page. Capped at 100; ask for the next page with `cursor`.
            Default: 50.
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404,
            never an empty page. OMITTING it lists records across the WHOLE SPACE, which is rarely
            what a caller means and is easy to miss — every other parameter still applies, so an
            unscoped query looks like it worked.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it — it is keyed on `createdAt`, or on the sort field
            when `sort` is given, and that is an implementation detail.
        status (RecordsListStatus | Unset): `active` is the live table; `archived` is the Base's
            trash. Default: 'active'.
        summary (bool | Literal['false'] | Literal['true'] | Unset): Return compact list previews:
            field values larger than 4 KB are replaced with omission markers, and Base field
            definitions and computed lookup values are omitted. Omit for full records; use records.get
            to read the complete content of a selected row.
        filters (list[RecordFilter] | Unset): View filters — a best-effort SUPERSET, not an exact
            answer. They mean what the grid means (a currency number reads as "$1,234.00", a select as
            its choice label), and the server may return records that do not match, so the caller must
            narrow them again and must NOT trust `limit` alongside them. Use `valueFilters` when you
            need an exact row set.
        value_filters (list[RecordValueAnyOf | RecordValueComparison] | Unset): EXACT value
            comparisons, unlike `filters` which are a best-effort superset. The returned rows are
            exactly those that match, so `limit` can be trusted alongside them. Entries are ANDed; an
            entry may instead be `{ any: [...] }` to OR its comparisons, which makes the list a CNF
            and can express any boolean combination. Requires `baseId`. Compares number, date,
            checkbox and text-like fields (text and select support eq/ne only); anything else is a 400
            rather than a silently dropped condition.
        sort (RecordSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordsListResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        base_id=base_id,
        cursor=cursor,
        status=status,
        summary=summary,
        filters=filters,
        value_filters=value_filters,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    base_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    status: RecordsListStatus | Unset = "active",
    summary: Literal["false", "true"] | bool | Unset = UNSET,
    filters: list[RecordFilter] | Unset = UNSET,
    value_filters: list[RecordValueAnyOf | RecordValueComparison] | Unset = UNSET,
    sort: RecordSort | Unset = UNSET,
) -> RecordsListResponse200 | None:
    """List records

    Args:
        limit (int | Unset): Records per page. Capped at 100; ask for the next page with `cursor`.
            Default: 50.
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404,
            never an empty page. OMITTING it lists records across the WHOLE SPACE, which is rarely
            what a caller means and is easy to miss — every other parameter still applies, so an
            unscoped query looks like it worked.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it — it is keyed on `createdAt`, or on the sort field
            when `sort` is given, and that is an implementation detail.
        status (RecordsListStatus | Unset): `active` is the live table; `archived` is the Base's
            trash. Default: 'active'.
        summary (bool | Literal['false'] | Literal['true'] | Unset): Return compact list previews:
            field values larger than 4 KB are replaced with omission markers, and Base field
            definitions and computed lookup values are omitted. Omit for full records; use records.get
            to read the complete content of a selected row.
        filters (list[RecordFilter] | Unset): View filters — a best-effort SUPERSET, not an exact
            answer. They mean what the grid means (a currency number reads as "$1,234.00", a select as
            its choice label), and the server may return records that do not match, so the caller must
            narrow them again and must NOT trust `limit` alongside them. Use `valueFilters` when you
            need an exact row set.
        value_filters (list[RecordValueAnyOf | RecordValueComparison] | Unset): EXACT value
            comparisons, unlike `filters` which are a best-effort superset. The returned rows are
            exactly those that match, so `limit` can be trusted alongside them. Entries are ANDed; an
            entry may instead be `{ any: [...] }` to OR its comparisons, which makes the list a CNF
            and can express any boolean combination. Requires `baseId`. Compares number, date,
            checkbox and text-like fields (text and select support eq/ne only); anything else is a 400
            rather than a silently dropped condition.
        sort (RecordSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordsListResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        base_id=base_id,
        cursor=cursor,
        status=status,
        summary=summary,
        filters=filters,
        value_filters=value_filters,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    base_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    status: RecordsListStatus | Unset = "active",
    summary: Literal["false", "true"] | bool | Unset = UNSET,
    filters: list[RecordFilter] | Unset = UNSET,
    value_filters: list[RecordValueAnyOf | RecordValueComparison] | Unset = UNSET,
    sort: RecordSort | Unset = UNSET,
) -> Response[RecordsListResponse200]:
    """List records

    Args:
        limit (int | Unset): Records per page. Capped at 100; ask for the next page with `cursor`.
            Default: 50.
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404,
            never an empty page. OMITTING it lists records across the WHOLE SPACE, which is rarely
            what a caller means and is easy to miss — every other parameter still applies, so an
            unscoped query looks like it worked.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it — it is keyed on `createdAt`, or on the sort field
            when `sort` is given, and that is an implementation detail.
        status (RecordsListStatus | Unset): `active` is the live table; `archived` is the Base's
            trash. Default: 'active'.
        summary (bool | Literal['false'] | Literal['true'] | Unset): Return compact list previews:
            field values larger than 4 KB are replaced with omission markers, and Base field
            definitions and computed lookup values are omitted. Omit for full records; use records.get
            to read the complete content of a selected row.
        filters (list[RecordFilter] | Unset): View filters — a best-effort SUPERSET, not an exact
            answer. They mean what the grid means (a currency number reads as "$1,234.00", a select as
            its choice label), and the server may return records that do not match, so the caller must
            narrow them again and must NOT trust `limit` alongside them. Use `valueFilters` when you
            need an exact row set.
        value_filters (list[RecordValueAnyOf | RecordValueComparison] | Unset): EXACT value
            comparisons, unlike `filters` which are a best-effort superset. The returned rows are
            exactly those that match, so `limit` can be trusted alongside them. Entries are ANDed; an
            entry may instead be `{ any: [...] }` to OR its comparisons, which makes the list a CNF
            and can express any boolean combination. Requires `baseId`. Compares number, date,
            checkbox and text-like fields (text and select support eq/ne only); anything else is a 400
            rather than a silently dropped condition.
        sort (RecordSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordsListResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        base_id=base_id,
        cursor=cursor,
        status=status,
        summary=summary,
        filters=filters,
        value_filters=value_filters,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    base_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    status: RecordsListStatus | Unset = "active",
    summary: Literal["false", "true"] | bool | Unset = UNSET,
    filters: list[RecordFilter] | Unset = UNSET,
    value_filters: list[RecordValueAnyOf | RecordValueComparison] | Unset = UNSET,
    sort: RecordSort | Unset = UNSET,
) -> RecordsListResponse200 | None:
    """List records

    Args:
        limit (int | Unset): Records per page. Capped at 100; ask for the next page with `cursor`.
            Default: 50.
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404,
            never an empty page. OMITTING it lists records across the WHOLE SPACE, which is rarely
            what a caller means and is easy to miss — every other parameter still applies, so an
            unscoped query looks like it worked.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it — it is keyed on `createdAt`, or on the sort field
            when `sort` is given, and that is an implementation detail.
        status (RecordsListStatus | Unset): `active` is the live table; `archived` is the Base's
            trash. Default: 'active'.
        summary (bool | Literal['false'] | Literal['true'] | Unset): Return compact list previews:
            field values larger than 4 KB are replaced with omission markers, and Base field
            definitions and computed lookup values are omitted. Omit for full records; use records.get
            to read the complete content of a selected row.
        filters (list[RecordFilter] | Unset): View filters — a best-effort SUPERSET, not an exact
            answer. They mean what the grid means (a currency number reads as "$1,234.00", a select as
            its choice label), and the server may return records that do not match, so the caller must
            narrow them again and must NOT trust `limit` alongside them. Use `valueFilters` when you
            need an exact row set.
        value_filters (list[RecordValueAnyOf | RecordValueComparison] | Unset): EXACT value
            comparisons, unlike `filters` which are a best-effort superset. The returned rows are
            exactly those that match, so `limit` can be trusted alongside them. Entries are ANDed; an
            entry may instead be `{ any: [...] }` to OR its comparisons, which makes the list a CNF
            and can express any boolean combination. Requires `baseId`. Compares number, date,
            checkbox and text-like fields (text and select support eq/ne only); anything else is a 400
            rather than a silently dropped condition.
        sort (RecordSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            base_id=base_id,
            cursor=cursor,
            status=status,
            summary=summary,
            filters=filters,
            value_filters=value_filters,
            sort=sort,
        )
    ).parsed
