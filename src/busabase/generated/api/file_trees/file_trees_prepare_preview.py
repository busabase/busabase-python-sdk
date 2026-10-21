from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_trees_prepare_preview_body import FileTreesPreparePreviewBody
from ...models.file_trees_prepare_preview_response_200_type_0 import FileTreesPreparePreviewResponse200Type0
from ...models.file_trees_prepare_preview_response_200_type_1 import FileTreesPreparePreviewResponse200Type1
from ...models.file_trees_prepare_preview_response_200_type_2 import FileTreesPreparePreviewResponse200Type2
from ...types import Response


def _get_kwargs(
    node_id: str,
    *,
    body: FileTreesPreparePreviewBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/file-trees/{node_id}/preview".format(
            node_id=quote(str(node_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FileTreesPreparePreviewResponse200Type0
    | FileTreesPreparePreviewResponse200Type1
    | FileTreesPreparePreviewResponse200Type2
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            FileTreesPreparePreviewResponse200Type0
            | FileTreesPreparePreviewResponse200Type1
            | FileTreesPreparePreviewResponse200Type2
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = FileTreesPreparePreviewResponse200Type0.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = FileTreesPreparePreviewResponse200Type1.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = FileTreesPreparePreviewResponse200Type2.from_dict(data)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FileTreesPreparePreviewResponse200Type0
    | FileTreesPreparePreviewResponse200Type1
    | FileTreesPreparePreviewResponse200Type2
]:
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
    body: FileTreesPreparePreviewBody,
) -> Response[
    FileTreesPreparePreviewResponse200Type0
    | FileTreesPreparePreviewResponse200Type1
    | FileTreesPreparePreviewResponse200Type2
]:
    """Prepare a Drive file preview

    Args:
        node_id (str):
        body (FileTreesPreparePreviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileTreesPreparePreviewResponse200Type0 | FileTreesPreparePreviewResponse200Type1 | FileTreesPreparePreviewResponse200Type2]
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
    body: FileTreesPreparePreviewBody,
) -> (
    FileTreesPreparePreviewResponse200Type0
    | FileTreesPreparePreviewResponse200Type1
    | FileTreesPreparePreviewResponse200Type2
    | None
):
    """Prepare a Drive file preview

    Args:
        node_id (str):
        body (FileTreesPreparePreviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileTreesPreparePreviewResponse200Type0 | FileTreesPreparePreviewResponse200Type1 | FileTreesPreparePreviewResponse200Type2
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
    body: FileTreesPreparePreviewBody,
) -> Response[
    FileTreesPreparePreviewResponse200Type0
    | FileTreesPreparePreviewResponse200Type1
    | FileTreesPreparePreviewResponse200Type2
]:
    """Prepare a Drive file preview

    Args:
        node_id (str):
        body (FileTreesPreparePreviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileTreesPreparePreviewResponse200Type0 | FileTreesPreparePreviewResponse200Type1 | FileTreesPreparePreviewResponse200Type2]
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
    body: FileTreesPreparePreviewBody,
) -> (
    FileTreesPreparePreviewResponse200Type0
    | FileTreesPreparePreviewResponse200Type1
    | FileTreesPreparePreviewResponse200Type2
    | None
):
    """Prepare a Drive file preview

    Args:
        node_id (str):
        body (FileTreesPreparePreviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileTreesPreparePreviewResponse200Type0 | FileTreesPreparePreviewResponse200Type1 | FileTreesPreparePreviewResponse200Type2
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            body=body,
        )
    ).parsed
