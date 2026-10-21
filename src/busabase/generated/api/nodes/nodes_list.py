from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.node import Node
from ...models.nodes_list_status import NodesListStatus
from ...models.nodes_list_types_type_0_item import NodesListTypesType0Item
from ...models.nodes_list_types_type_1 import NodesListTypesType1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    parent_id: None | str | Unset = UNSET,
    depth: int | Unset = UNSET,
    status: NodesListStatus | Unset = "active",
    types: list[NodesListTypesType0Item] | NodesListTypesType1 | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: None | str | Unset
    if isinstance(parent_id, Unset):
        json_parent_id = UNSET
    else:
        json_parent_id = parent_id
    params["parentId"] = json_parent_id

    params["depth"] = depth

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_types: list[str] | str | Unset
    if isinstance(types, Unset):
        json_types = UNSET
    elif isinstance(types, list):
        json_types = []
        for types_type_0_item_data in types:
            types_type_0_item: str = types_type_0_item_data
            json_types.append(types_type_0_item)

    else:
        json_types = types

    params["types"] = json_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/nodes",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Node] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Node.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Node]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: None | str | Unset = UNSET,
    depth: int | Unset = UNSET,
    status: NodesListStatus | Unset = "active",
    types: list[NodesListTypesType0Item] | NodesListTypesType1 | Unset = UNSET,
) -> Response[list[Node]]:
    """List nodes (workspace tree, or a flat summary list by type)

    Args:
        parent_id (None | str | Unset): Folder to start from: a node id or a folder slug. Omit or
            null to start from the space root. An unknown ref is a 404 and a node that is not a folder
            is a 400 — never an empty list. With `types`, scopes the flat list to this folder's
            subtree.
        depth (int | Unset): How many levels beneath the start point to eagerly include (default 2
            once either field is set). Capped at 5. With `types` and `parentId`, how many levels of
            the folder's subtree to search (default: all of it).
        status (NodesListStatus | Unset): `active` walks the live TREE. `archived` returns a FLAT
            list of soft-archived nodes (the Trash view) with no parent/depth walk — so the response
            shape you can rely on differs between the two, not just the rows. `parentId` with
            `archived` is a 400. Default: 'active'.
        types (list[NodesListTypesType0Item] | NodesListTypesType1 | Unset): Return a flat list of
            lightweight summaries for these node types instead of the tree — across the space, or
            within `parentId`'s subtree when given. Read one node's full detail with GET
            /nodes/{nodeId}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Node]]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        depth=depth,
        status=status,
        types=types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_id: None | str | Unset = UNSET,
    depth: int | Unset = UNSET,
    status: NodesListStatus | Unset = "active",
    types: list[NodesListTypesType0Item] | NodesListTypesType1 | Unset = UNSET,
) -> list[Node] | None:
    """List nodes (workspace tree, or a flat summary list by type)

    Args:
        parent_id (None | str | Unset): Folder to start from: a node id or a folder slug. Omit or
            null to start from the space root. An unknown ref is a 404 and a node that is not a folder
            is a 400 — never an empty list. With `types`, scopes the flat list to this folder's
            subtree.
        depth (int | Unset): How many levels beneath the start point to eagerly include (default 2
            once either field is set). Capped at 5. With `types` and `parentId`, how many levels of
            the folder's subtree to search (default: all of it).
        status (NodesListStatus | Unset): `active` walks the live TREE. `archived` returns a FLAT
            list of soft-archived nodes (the Trash view) with no parent/depth walk — so the response
            shape you can rely on differs between the two, not just the rows. `parentId` with
            `archived` is a 400. Default: 'active'.
        types (list[NodesListTypesType0Item] | NodesListTypesType1 | Unset): Return a flat list of
            lightweight summaries for these node types instead of the tree — across the space, or
            within `parentId`'s subtree when given. Read one node's full detail with GET
            /nodes/{nodeId}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Node]
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        depth=depth,
        status=status,
        types=types,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: None | str | Unset = UNSET,
    depth: int | Unset = UNSET,
    status: NodesListStatus | Unset = "active",
    types: list[NodesListTypesType0Item] | NodesListTypesType1 | Unset = UNSET,
) -> Response[list[Node]]:
    """List nodes (workspace tree, or a flat summary list by type)

    Args:
        parent_id (None | str | Unset): Folder to start from: a node id or a folder slug. Omit or
            null to start from the space root. An unknown ref is a 404 and a node that is not a folder
            is a 400 — never an empty list. With `types`, scopes the flat list to this folder's
            subtree.
        depth (int | Unset): How many levels beneath the start point to eagerly include (default 2
            once either field is set). Capped at 5. With `types` and `parentId`, how many levels of
            the folder's subtree to search (default: all of it).
        status (NodesListStatus | Unset): `active` walks the live TREE. `archived` returns a FLAT
            list of soft-archived nodes (the Trash view) with no parent/depth walk — so the response
            shape you can rely on differs between the two, not just the rows. `parentId` with
            `archived` is a 400. Default: 'active'.
        types (list[NodesListTypesType0Item] | NodesListTypesType1 | Unset): Return a flat list of
            lightweight summaries for these node types instead of the tree — across the space, or
            within `parentId`'s subtree when given. Read one node's full detail with GET
            /nodes/{nodeId}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Node]]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        depth=depth,
        status=status,
        types=types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: None | str | Unset = UNSET,
    depth: int | Unset = UNSET,
    status: NodesListStatus | Unset = "active",
    types: list[NodesListTypesType0Item] | NodesListTypesType1 | Unset = UNSET,
) -> list[Node] | None:
    """List nodes (workspace tree, or a flat summary list by type)

    Args:
        parent_id (None | str | Unset): Folder to start from: a node id or a folder slug. Omit or
            null to start from the space root. An unknown ref is a 404 and a node that is not a folder
            is a 400 — never an empty list. With `types`, scopes the flat list to this folder's
            subtree.
        depth (int | Unset): How many levels beneath the start point to eagerly include (default 2
            once either field is set). Capped at 5. With `types` and `parentId`, how many levels of
            the folder's subtree to search (default: all of it).
        status (NodesListStatus | Unset): `active` walks the live TREE. `archived` returns a FLAT
            list of soft-archived nodes (the Trash view) with no parent/depth walk — so the response
            shape you can rely on differs between the two, not just the rows. `parentId` with
            `archived` is a 400. Default: 'active'.
        types (list[NodesListTypesType0Item] | NodesListTypesType1 | Unset): Return a flat list of
            lightweight summaries for these node types instead of the tree — across the space, or
            within `parentId`'s subtree when given. Read one node's full detail with GET
            /nodes/{nodeId}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Node]
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            depth=depth,
            status=status,
            types=types,
        )
    ).parsed
