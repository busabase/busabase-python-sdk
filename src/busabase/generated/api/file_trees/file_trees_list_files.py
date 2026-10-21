from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_tree_file import FileTreeFile
from ...models.file_trees_list_files_type import FileTreesListFilesType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    type_: FileTreesListFilesType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/file-trees/{node_id}/files".format(
            node_id=quote(str(node_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[FileTreeFile] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FileTreeFile.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[FileTreeFile]]:
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
    type_: FileTreesListFilesType | Unset = UNSET,
) -> Response[list[FileTreeFile]]:
    """List file-tree files

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        type_ (FileTreesListFilesType | Unset): Disambiguates a slug. Unnecessary — and ignored —
            when `nodeId` is an id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[FileTreeFile]]
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
    type_: FileTreesListFilesType | Unset = UNSET,
) -> list[FileTreeFile] | None:
    """List file-tree files

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        type_ (FileTreesListFilesType | Unset): Disambiguates a slug. Unnecessary — and ignored —
            when `nodeId` is an id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[FileTreeFile]
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
    type_: FileTreesListFilesType | Unset = UNSET,
) -> Response[list[FileTreeFile]]:
    """List file-tree files

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        type_ (FileTreesListFilesType | Unset): Disambiguates a slug. Unnecessary — and ignored —
            when `nodeId` is an id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[FileTreeFile]]
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
    type_: FileTreesListFilesType | Unset = UNSET,
) -> list[FileTreeFile] | None:
    """List file-tree files

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        type_ (FileTreesListFilesType | Unset): Disambiguates a slug. Unnecessary — and ignored —
            when `nodeId` is an id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[FileTreeFile]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            type_=type_,
        )
    ).parsed
