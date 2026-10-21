from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nodes_principals_list_response_200_item import NodesPrincipalsListResponse200Item
from ...types import Response


def _get_kwargs(
    node_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/nodes/{node_id}/principals".format(
            node_id=quote(str(node_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[NodesPrincipalsListResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = NodesPrincipalsListResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[NodesPrincipalsListResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[NodesPrincipalsListResponse200Item]]:
    """List a node's direct access grants

    Args:
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[NodesPrincipalsListResponse200Item]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[NodesPrincipalsListResponse200Item] | None:
    """List a node's direct access grants

    Args:
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[NodesPrincipalsListResponse200Item]
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[NodesPrincipalsListResponse200Item]]:
    """List a node's direct access grants

    Args:
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[NodesPrincipalsListResponse200Item]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[NodesPrincipalsListResponse200Item] | None:
    """List a node's direct access grants

    Args:
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[NodesPrincipalsListResponse200Item]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
        )
    ).parsed
