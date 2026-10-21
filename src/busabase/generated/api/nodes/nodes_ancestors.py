from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nodes_ancestors_response_200 import NodesAncestorsResponse200
from ...models.nodes_ancestors_type import NodesAncestorsType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    type_: NodesAncestorsType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/nodes/{node_id}/ancestors".format(
            node_id=quote(str(node_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NodesAncestorsResponse200 | None:
    if response.status_code == 200:
        response_200 = NodesAncestorsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[NodesAncestorsResponse200]:
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
    type_: NodesAncestorsType | Unset = UNSET,
) -> Response[NodesAncestorsResponse200]:
    """List a node's ancestor ids

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesAncestorsType | Unset): Optional disambiguation hint, only needed when
            `nodeId` is a slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NodesAncestorsResponse200]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: NodesAncestorsType | Unset = UNSET,
) -> NodesAncestorsResponse200 | None:
    """List a node's ancestor ids

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesAncestorsType | Unset): Optional disambiguation hint, only needed when
            `nodeId` is a slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NodesAncestorsResponse200
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: NodesAncestorsType | Unset = UNSET,
) -> Response[NodesAncestorsResponse200]:
    """List a node's ancestor ids

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesAncestorsType | Unset): Optional disambiguation hint, only needed when
            `nodeId` is a slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NodesAncestorsResponse200]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: NodesAncestorsType | Unset = UNSET,
) -> NodesAncestorsResponse200 | None:
    """List a node's ancestor ids

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesAncestorsType | Unset): Optional disambiguation hint, only needed when
            `nodeId` is a slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NodesAncestorsResponse200
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            type_=type_,
        )
    ).parsed
