from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_request import ChangeRequest
from ...models.file_trees_create_change_request_body import FileTreesCreateChangeRequestBody
from ...types import Response


def _get_kwargs(
    node_id: str,
    *,
    body: FileTreesCreateChangeRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/file-trees/{node_id}/change-requests".format(
            node_id=quote(str(node_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChangeRequest | None:
    if response.status_code == 200:
        response_200 = ChangeRequest.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChangeRequest]:
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
    body: FileTreesCreateChangeRequestBody,
) -> Response[ChangeRequest]:
    """Create file-tree change request

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        body (FileTreesCreateChangeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeRequest]
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
    body: FileTreesCreateChangeRequestBody,
) -> ChangeRequest | None:
    """Create file-tree change request

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        body (FileTreesCreateChangeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeRequest
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
    body: FileTreesCreateChangeRequestBody,
) -> Response[ChangeRequest]:
    """Create file-tree change request

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        body (FileTreesCreateChangeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeRequest]
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
    body: FileTreesCreateChangeRequestBody,
) -> ChangeRequest | None:
    """Create file-tree change request

    Args:
        node_id (str): A node id OR a slug. A slug is only unique WITHIN a type, so pass `type`
            alongside one; a node id needs no hint.
        body (FileTreesCreateChangeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeRequest
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            body=body,
        )
    ).parsed
