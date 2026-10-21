from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.embed_link import EmbedLink
from ...models.embed_links_list_type import EmbedLinksListType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: EmbedLinksListType | Unset = UNSET,
    type_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params["typeId"] = type_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/embed-links",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | list[EmbedLink] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EmbedLink.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Error | list[EmbedLink]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: EmbedLinksListType | Unset = UNSET,
    type_id: str | Unset = UNSET,
) -> Response[Error | list[EmbedLink]]:
    """List embed links the caller can manage

    Args:
        type_ (EmbedLinksListType | Unset): Which kind of target the links point at. Omitting it
            returns links of every kind.
        type_id (str | Unset): The target's id, interpreted according to `type`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[EmbedLink]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        type_id=type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: EmbedLinksListType | Unset = UNSET,
    type_id: str | Unset = UNSET,
) -> Error | list[EmbedLink] | None:
    """List embed links the caller can manage

    Args:
        type_ (EmbedLinksListType | Unset): Which kind of target the links point at. Omitting it
            returns links of every kind.
        type_id (str | Unset): The target's id, interpreted according to `type`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[EmbedLink]
    """

    return sync_detailed(
        client=client,
        type_=type_,
        type_id=type_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: EmbedLinksListType | Unset = UNSET,
    type_id: str | Unset = UNSET,
) -> Response[Error | list[EmbedLink]]:
    """List embed links the caller can manage

    Args:
        type_ (EmbedLinksListType | Unset): Which kind of target the links point at. Omitting it
            returns links of every kind.
        type_id (str | Unset): The target's id, interpreted according to `type`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[EmbedLink]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        type_id=type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: EmbedLinksListType | Unset = UNSET,
    type_id: str | Unset = UNSET,
) -> Error | list[EmbedLink] | None:
    """List embed links the caller can manage

    Args:
        type_ (EmbedLinksListType | Unset): Which kind of target the links point at. Omitting it
            returns links of every kind.
        type_id (str | Unset): The target's id, interpreted according to `type`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[EmbedLink]
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            type_id=type_id,
        )
    ).parsed
