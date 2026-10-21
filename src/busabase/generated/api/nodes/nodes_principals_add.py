from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nodes_principals_add_body import NodesPrincipalsAddBody
from ...models.nodes_principals_add_response_200 import NodesPrincipalsAddResponse200
from ...types import Response


def _get_kwargs(
    node_id: str,
    *,
    body: NodesPrincipalsAddBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/nodes/{node_id}/principals".format(
            node_id=quote(str(node_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NodesPrincipalsAddResponse200 | None:
    if response.status_code == 200:
        response_200 = NodesPrincipalsAddResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[NodesPrincipalsAddResponse200]:
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
    body: NodesPrincipalsAddBody,
) -> Response[NodesPrincipalsAddResponse200]:
    """Grant (or update) a principal's access level on a node

    Args:
        node_id (str):
        body (NodesPrincipalsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NodesPrincipalsAddResponse200]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NodesPrincipalsAddBody,
) -> NodesPrincipalsAddResponse200 | None:
    """Grant (or update) a principal's access level on a node

    Args:
        node_id (str):
        body (NodesPrincipalsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NodesPrincipalsAddResponse200
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NodesPrincipalsAddBody,
) -> Response[NodesPrincipalsAddResponse200]:
    """Grant (or update) a principal's access level on a node

    Args:
        node_id (str):
        body (NodesPrincipalsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NodesPrincipalsAddResponse200]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NodesPrincipalsAddBody,
) -> NodesPrincipalsAddResponse200 | None:
    """Grant (or update) a principal's access level on a node

    Args:
        node_id (str):
        body (NodesPrincipalsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NodesPrincipalsAddResponse200
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            body=body,
        )
    ).parsed
