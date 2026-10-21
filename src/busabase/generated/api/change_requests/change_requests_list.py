from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_requests_list_response_200 import ChangeRequestsListResponse200
from ...models.change_requests_list_status_item import (
    ChangeRequestsListStatusItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: list[ChangeRequestsListStatusItem] | Unset = UNSET,
    mine: bool | Unset = UNSET,
    affects_node_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item: str = status_item_data
            json_status.append(status_item)

    params["status"] = json_status

    params["mine"] = mine

    params["affectsNodeId"] = affects_node_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/change-requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChangeRequestsListResponse200 | None:
    if response.status_code == 200:
        response_200 = ChangeRequestsListResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ChangeRequestsListResponse200]:
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
    cursor: str | Unset = UNSET,
    status: list[ChangeRequestsListStatusItem] | Unset = UNSET,
    mine: bool | Unset = UNSET,
    affects_node_id: str | Unset = UNSET,
) -> Response[ChangeRequestsListResponse200]:
    """List change requests

    Args:
        limit (int | Unset): Change requests per page. Capped at 100; ask for the next page with
            `cursor`. Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.
        status (list[ChangeRequestsListStatusItem] | Unset): Keep only these statuses. Omitting it
            returns every status, not just open ones.
        mine (bool | Unset): Only change requests CREATED by the acting user — not ones awaiting
            their review.
        affects_node_id (str | Unset): Only change requests whose target, or any of their
            operations, touches this node — including Base-backed nodes. To ask whether a resource
            already has an unfinished change request, pass this with `limit: 1` rather than paging the
            space: an empty result is conclusive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeRequestsListResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        status=status,
        mine=mine,
        affects_node_id=affects_node_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: list[ChangeRequestsListStatusItem] | Unset = UNSET,
    mine: bool | Unset = UNSET,
    affects_node_id: str | Unset = UNSET,
) -> ChangeRequestsListResponse200 | None:
    """List change requests

    Args:
        limit (int | Unset): Change requests per page. Capped at 100; ask for the next page with
            `cursor`. Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.
        status (list[ChangeRequestsListStatusItem] | Unset): Keep only these statuses. Omitting it
            returns every status, not just open ones.
        mine (bool | Unset): Only change requests CREATED by the acting user — not ones awaiting
            their review.
        affects_node_id (str | Unset): Only change requests whose target, or any of their
            operations, touches this node — including Base-backed nodes. To ask whether a resource
            already has an unfinished change request, pass this with `limit: 1` rather than paging the
            space: an empty result is conclusive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeRequestsListResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        status=status,
        mine=mine,
        affects_node_id=affects_node_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: list[ChangeRequestsListStatusItem] | Unset = UNSET,
    mine: bool | Unset = UNSET,
    affects_node_id: str | Unset = UNSET,
) -> Response[ChangeRequestsListResponse200]:
    """List change requests

    Args:
        limit (int | Unset): Change requests per page. Capped at 100; ask for the next page with
            `cursor`. Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.
        status (list[ChangeRequestsListStatusItem] | Unset): Keep only these statuses. Omitting it
            returns every status, not just open ones.
        mine (bool | Unset): Only change requests CREATED by the acting user — not ones awaiting
            their review.
        affects_node_id (str | Unset): Only change requests whose target, or any of their
            operations, touches this node — including Base-backed nodes. To ask whether a resource
            already has an unfinished change request, pass this with `limit: 1` rather than paging the
            space: an empty result is conclusive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeRequestsListResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        status=status,
        mine=mine,
        affects_node_id=affects_node_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    status: list[ChangeRequestsListStatusItem] | Unset = UNSET,
    mine: bool | Unset = UNSET,
    affects_node_id: str | Unset = UNSET,
) -> ChangeRequestsListResponse200 | None:
    """List change requests

    Args:
        limit (int | Unset): Change requests per page. Capped at 100; ask for the next page with
            `cursor`. Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.
        status (list[ChangeRequestsListStatusItem] | Unset): Keep only these statuses. Omitting it
            returns every status, not just open ones.
        mine (bool | Unset): Only change requests CREATED by the acting user — not ones awaiting
            their review.
        affects_node_id (str | Unset): Only change requests whose target, or any of their
            operations, touches this node — including Base-backed nodes. To ask whether a resource
            already has an unfinished change request, pass this with `limit: 1` rather than paging the
            space: an empty result is conclusive.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeRequestsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            status=status,
            mine=mine,
            affects_node_id=affects_node_id,
        )
    ).parsed
