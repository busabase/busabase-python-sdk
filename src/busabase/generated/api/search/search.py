import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_mode import SearchMode
from ...models.search_response_200 import SearchResponse200
from ...models.search_sort import SearchSort
from ...models.search_sources_type_0_item import SearchSourcesType0Item
from ...models.search_sources_type_1 import SearchSourcesType1
from ...models.search_surface import SearchSurface
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str | Unset = "",
    mode: SearchMode | Unset = "full",
    surface: SearchSurface | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sources: list[SearchSourcesType0Item] | SearchSourcesType1 | Unset = UNSET,
    sort: SearchSort | Unset = "relevance",
    updated_after: datetime.datetime | Unset = UNSET,
    updated_before: datetime.datetime | Unset = UNSET,
    created_by: str | Unset = UNSET,
    in_node_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    json_mode: str | Unset = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode

    params["mode"] = json_mode

    json_surface: str | Unset = UNSET
    if not isinstance(surface, Unset):
        json_surface = surface

    params["surface"] = json_surface

    params["limit"] = limit

    params["offset"] = offset

    json_sources: list[str] | str | Unset
    if isinstance(sources, Unset):
        json_sources = UNSET
    elif isinstance(sources, list):
        json_sources = []
        for sources_type_0_item_data in sources:
            sources_type_0_item: str = sources_type_0_item_data
            json_sources.append(sources_type_0_item)

    else:
        json_sources = sources

    params["sources"] = json_sources

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_updated_after: str | Unset = UNSET
    if not isinstance(updated_after, Unset):
        json_updated_after = updated_after.isoformat()
    params["updatedAfter"] = json_updated_after

    json_updated_before: str | Unset = UNSET
    if not isinstance(updated_before, Unset):
        json_updated_before = updated_before.isoformat()
    params["updatedBefore"] = json_updated_before

    params["createdBy"] = created_by

    params["inNodeId"] = in_node_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/search",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchResponse200 | None:
    if response.status_code == 200:
        response_200 = SearchResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = "",
    mode: SearchMode | Unset = "full",
    surface: SearchSurface | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sources: list[SearchSourcesType0Item] | SearchSourcesType1 | Unset = UNSET,
    sort: SearchSort | Unset = "relevance",
    updated_after: datetime.datetime | Unset = UNSET,
    updated_before: datetime.datetime | Unset = UNSET,
    created_by: str | Unset = UNSET,
    in_node_id: str | Unset = UNSET,
) -> Response[SearchResponse200]:
    """Search Busabase

    Args:
        query (str | Unset): Full-text query. An empty string matches nothing. Default: ''.
        mode (SearchMode | Unset): Search depth. `quick` skips live file-body scans for typeahead;
            `full` preserves complete search behavior. Default: 'full'.
        surface (SearchSurface | Unset): Optional first-party UI surface for aggregate quality
            metrics. API/CLI callers should omit it.
        limit (int | Unset): Results per page. Capped at 100; note the default is 20, not 50.
            Default: 20.
        offset (int | Unset): 0-indexed skip count. This endpoint pages by offset, not by cursor.
            Default: 0.
        sources (list[SearchSourcesType0Item] | SearchSourcesType1 | Unset): Restrict which
            content is searched. Omitting it searches ALL sources. Repeat the parameter to pass
            several (`?sources=records&sources=files`); a single occurrence is accepted as a bare
            value.
        sort (SearchSort | Unset): Result order. `relevance` (default) keeps each source's own
            ranking — for records that is the full-text rank, for everything else most-recently-
            updated first. The four explicit orders sort every source by the same column so a mixed
            result set is comparable. Default: 'relevance'.
        updated_after (datetime.datetime | Unset): Inclusive lower bound, ISO 8601. A UTC `Z` or
            an explicit offset; not a bare local time.
        updated_before (datetime.datetime | Unset): Inclusive upper bound, ISO 8601. A UTC `Z` or
            an explicit offset; not a bare local time.
        created_by (str | Unset): Restrict to one creator. Matches the actor id, which may be an
            agent or API key.
        in_node_id (str | Unset): Limit to this node and its descendants.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse200]
    """

    kwargs = _get_kwargs(
        query=query,
        mode=mode,
        surface=surface,
        limit=limit,
        offset=offset,
        sources=sources,
        sort=sort,
        updated_after=updated_after,
        updated_before=updated_before,
        created_by=created_by,
        in_node_id=in_node_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = "",
    mode: SearchMode | Unset = "full",
    surface: SearchSurface | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sources: list[SearchSourcesType0Item] | SearchSourcesType1 | Unset = UNSET,
    sort: SearchSort | Unset = "relevance",
    updated_after: datetime.datetime | Unset = UNSET,
    updated_before: datetime.datetime | Unset = UNSET,
    created_by: str | Unset = UNSET,
    in_node_id: str | Unset = UNSET,
) -> SearchResponse200 | None:
    """Search Busabase

    Args:
        query (str | Unset): Full-text query. An empty string matches nothing. Default: ''.
        mode (SearchMode | Unset): Search depth. `quick` skips live file-body scans for typeahead;
            `full` preserves complete search behavior. Default: 'full'.
        surface (SearchSurface | Unset): Optional first-party UI surface for aggregate quality
            metrics. API/CLI callers should omit it.
        limit (int | Unset): Results per page. Capped at 100; note the default is 20, not 50.
            Default: 20.
        offset (int | Unset): 0-indexed skip count. This endpoint pages by offset, not by cursor.
            Default: 0.
        sources (list[SearchSourcesType0Item] | SearchSourcesType1 | Unset): Restrict which
            content is searched. Omitting it searches ALL sources. Repeat the parameter to pass
            several (`?sources=records&sources=files`); a single occurrence is accepted as a bare
            value.
        sort (SearchSort | Unset): Result order. `relevance` (default) keeps each source's own
            ranking — for records that is the full-text rank, for everything else most-recently-
            updated first. The four explicit orders sort every source by the same column so a mixed
            result set is comparable. Default: 'relevance'.
        updated_after (datetime.datetime | Unset): Inclusive lower bound, ISO 8601. A UTC `Z` or
            an explicit offset; not a bare local time.
        updated_before (datetime.datetime | Unset): Inclusive upper bound, ISO 8601. A UTC `Z` or
            an explicit offset; not a bare local time.
        created_by (str | Unset): Restrict to one creator. Matches the actor id, which may be an
            agent or API key.
        in_node_id (str | Unset): Limit to this node and its descendants.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponse200
    """

    return sync_detailed(
        client=client,
        query=query,
        mode=mode,
        surface=surface,
        limit=limit,
        offset=offset,
        sources=sources,
        sort=sort,
        updated_after=updated_after,
        updated_before=updated_before,
        created_by=created_by,
        in_node_id=in_node_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = "",
    mode: SearchMode | Unset = "full",
    surface: SearchSurface | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sources: list[SearchSourcesType0Item] | SearchSourcesType1 | Unset = UNSET,
    sort: SearchSort | Unset = "relevance",
    updated_after: datetime.datetime | Unset = UNSET,
    updated_before: datetime.datetime | Unset = UNSET,
    created_by: str | Unset = UNSET,
    in_node_id: str | Unset = UNSET,
) -> Response[SearchResponse200]:
    """Search Busabase

    Args:
        query (str | Unset): Full-text query. An empty string matches nothing. Default: ''.
        mode (SearchMode | Unset): Search depth. `quick` skips live file-body scans for typeahead;
            `full` preserves complete search behavior. Default: 'full'.
        surface (SearchSurface | Unset): Optional first-party UI surface for aggregate quality
            metrics. API/CLI callers should omit it.
        limit (int | Unset): Results per page. Capped at 100; note the default is 20, not 50.
            Default: 20.
        offset (int | Unset): 0-indexed skip count. This endpoint pages by offset, not by cursor.
            Default: 0.
        sources (list[SearchSourcesType0Item] | SearchSourcesType1 | Unset): Restrict which
            content is searched. Omitting it searches ALL sources. Repeat the parameter to pass
            several (`?sources=records&sources=files`); a single occurrence is accepted as a bare
            value.
        sort (SearchSort | Unset): Result order. `relevance` (default) keeps each source's own
            ranking — for records that is the full-text rank, for everything else most-recently-
            updated first. The four explicit orders sort every source by the same column so a mixed
            result set is comparable. Default: 'relevance'.
        updated_after (datetime.datetime | Unset): Inclusive lower bound, ISO 8601. A UTC `Z` or
            an explicit offset; not a bare local time.
        updated_before (datetime.datetime | Unset): Inclusive upper bound, ISO 8601. A UTC `Z` or
            an explicit offset; not a bare local time.
        created_by (str | Unset): Restrict to one creator. Matches the actor id, which may be an
            agent or API key.
        in_node_id (str | Unset): Limit to this node and its descendants.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse200]
    """

    kwargs = _get_kwargs(
        query=query,
        mode=mode,
        surface=surface,
        limit=limit,
        offset=offset,
        sources=sources,
        sort=sort,
        updated_after=updated_after,
        updated_before=updated_before,
        created_by=created_by,
        in_node_id=in_node_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = "",
    mode: SearchMode | Unset = "full",
    surface: SearchSurface | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sources: list[SearchSourcesType0Item] | SearchSourcesType1 | Unset = UNSET,
    sort: SearchSort | Unset = "relevance",
    updated_after: datetime.datetime | Unset = UNSET,
    updated_before: datetime.datetime | Unset = UNSET,
    created_by: str | Unset = UNSET,
    in_node_id: str | Unset = UNSET,
) -> SearchResponse200 | None:
    """Search Busabase

    Args:
        query (str | Unset): Full-text query. An empty string matches nothing. Default: ''.
        mode (SearchMode | Unset): Search depth. `quick` skips live file-body scans for typeahead;
            `full` preserves complete search behavior. Default: 'full'.
        surface (SearchSurface | Unset): Optional first-party UI surface for aggregate quality
            metrics. API/CLI callers should omit it.
        limit (int | Unset): Results per page. Capped at 100; note the default is 20, not 50.
            Default: 20.
        offset (int | Unset): 0-indexed skip count. This endpoint pages by offset, not by cursor.
            Default: 0.
        sources (list[SearchSourcesType0Item] | SearchSourcesType1 | Unset): Restrict which
            content is searched. Omitting it searches ALL sources. Repeat the parameter to pass
            several (`?sources=records&sources=files`); a single occurrence is accepted as a bare
            value.
        sort (SearchSort | Unset): Result order. `relevance` (default) keeps each source's own
            ranking — for records that is the full-text rank, for everything else most-recently-
            updated first. The four explicit orders sort every source by the same column so a mixed
            result set is comparable. Default: 'relevance'.
        updated_after (datetime.datetime | Unset): Inclusive lower bound, ISO 8601. A UTC `Z` or
            an explicit offset; not a bare local time.
        updated_before (datetime.datetime | Unset): Inclusive upper bound, ISO 8601. A UTC `Z` or
            an explicit offset; not a bare local time.
        created_by (str | Unset): Restrict to one creator. Matches the actor id, which may be an
            agent or API key.
        in_node_id (str | Unset): Limit to this node and its descendants.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            mode=mode,
            surface=surface,
            limit=limit,
            offset=offset,
            sources=sources,
            sort=sort,
            updated_after=updated_after,
            updated_before=updated_before,
            created_by=created_by,
            in_node_id=in_node_id,
        )
    ).parsed
