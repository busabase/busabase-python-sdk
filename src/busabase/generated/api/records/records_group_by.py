from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.records_group_by_aggregates_item import RecordsGroupByAggregatesItem
from ...models.records_group_by_bucketing import RecordsGroupByBucketing
from ...models.records_group_by_filters_item import RecordsGroupByFiltersItem
from ...models.records_group_by_response_200 import RecordsGroupByResponse200
from ...models.records_group_by_value_filters_item_type_0 import RecordsGroupByValueFiltersItemType0
from ...models.records_group_by_value_filters_item_type_1 import RecordsGroupByValueFiltersItemType1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    base_id: str,
    field_slug: str | Unset = UNSET,
    bucketing: RecordsGroupByBucketing | Unset = "grid",
    aggregates: list[RecordsGroupByAggregatesItem] | Unset = UNSET,
    view_id: str | Unset = UNSET,
    filters: list[RecordsGroupByFiltersItem] | Unset = UNSET,
    value_filters: list[RecordsGroupByValueFiltersItemType0 | RecordsGroupByValueFiltersItemType1] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["baseId"] = base_id

    params["fieldSlug"] = field_slug

    json_bucketing: str | Unset = UNSET
    if not isinstance(bucketing, Unset):
        json_bucketing = bucketing

    params["bucketing"] = json_bucketing

    json_aggregates: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(aggregates, Unset):
        json_aggregates = []
        for aggregates_item_data in aggregates:
            aggregates_item = aggregates_item_data.to_dict()
            json_aggregates.append(aggregates_item)

    params["aggregates"] = json_aggregates

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
            if isinstance(value_filters_item_data, RecordsGroupByValueFiltersItemType0):
                value_filters_item = value_filters_item_data.to_dict()
            else:
                value_filters_item = value_filters_item_data.to_dict()

            json_value_filters.append(value_filters_item)

    params["valueFilters"] = json_value_filters

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/records/group-by",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | RecordsGroupByResponse200 | None:
    if response.status_code == 200:
        response_200 = RecordsGroupByResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | RecordsGroupByResponse200]:
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
    field_slug: str | Unset = UNSET,
    bucketing: RecordsGroupByBucketing | Unset = "grid",
    aggregates: list[RecordsGroupByAggregatesItem] | Unset = UNSET,
    view_id: str | Unset = UNSET,
    filters: list[RecordsGroupByFiltersItem] | Unset = UNSET,
    value_filters: list[RecordsGroupByValueFiltersItemType0 | RecordsGroupByValueFiltersItemType1] | Unset = UNSET,
) -> Response[Error | RecordsGroupByResponse200]:
    """Count records per group

     One SQL GROUP BY returning every bucket's exact count — the split a board column header or a summary
    tile needs, without reading the records themselves. `fieldSlug` must name a `select` or `checkbox`
    field: their stored value IS the grouping key, so the buckets are exactly the ones a client would
    build. Grouping by a text, number or date field is rejected rather than approximated (text keys are
    truncated at the projection limit; date keys would bucket by the server's timezone, not the
    viewer's). `viewId` and `filters` narrow the set first, with the same exactness rules as
    `records.count`: provably-exact conditions stay a cheap SQL aggregate, anything else falls back to
    evaluating every matching row server-side — exact, but not free on a large Base. Groups come back
    keyed by raw choice id (or `"true"`/`"false"`), with `null` for records that have no value; labels
    are the client's to render.

    Args:
        base_id (str): Required: a field slug is only unambiguous within one Base.
        field_slug (str | Unset): The field to group by. OMIT it to aggregate the whole filtered
            set as a single bucket, which is what a summary tile wants. Under the default `grid`
            bucketing only `select` and `checkbox` can be grouped; `sql` bucketing also allows number
            and date fields.
        bucketing (RecordsGroupByBucketing | Unset): How records are bucketed, and the two modes
            disagree on real data. `grid` (default) buckets the way the grid renders: an unset
            checkbox counts as `false` and an empty string falls in the null bucket — right for a
            Kanban column header. `sql` buckets the way GROUP BY does: a missing value gets its OWN
            bucket and nothing is folded — right for anything reproducing SQL. `sql` also returns keys
            in their own type (a number for a number field) rather than as strings. Default: 'grid'.
        aggregates (list[RecordsGroupByAggregatesItem] | Unset): Numeric aggregates evaluated per
            group, keyed in the response as `"<fn>:<fieldSlug>"`. Only number-shaped fields can be
            aggregated; anything else is a 400. `sum`/`avg`/`min`/`max` of a group holding no values
            are NULL rather than 0, and `count` over a FIELD counts present values — which is not the
            same as the group's own `count`, which counts records.
        view_id (str | Unset): Group only what this saved View would display. Its filters apply;
            its sort is ignored.
        filters (list[RecordsGroupByFiltersItem] | Unset): Ad-hoc conditions, ANDed with the
            View's own when both are given. The grouping is exact either way, but a condition whose
            exactness cannot be proven makes the server read every candidate row instead of running
            one GROUP BY.
        value_filters (list[RecordsGroupByValueFiltersItemType0 |
            RecordsGroupByValueFiltersItemType1] | Unset): EXACT value comparisons, same shape as
            `records.list`'s. Always exact, so a grouping scoped only by these stays a single SQL
            GROUP BY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RecordsGroupByResponse200]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        field_slug=field_slug,
        bucketing=bucketing,
        aggregates=aggregates,
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
    base_id: str,
    field_slug: str | Unset = UNSET,
    bucketing: RecordsGroupByBucketing | Unset = "grid",
    aggregates: list[RecordsGroupByAggregatesItem] | Unset = UNSET,
    view_id: str | Unset = UNSET,
    filters: list[RecordsGroupByFiltersItem] | Unset = UNSET,
    value_filters: list[RecordsGroupByValueFiltersItemType0 | RecordsGroupByValueFiltersItemType1] | Unset = UNSET,
) -> Error | RecordsGroupByResponse200 | None:
    """Count records per group

     One SQL GROUP BY returning every bucket's exact count — the split a board column header or a summary
    tile needs, without reading the records themselves. `fieldSlug` must name a `select` or `checkbox`
    field: their stored value IS the grouping key, so the buckets are exactly the ones a client would
    build. Grouping by a text, number or date field is rejected rather than approximated (text keys are
    truncated at the projection limit; date keys would bucket by the server's timezone, not the
    viewer's). `viewId` and `filters` narrow the set first, with the same exactness rules as
    `records.count`: provably-exact conditions stay a cheap SQL aggregate, anything else falls back to
    evaluating every matching row server-side — exact, but not free on a large Base. Groups come back
    keyed by raw choice id (or `"true"`/`"false"`), with `null` for records that have no value; labels
    are the client's to render.

    Args:
        base_id (str): Required: a field slug is only unambiguous within one Base.
        field_slug (str | Unset): The field to group by. OMIT it to aggregate the whole filtered
            set as a single bucket, which is what a summary tile wants. Under the default `grid`
            bucketing only `select` and `checkbox` can be grouped; `sql` bucketing also allows number
            and date fields.
        bucketing (RecordsGroupByBucketing | Unset): How records are bucketed, and the two modes
            disagree on real data. `grid` (default) buckets the way the grid renders: an unset
            checkbox counts as `false` and an empty string falls in the null bucket — right for a
            Kanban column header. `sql` buckets the way GROUP BY does: a missing value gets its OWN
            bucket and nothing is folded — right for anything reproducing SQL. `sql` also returns keys
            in their own type (a number for a number field) rather than as strings. Default: 'grid'.
        aggregates (list[RecordsGroupByAggregatesItem] | Unset): Numeric aggregates evaluated per
            group, keyed in the response as `"<fn>:<fieldSlug>"`. Only number-shaped fields can be
            aggregated; anything else is a 400. `sum`/`avg`/`min`/`max` of a group holding no values
            are NULL rather than 0, and `count` over a FIELD counts present values — which is not the
            same as the group's own `count`, which counts records.
        view_id (str | Unset): Group only what this saved View would display. Its filters apply;
            its sort is ignored.
        filters (list[RecordsGroupByFiltersItem] | Unset): Ad-hoc conditions, ANDed with the
            View's own when both are given. The grouping is exact either way, but a condition whose
            exactness cannot be proven makes the server read every candidate row instead of running
            one GROUP BY.
        value_filters (list[RecordsGroupByValueFiltersItemType0 |
            RecordsGroupByValueFiltersItemType1] | Unset): EXACT value comparisons, same shape as
            `records.list`'s. Always exact, so a grouping scoped only by these stays a single SQL
            GROUP BY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RecordsGroupByResponse200
    """

    return sync_detailed(
        client=client,
        base_id=base_id,
        field_slug=field_slug,
        bucketing=bucketing,
        aggregates=aggregates,
        view_id=view_id,
        filters=filters,
        value_filters=value_filters,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    base_id: str,
    field_slug: str | Unset = UNSET,
    bucketing: RecordsGroupByBucketing | Unset = "grid",
    aggregates: list[RecordsGroupByAggregatesItem] | Unset = UNSET,
    view_id: str | Unset = UNSET,
    filters: list[RecordsGroupByFiltersItem] | Unset = UNSET,
    value_filters: list[RecordsGroupByValueFiltersItemType0 | RecordsGroupByValueFiltersItemType1] | Unset = UNSET,
) -> Response[Error | RecordsGroupByResponse200]:
    """Count records per group

     One SQL GROUP BY returning every bucket's exact count — the split a board column header or a summary
    tile needs, without reading the records themselves. `fieldSlug` must name a `select` or `checkbox`
    field: their stored value IS the grouping key, so the buckets are exactly the ones a client would
    build. Grouping by a text, number or date field is rejected rather than approximated (text keys are
    truncated at the projection limit; date keys would bucket by the server's timezone, not the
    viewer's). `viewId` and `filters` narrow the set first, with the same exactness rules as
    `records.count`: provably-exact conditions stay a cheap SQL aggregate, anything else falls back to
    evaluating every matching row server-side — exact, but not free on a large Base. Groups come back
    keyed by raw choice id (or `"true"`/`"false"`), with `null` for records that have no value; labels
    are the client's to render.

    Args:
        base_id (str): Required: a field slug is only unambiguous within one Base.
        field_slug (str | Unset): The field to group by. OMIT it to aggregate the whole filtered
            set as a single bucket, which is what a summary tile wants. Under the default `grid`
            bucketing only `select` and `checkbox` can be grouped; `sql` bucketing also allows number
            and date fields.
        bucketing (RecordsGroupByBucketing | Unset): How records are bucketed, and the two modes
            disagree on real data. `grid` (default) buckets the way the grid renders: an unset
            checkbox counts as `false` and an empty string falls in the null bucket — right for a
            Kanban column header. `sql` buckets the way GROUP BY does: a missing value gets its OWN
            bucket and nothing is folded — right for anything reproducing SQL. `sql` also returns keys
            in their own type (a number for a number field) rather than as strings. Default: 'grid'.
        aggregates (list[RecordsGroupByAggregatesItem] | Unset): Numeric aggregates evaluated per
            group, keyed in the response as `"<fn>:<fieldSlug>"`. Only number-shaped fields can be
            aggregated; anything else is a 400. `sum`/`avg`/`min`/`max` of a group holding no values
            are NULL rather than 0, and `count` over a FIELD counts present values — which is not the
            same as the group's own `count`, which counts records.
        view_id (str | Unset): Group only what this saved View would display. Its filters apply;
            its sort is ignored.
        filters (list[RecordsGroupByFiltersItem] | Unset): Ad-hoc conditions, ANDed with the
            View's own when both are given. The grouping is exact either way, but a condition whose
            exactness cannot be proven makes the server read every candidate row instead of running
            one GROUP BY.
        value_filters (list[RecordsGroupByValueFiltersItemType0 |
            RecordsGroupByValueFiltersItemType1] | Unset): EXACT value comparisons, same shape as
            `records.list`'s. Always exact, so a grouping scoped only by these stays a single SQL
            GROUP BY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RecordsGroupByResponse200]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        field_slug=field_slug,
        bucketing=bucketing,
        aggregates=aggregates,
        view_id=view_id,
        filters=filters,
        value_filters=value_filters,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    base_id: str,
    field_slug: str | Unset = UNSET,
    bucketing: RecordsGroupByBucketing | Unset = "grid",
    aggregates: list[RecordsGroupByAggregatesItem] | Unset = UNSET,
    view_id: str | Unset = UNSET,
    filters: list[RecordsGroupByFiltersItem] | Unset = UNSET,
    value_filters: list[RecordsGroupByValueFiltersItemType0 | RecordsGroupByValueFiltersItemType1] | Unset = UNSET,
) -> Error | RecordsGroupByResponse200 | None:
    """Count records per group

     One SQL GROUP BY returning every bucket's exact count — the split a board column header or a summary
    tile needs, without reading the records themselves. `fieldSlug` must name a `select` or `checkbox`
    field: their stored value IS the grouping key, so the buckets are exactly the ones a client would
    build. Grouping by a text, number or date field is rejected rather than approximated (text keys are
    truncated at the projection limit; date keys would bucket by the server's timezone, not the
    viewer's). `viewId` and `filters` narrow the set first, with the same exactness rules as
    `records.count`: provably-exact conditions stay a cheap SQL aggregate, anything else falls back to
    evaluating every matching row server-side — exact, but not free on a large Base. Groups come back
    keyed by raw choice id (or `"true"`/`"false"`), with `null` for records that have no value; labels
    are the client's to render.

    Args:
        base_id (str): Required: a field slug is only unambiguous within one Base.
        field_slug (str | Unset): The field to group by. OMIT it to aggregate the whole filtered
            set as a single bucket, which is what a summary tile wants. Under the default `grid`
            bucketing only `select` and `checkbox` can be grouped; `sql` bucketing also allows number
            and date fields.
        bucketing (RecordsGroupByBucketing | Unset): How records are bucketed, and the two modes
            disagree on real data. `grid` (default) buckets the way the grid renders: an unset
            checkbox counts as `false` and an empty string falls in the null bucket — right for a
            Kanban column header. `sql` buckets the way GROUP BY does: a missing value gets its OWN
            bucket and nothing is folded — right for anything reproducing SQL. `sql` also returns keys
            in their own type (a number for a number field) rather than as strings. Default: 'grid'.
        aggregates (list[RecordsGroupByAggregatesItem] | Unset): Numeric aggregates evaluated per
            group, keyed in the response as `"<fn>:<fieldSlug>"`. Only number-shaped fields can be
            aggregated; anything else is a 400. `sum`/`avg`/`min`/`max` of a group holding no values
            are NULL rather than 0, and `count` over a FIELD counts present values — which is not the
            same as the group's own `count`, which counts records.
        view_id (str | Unset): Group only what this saved View would display. Its filters apply;
            its sort is ignored.
        filters (list[RecordsGroupByFiltersItem] | Unset): Ad-hoc conditions, ANDed with the
            View's own when both are given. The grouping is exact either way, but a condition whose
            exactness cannot be proven makes the server read every candidate row instead of running
            one GROUP BY.
        value_filters (list[RecordsGroupByValueFiltersItemType0 |
            RecordsGroupByValueFiltersItemType1] | Unset): EXACT value comparisons, same shape as
            `records.list`'s. Always exact, so a grouping scoped only by these stays a single SQL
            GROUP BY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RecordsGroupByResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            base_id=base_id,
            field_slug=field_slug,
            bucketing=bucketing,
            aggregates=aggregates,
            view_id=view_id,
            filters=filters,
            value_filters=value_filters,
        )
    ).parsed
