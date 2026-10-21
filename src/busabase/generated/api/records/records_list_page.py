from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.records_list_page_date_range import RecordsListPageDateRange
from ...models.records_list_page_filters_item import RecordsListPageFiltersItem
from ...models.records_list_page_response_200 import RecordsListPageResponse200
from ...models.records_list_page_sort import RecordsListPageSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    base_id: str,
    view_id: str | Unset = UNSET,
    filters: list[RecordsListPageFiltersItem] | Unset = UNSET,
    date_range: RecordsListPageDateRange | Unset = UNSET,
    sort: RecordsListPageSort | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
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

    json_date_range: dict[str, Any] | Unset = UNSET
    if not isinstance(date_range, Unset):
        json_date_range = date_range.to_dict()
    if not isinstance(json_date_range, Unset):
        params.update(json_date_range)

    json_sort: dict[str, Any] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.to_dict()
    if not isinstance(json_sort, Unset):
        params.update(json_sort)

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/records/page",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RecordsListPageResponse200 | None:
    if response.status_code == 200:
        response_200 = RecordsListPageResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RecordsListPageResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    base_id: str,
    view_id: str | Unset = UNSET,
    filters: list[RecordsListPageFiltersItem] | Unset = UNSET,
    date_range: RecordsListPageDateRange | Unset = UNSET,
    sort: RecordsListPageSort | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> Response[RecordsListPageResponse200]:
    """List a numbered record page

    Args:
        base_id (str): Required here, unlike `records.list` where omitting it spans the whole
            space.
        view_id (str | Unset): Show only what this saved View would: its filters and its sort.
        filters (list[RecordsListPageFiltersItem] | Unset): Extra conditions ANDed with the View's
            own — "this View, further narrowed". Unlike `records.list`'s `filters`, these are EXACT:
            every page is precisely what the client's own matcher would keep, so a page is never
            missing records it should hold.
        date_range (RecordsListPageDateRange | Unset): Scope the page to a
            `date`/`created_time`/`updated_time` field falling in `[gte, lt)` — a half-open range of
            absolute UTC instants, not a `filters` condition. Resolve the bounds yourself: a day or a
            month only means something in a timezone, and the server does not know the viewer's.
        sort (RecordsListPageSort | Unset): Sort by one field. Only number and date fields sort
            authoritatively (their typed value column matches a client's own ordering); any other
            field type is returned in the default order and left for the caller to sort. Replaces the
            saved View's sort when `viewId` is also given (the View's filters still apply). Empty
            values sort last; ties are broken by record id, so pages never overlap.
        page (int | Unset): 1-indexed, not 0-indexed. Default: 1.
        page_size (int | Unset): Records per page. Capped at 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordsListPageResponse200]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        view_id=view_id,
        filters=filters,
        date_range=date_range,
        sort=sort,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    base_id: str,
    view_id: str | Unset = UNSET,
    filters: list[RecordsListPageFiltersItem] | Unset = UNSET,
    date_range: RecordsListPageDateRange | Unset = UNSET,
    sort: RecordsListPageSort | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> RecordsListPageResponse200 | None:
    """List a numbered record page

    Args:
        base_id (str): Required here, unlike `records.list` where omitting it spans the whole
            space.
        view_id (str | Unset): Show only what this saved View would: its filters and its sort.
        filters (list[RecordsListPageFiltersItem] | Unset): Extra conditions ANDed with the View's
            own — "this View, further narrowed". Unlike `records.list`'s `filters`, these are EXACT:
            every page is precisely what the client's own matcher would keep, so a page is never
            missing records it should hold.
        date_range (RecordsListPageDateRange | Unset): Scope the page to a
            `date`/`created_time`/`updated_time` field falling in `[gte, lt)` — a half-open range of
            absolute UTC instants, not a `filters` condition. Resolve the bounds yourself: a day or a
            month only means something in a timezone, and the server does not know the viewer's.
        sort (RecordsListPageSort | Unset): Sort by one field. Only number and date fields sort
            authoritatively (their typed value column matches a client's own ordering); any other
            field type is returned in the default order and left for the caller to sort. Replaces the
            saved View's sort when `viewId` is also given (the View's filters still apply). Empty
            values sort last; ties are broken by record id, so pages never overlap.
        page (int | Unset): 1-indexed, not 0-indexed. Default: 1.
        page_size (int | Unset): Records per page. Capped at 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordsListPageResponse200
    """

    return sync_detailed(
        client=client,
        base_id=base_id,
        view_id=view_id,
        filters=filters,
        date_range=date_range,
        sort=sort,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    base_id: str,
    view_id: str | Unset = UNSET,
    filters: list[RecordsListPageFiltersItem] | Unset = UNSET,
    date_range: RecordsListPageDateRange | Unset = UNSET,
    sort: RecordsListPageSort | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> Response[RecordsListPageResponse200]:
    """List a numbered record page

    Args:
        base_id (str): Required here, unlike `records.list` where omitting it spans the whole
            space.
        view_id (str | Unset): Show only what this saved View would: its filters and its sort.
        filters (list[RecordsListPageFiltersItem] | Unset): Extra conditions ANDed with the View's
            own — "this View, further narrowed". Unlike `records.list`'s `filters`, these are EXACT:
            every page is precisely what the client's own matcher would keep, so a page is never
            missing records it should hold.
        date_range (RecordsListPageDateRange | Unset): Scope the page to a
            `date`/`created_time`/`updated_time` field falling in `[gte, lt)` — a half-open range of
            absolute UTC instants, not a `filters` condition. Resolve the bounds yourself: a day or a
            month only means something in a timezone, and the server does not know the viewer's.
        sort (RecordsListPageSort | Unset): Sort by one field. Only number and date fields sort
            authoritatively (their typed value column matches a client's own ordering); any other
            field type is returned in the default order and left for the caller to sort. Replaces the
            saved View's sort when `viewId` is also given (the View's filters still apply). Empty
            values sort last; ties are broken by record id, so pages never overlap.
        page (int | Unset): 1-indexed, not 0-indexed. Default: 1.
        page_size (int | Unset): Records per page. Capped at 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordsListPageResponse200]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        view_id=view_id,
        filters=filters,
        date_range=date_range,
        sort=sort,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    base_id: str,
    view_id: str | Unset = UNSET,
    filters: list[RecordsListPageFiltersItem] | Unset = UNSET,
    date_range: RecordsListPageDateRange | Unset = UNSET,
    sort: RecordsListPageSort | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> RecordsListPageResponse200 | None:
    """List a numbered record page

    Args:
        base_id (str): Required here, unlike `records.list` where omitting it spans the whole
            space.
        view_id (str | Unset): Show only what this saved View would: its filters and its sort.
        filters (list[RecordsListPageFiltersItem] | Unset): Extra conditions ANDed with the View's
            own — "this View, further narrowed". Unlike `records.list`'s `filters`, these are EXACT:
            every page is precisely what the client's own matcher would keep, so a page is never
            missing records it should hold.
        date_range (RecordsListPageDateRange | Unset): Scope the page to a
            `date`/`created_time`/`updated_time` field falling in `[gte, lt)` — a half-open range of
            absolute UTC instants, not a `filters` condition. Resolve the bounds yourself: a day or a
            month only means something in a timezone, and the server does not know the viewer's.
        sort (RecordsListPageSort | Unset): Sort by one field. Only number and date fields sort
            authoritatively (their typed value column matches a client's own ordering); any other
            field type is returned in the default order and left for the caller to sort. Replaces the
            saved View's sort when `viewId` is also given (the View's filters still apply). Empty
            values sort last; ties are broken by record id, so pages never overlap.
        page (int | Unset): 1-indexed, not 0-indexed. Default: 1.
        page_size (int | Unset): Records per page. Capped at 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordsListPageResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            base_id=base_id,
            view_id=view_id,
            filters=filters,
            date_range=date_range,
            sort=sort,
            page=page,
            page_size=page_size,
        )
    ).parsed
