from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_requests_list_page_response_200 import ChangeRequestsListPageResponse200
from ...models.change_requests_list_page_status_item import (
    ChangeRequestsListPageStatusItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    status: list[ChangeRequestsListPageStatusItem] | Unset = UNSET,
    mine: bool | Unset = UNSET,
    affects_node_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

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
        "url": "/api/v1/change-requests/page",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChangeRequestsListPageResponse200 | None:
    if response.status_code == 200:
        response_200 = ChangeRequestsListPageResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ChangeRequestsListPageResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    status: list[ChangeRequestsListPageStatusItem] | Unset = UNSET,
    mine: bool | Unset = UNSET,
    affects_node_id: str | Unset = UNSET,
) -> Response[ChangeRequestsListPageResponse200]:
    """List a numbered change request page

    Args:
        page (int | Unset): 1-indexed, not 0-indexed. Default: 1.
        page_size (int | Unset): Change requests per page. Capped at 100. Default: 50.
        status (list[ChangeRequestsListPageStatusItem] | Unset): Keep only these statuses.
            Omitting it returns every status, not just open ones.
        mine (bool | Unset): Only change requests CREATED by the acting user — not ones awaiting
            their review.
        affects_node_id (str | Unset): Only change requests whose target, or any of their
            operations, touches this node — including Base-backed nodes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeRequestsListPageResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
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
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    status: list[ChangeRequestsListPageStatusItem] | Unset = UNSET,
    mine: bool | Unset = UNSET,
    affects_node_id: str | Unset = UNSET,
) -> ChangeRequestsListPageResponse200 | None:
    """List a numbered change request page

    Args:
        page (int | Unset): 1-indexed, not 0-indexed. Default: 1.
        page_size (int | Unset): Change requests per page. Capped at 100. Default: 50.
        status (list[ChangeRequestsListPageStatusItem] | Unset): Keep only these statuses.
            Omitting it returns every status, not just open ones.
        mine (bool | Unset): Only change requests CREATED by the acting user — not ones awaiting
            their review.
        affects_node_id (str | Unset): Only change requests whose target, or any of their
            operations, touches this node — including Base-backed nodes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeRequestsListPageResponse200
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        status=status,
        mine=mine,
        affects_node_id=affects_node_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    status: list[ChangeRequestsListPageStatusItem] | Unset = UNSET,
    mine: bool | Unset = UNSET,
    affects_node_id: str | Unset = UNSET,
) -> Response[ChangeRequestsListPageResponse200]:
    """List a numbered change request page

    Args:
        page (int | Unset): 1-indexed, not 0-indexed. Default: 1.
        page_size (int | Unset): Change requests per page. Capped at 100. Default: 50.
        status (list[ChangeRequestsListPageStatusItem] | Unset): Keep only these statuses.
            Omitting it returns every status, not just open ones.
        mine (bool | Unset): Only change requests CREATED by the acting user — not ones awaiting
            their review.
        affects_node_id (str | Unset): Only change requests whose target, or any of their
            operations, touches this node — including Base-backed nodes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeRequestsListPageResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        status=status,
        mine=mine,
        affects_node_id=affects_node_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    status: list[ChangeRequestsListPageStatusItem] | Unset = UNSET,
    mine: bool | Unset = UNSET,
    affects_node_id: str | Unset = UNSET,
) -> ChangeRequestsListPageResponse200 | None:
    """List a numbered change request page

    Args:
        page (int | Unset): 1-indexed, not 0-indexed. Default: 1.
        page_size (int | Unset): Change requests per page. Capped at 100. Default: 50.
        status (list[ChangeRequestsListPageStatusItem] | Unset): Keep only these statuses.
            Omitting it returns every status, not just open ones.
        mine (bool | Unset): Only change requests CREATED by the acting user — not ones awaiting
            their review.
        affects_node_id (str | Unset): Only change requests whose target, or any of their
            operations, touches this node — including Base-backed nodes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeRequestsListPageResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            status=status,
            mine=mine,
            affects_node_id=affects_node_id,
        )
    ).parsed
