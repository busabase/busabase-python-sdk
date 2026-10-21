from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.created_embed_link import CreatedEmbedLink
from ...types import Response


def _get_kwargs(
    change_request_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/change-requests/{change_request_id}/preview-link".format(
            change_request_id=quote(str(change_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreatedEmbedLink | None:
    if response.status_code == 200:
        response_200 = CreatedEmbedLink.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreatedEmbedLink]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    change_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CreatedEmbedLink]:
    """Create a short-lived preview link for a visible Change Request

    Args:
        change_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedEmbedLink]
    """

    kwargs = _get_kwargs(
        change_request_id=change_request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    change_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CreatedEmbedLink | None:
    """Create a short-lived preview link for a visible Change Request

    Args:
        change_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedEmbedLink
    """

    return sync_detailed(
        change_request_id=change_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    change_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CreatedEmbedLink]:
    """Create a short-lived preview link for a visible Change Request

    Args:
        change_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedEmbedLink]
    """

    kwargs = _get_kwargs(
        change_request_id=change_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    change_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CreatedEmbedLink | None:
    """Create a short-lived preview link for a visible Change Request

    Args:
        change_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedEmbedLink
    """

    return (
        await asyncio_detailed(
            change_request_id=change_request_id,
            client=client,
        )
    ).parsed
