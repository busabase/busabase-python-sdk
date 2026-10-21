from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nodes_is_descendant_response_200 import NodesIsDescendantResponse200
from ...types import UNSET, Response


def _get_kwargs(
    node_id: str,
    *,
    potential_ancestor_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["potentialAncestorId"] = potential_ancestor_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/nodes/{node_id}/is-descendant".format(
            node_id=quote(str(node_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NodesIsDescendantResponse200 | None:
    if response.status_code == 200:
        response_200 = NodesIsDescendantResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[NodesIsDescendantResponse200]:
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
    potential_ancestor_id: str,
) -> Response[NodesIsDescendantResponse200]:
    """Check whether a node is a descendant of another

    Args:
        node_id (str): The node walked UPWARDS from — the possible descendant.
        potential_ancestor_id (str): The node looked for on the way up. Answers "is `nodeId`
            inside this one?", not the reverse — swapping the two silently returns the wrong answer
            rather than an error.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NodesIsDescendantResponse200]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        potential_ancestor_id=potential_ancestor_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    potential_ancestor_id: str,
) -> NodesIsDescendantResponse200 | None:
    """Check whether a node is a descendant of another

    Args:
        node_id (str): The node walked UPWARDS from — the possible descendant.
        potential_ancestor_id (str): The node looked for on the way up. Answers "is `nodeId`
            inside this one?", not the reverse — swapping the two silently returns the wrong answer
            rather than an error.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NodesIsDescendantResponse200
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        potential_ancestor_id=potential_ancestor_id,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    potential_ancestor_id: str,
) -> Response[NodesIsDescendantResponse200]:
    """Check whether a node is a descendant of another

    Args:
        node_id (str): The node walked UPWARDS from — the possible descendant.
        potential_ancestor_id (str): The node looked for on the way up. Answers "is `nodeId`
            inside this one?", not the reverse — swapping the two silently returns the wrong answer
            rather than an error.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NodesIsDescendantResponse200]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        potential_ancestor_id=potential_ancestor_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    potential_ancestor_id: str,
) -> NodesIsDescendantResponse200 | None:
    """Check whether a node is a descendant of another

    Args:
        node_id (str): The node walked UPWARDS from — the possible descendant.
        potential_ancestor_id (str): The node looked for on the way up. Answers "is `nodeId`
            inside this one?", not the reverse — swapping the two silently returns the wrong answer
            rather than an error.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NodesIsDescendantResponse200
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            potential_ancestor_id=potential_ancestor_id,
        )
    ).parsed
