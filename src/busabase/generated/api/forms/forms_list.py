from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.forms_list_response_200 import FormsListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    target_base_id: str,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["targetBaseId"] = target_base_id

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/forms",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FormsListResponse200 | None:
    if response.status_code == 200:
        response_200 = FormsListResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FormsListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    target_base_id: str,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[FormsListResponse200]:
    """List forms bound to a Base

    Args:
        target_base_id (str): The Base the forms WRITE INTO — required; this is not a space-wide
            listing.
        limit (int | Unset): Forms per page. Capped at 100; ask for the next page with `cursor`.
            Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormsListResponse200]
    """

    kwargs = _get_kwargs(
        target_base_id=target_base_id,
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
    target_base_id: str,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> FormsListResponse200 | None:
    """List forms bound to a Base

    Args:
        target_base_id (str): The Base the forms WRITE INTO — required; this is not a space-wide
            listing.
        limit (int | Unset): Forms per page. Capped at 100; ask for the next page with `cursor`.
            Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormsListResponse200
    """

    return sync_detailed(
        client=client,
        target_base_id=target_base_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    target_base_id: str,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[FormsListResponse200]:
    """List forms bound to a Base

    Args:
        target_base_id (str): The Base the forms WRITE INTO — required; this is not a space-wide
            listing.
        limit (int | Unset): Forms per page. Capped at 100; ask for the next page with `cursor`.
            Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormsListResponse200]
    """

    kwargs = _get_kwargs(
        target_base_id=target_base_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    target_base_id: str,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> FormsListResponse200 | None:
    """List forms bound to a Base

    Args:
        target_base_id (str): The Base the forms WRITE INTO — required; this is not a space-wide
            listing.
        limit (int | Unset): Forms per page. Capped at 100; ask for the next page with `cursor`.
            Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormsListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            target_base_id=target_base_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
