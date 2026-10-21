from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.embed_links_list_paged_response_200 import EmbedLinksListPagedResponse200
from ...models.embed_links_list_paged_status import EmbedLinksListPagedStatus
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: EmbedLinksListPagedStatus | Unset = "active",
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/embed-links/paged",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmbedLinksListPagedResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = EmbedLinksListPagedResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EmbedLinksListPagedResponse200 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: EmbedLinksListPagedStatus | Unset = "active",
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[EmbedLinksListPagedResponse200 | Error]:
    """Audit workspace embed links with status filtering and keyset pagination

    Args:
        status (EmbedLinksListPagedStatus | Unset): Filter the workspace audit to active, expired,
            revoked, or all embed links. Default: 'active'.
        limit (int | Unset): Embed links per page. Capped at 100; continue with `cursor`. Default:
            50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmbedLinksListPagedResponse200 | Error]
    """

    kwargs = _get_kwargs(
        status=status,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: EmbedLinksListPagedStatus | Unset = "active",
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> EmbedLinksListPagedResponse200 | Error | None:
    """Audit workspace embed links with status filtering and keyset pagination

    Args:
        status (EmbedLinksListPagedStatus | Unset): Filter the workspace audit to active, expired,
            revoked, or all embed links. Default: 'active'.
        limit (int | Unset): Embed links per page. Capped at 100; continue with `cursor`. Default:
            50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmbedLinksListPagedResponse200 | Error
    """

    return sync_detailed(
        client=client,
        status=status,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: EmbedLinksListPagedStatus | Unset = "active",
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[EmbedLinksListPagedResponse200 | Error]:
    """Audit workspace embed links with status filtering and keyset pagination

    Args:
        status (EmbedLinksListPagedStatus | Unset): Filter the workspace audit to active, expired,
            revoked, or all embed links. Default: 'active'.
        limit (int | Unset): Embed links per page. Capped at 100; continue with `cursor`. Default:
            50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmbedLinksListPagedResponse200 | Error]
    """

    kwargs = _get_kwargs(
        status=status,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: EmbedLinksListPagedStatus | Unset = "active",
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> EmbedLinksListPagedResponse200 | Error | None:
    """Audit workspace embed links with status filtering and keyset pagination

    Args:
        status (EmbedLinksListPagedStatus | Unset): Filter the workspace audit to active, expired,
            revoked, or all embed links. Default: 'active'.
        limit (int | Unset): Embed links per page. Capped at 100; continue with `cursor`. Default:
            50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmbedLinksListPagedResponse200 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
