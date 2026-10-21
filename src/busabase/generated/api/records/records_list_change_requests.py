from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_request import ChangeRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    record_id: str,
    *,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/records/{record_id}/change-requests".format(
            record_id=quote(str(record_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[ChangeRequest] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChangeRequest.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[ChangeRequest]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> Response[list[ChangeRequest]]:
    """List record change request history

    Args:
        record_id (str):
        limit (int | Unset): Recent change request summaries to return. Omit to retain the full
            legacy history.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ChangeRequest]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> list[ChangeRequest] | None:
    """List record change request history

    Args:
        record_id (str):
        limit (int | Unset): Recent change request summaries to return. Omit to retain the full
            legacy history.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ChangeRequest]
    """

    return sync_detailed(
        record_id=record_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> Response[list[ChangeRequest]]:
    """List record change request history

    Args:
        record_id (str):
        limit (int | Unset): Recent change request summaries to return. Omit to retain the full
            legacy history.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ChangeRequest]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> list[ChangeRequest] | None:
    """List record change request history

    Args:
        record_id (str):
        limit (int | Unset): Recent change request summaries to return. Omit to retain the full
            legacy history.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ChangeRequest]
    """

    return (
        await asyncio_detailed(
            record_id=record_id,
            client=client,
            limit=limit,
        )
    ).parsed
