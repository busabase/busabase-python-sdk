from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.records_list_links_response_200_item import RecordsListLinksResponse200Item
from ...types import Response


def _get_kwargs(
    record_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/records/{record_id}/links".format(
            record_id=quote(str(record_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[RecordsListLinksResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RecordsListLinksResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[RecordsListLinksResponse200Item]]:
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
) -> Response[list[RecordsListLinksResponse200Item]]:
    """List record links

    Args:
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[RecordsListLinksResponse200Item]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[RecordsListLinksResponse200Item] | None:
    """List record links

    Args:
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[RecordsListLinksResponse200Item]
    """

    return sync_detailed(
        record_id=record_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[RecordsListLinksResponse200Item]]:
    """List record links

    Args:
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[RecordsListLinksResponse200Item]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[RecordsListLinksResponse200Item] | None:
    """List record links

    Args:
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[RecordsListLinksResponse200Item]
    """

    return (
        await asyncio_detailed(
            record_id=record_id,
            client=client,
        )
    ).parsed
