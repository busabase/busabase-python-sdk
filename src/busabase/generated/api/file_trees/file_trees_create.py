from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_trees_create_body import FileTreesCreateBody
from ...models.materialized_file_tree import MaterializedFileTree
from ...models.pending_change_request import PendingChangeRequest
from ...types import Response


def _get_kwargs(
    *,
    body: FileTreesCreateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/file-trees",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MaterializedFileTree | PendingChangeRequest | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> MaterializedFileTree | PendingChangeRequest:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = MaterializedFileTree.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = PendingChangeRequest.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MaterializedFileTree | PendingChangeRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FileTreesCreateBody,
) -> Response[MaterializedFileTree | PendingChangeRequest]:
    """Create file-tree node

    Args:
        body (FileTreesCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaterializedFileTree | PendingChangeRequest]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: FileTreesCreateBody,
) -> MaterializedFileTree | PendingChangeRequest | None:
    """Create file-tree node

    Args:
        body (FileTreesCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaterializedFileTree | PendingChangeRequest
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FileTreesCreateBody,
) -> Response[MaterializedFileTree | PendingChangeRequest]:
    """Create file-tree node

    Args:
        body (FileTreesCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaterializedFileTree | PendingChangeRequest]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FileTreesCreateBody,
) -> MaterializedFileTree | PendingChangeRequest | None:
    """Create file-tree node

    Args:
        body (FileTreesCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaterializedFileTree | PendingChangeRequest
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
