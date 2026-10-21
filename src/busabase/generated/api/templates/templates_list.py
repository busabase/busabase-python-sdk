from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.templates_list_response_200 import TemplatesListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    refresh: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["refresh"] = refresh

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/templates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TemplatesListResponse200 | None:
    if response.status_code == 200:
        response_200 = TemplatesListResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TemplatesListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    refresh: bool | Unset = UNSET,
) -> Response[TemplatesListResponse200]:
    """List the Template Center catalog

    Args:
        refresh (bool | Unset): Bypass the cache and re-fetch the catalogue — what the refresh
            button does. Slower; leave it off for ordinary reads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplatesListResponse200]
    """

    kwargs = _get_kwargs(
        refresh=refresh,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    refresh: bool | Unset = UNSET,
) -> TemplatesListResponse200 | None:
    """List the Template Center catalog

    Args:
        refresh (bool | Unset): Bypass the cache and re-fetch the catalogue — what the refresh
            button does. Slower; leave it off for ordinary reads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplatesListResponse200
    """

    return sync_detailed(
        client=client,
        refresh=refresh,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    refresh: bool | Unset = UNSET,
) -> Response[TemplatesListResponse200]:
    """List the Template Center catalog

    Args:
        refresh (bool | Unset): Bypass the cache and re-fetch the catalogue — what the refresh
            button does. Slower; leave it off for ordinary reads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplatesListResponse200]
    """

    kwargs = _get_kwargs(
        refresh=refresh,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    refresh: bool | Unset = UNSET,
) -> TemplatesListResponse200 | None:
    """List the Template Center catalog

    Args:
        refresh (bool | Unset): Bypass the cache and re-fetch the catalogue — what the refresh
            button does. Slower; leave it off for ordinary reads.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplatesListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            refresh=refresh,
        )
    ).parsed
