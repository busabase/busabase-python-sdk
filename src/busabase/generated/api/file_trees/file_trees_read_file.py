from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_trees_read_file_response_200 import FileTreesReadFileResponse200
from ...models.file_trees_read_file_type import FileTreesReadFileType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    file_path: str,
    *,
    type_: FileTreesReadFileType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/file-trees/{node_id}/files/{file_path}".format(
            node_id=quote(str(node_id), safe=""),
            file_path=quote(str(file_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileTreesReadFileResponse200 | None:
    if response.status_code == 200:
        response_200 = FileTreesReadFileResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FileTreesReadFileResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node_id: str,
    file_path: str,
    *,
    client: AuthenticatedClient | Client,
    type_: FileTreesReadFileType | Unset = UNSET,
) -> Response[FileTreesReadFileResponse200]:
    """Read file-tree file

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        file_path (str):
        type_ (FileTreesReadFileType | Unset): Disambiguates a slug. Unnecessary — and ignored —
            when `nodeId` is an id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileTreesReadFileResponse200]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        file_path=file_path,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    file_path: str,
    *,
    client: AuthenticatedClient | Client,
    type_: FileTreesReadFileType | Unset = UNSET,
) -> FileTreesReadFileResponse200 | None:
    """Read file-tree file

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        file_path (str):
        type_ (FileTreesReadFileType | Unset): Disambiguates a slug. Unnecessary — and ignored —
            when `nodeId` is an id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileTreesReadFileResponse200
    """

    return sync_detailed(
        node_id=node_id,
        file_path=file_path,
        client=client,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    file_path: str,
    *,
    client: AuthenticatedClient | Client,
    type_: FileTreesReadFileType | Unset = UNSET,
) -> Response[FileTreesReadFileResponse200]:
    """Read file-tree file

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        file_path (str):
        type_ (FileTreesReadFileType | Unset): Disambiguates a slug. Unnecessary — and ignored —
            when `nodeId` is an id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileTreesReadFileResponse200]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        file_path=file_path,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    file_path: str,
    *,
    client: AuthenticatedClient | Client,
    type_: FileTreesReadFileType | Unset = UNSET,
) -> FileTreesReadFileResponse200 | None:
    """Read file-tree file

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        file_path (str):
        type_ (FileTreesReadFileType | Unset): Disambiguates a slug. Unnecessary — and ignored —
            when `nodeId` is an id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileTreesReadFileResponse200
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            file_path=file_path,
            client=client,
            type_=type_,
        )
    ).parsed
