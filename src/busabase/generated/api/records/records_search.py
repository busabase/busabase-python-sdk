from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.record import Record
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    base_id: str | Unset = UNSET,
    field_slug: str,
    value_text: str,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["baseId"] = base_id

    params["fieldSlug"] = field_slug

    params["valueText"] = value_text

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/records/search",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Record] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Record.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Record]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    base_id: str | Unset = UNSET,
    field_slug: str,
    value_text: str,
    limit: int | Unset = 50,
) -> Response[list[Record]]:
    """Filter records by field text

    Args:
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404.
            Omitting it searches the whole space.
        field_slug (str): The field's SLUG, not its display name — visible in the Base's field
            settings. With `baseId`, a slug the Base does not have is a 400 listing its fields.
        value_text (str): Matched by EXACT equality, not substring or fuzzy — this is the de-dup-
            by-key lookup. Use `/api/v1/search` for full-text.
        limit (int | Unset): Maximum matches to return. Capped at 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Record]]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        field_slug=field_slug,
        value_text=value_text,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    base_id: str | Unset = UNSET,
    field_slug: str,
    value_text: str,
    limit: int | Unset = 50,
) -> list[Record] | None:
    """Filter records by field text

    Args:
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404.
            Omitting it searches the whole space.
        field_slug (str): The field's SLUG, not its display name — visible in the Base's field
            settings. With `baseId`, a slug the Base does not have is a 400 listing its fields.
        value_text (str): Matched by EXACT equality, not substring or fuzzy — this is the de-dup-
            by-key lookup. Use `/api/v1/search` for full-text.
        limit (int | Unset): Maximum matches to return. Capped at 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Record]
    """

    return sync_detailed(
        client=client,
        base_id=base_id,
        field_slug=field_slug,
        value_text=value_text,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    base_id: str | Unset = UNSET,
    field_slug: str,
    value_text: str,
    limit: int | Unset = 50,
) -> Response[list[Record]]:
    """Filter records by field text

    Args:
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404.
            Omitting it searches the whole space.
        field_slug (str): The field's SLUG, not its display name — visible in the Base's field
            settings. With `baseId`, a slug the Base does not have is a 400 listing its fields.
        value_text (str): Matched by EXACT equality, not substring or fuzzy — this is the de-dup-
            by-key lookup. Use `/api/v1/search` for full-text.
        limit (int | Unset): Maximum matches to return. Capped at 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Record]]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        field_slug=field_slug,
        value_text=value_text,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    base_id: str | Unset = UNSET,
    field_slug: str,
    value_text: str,
    limit: int | Unset = 50,
) -> list[Record] | None:
    """Filter records by field text

    Args:
        base_id (str | Unset): Restrict to one Base — its id or slug; an unknown one is a 404.
            Omitting it searches the whole space.
        field_slug (str): The field's SLUG, not its display name — visible in the Base's field
            settings. With `baseId`, a slug the Base does not have is a 400 listing its fields.
        value_text (str): Matched by EXACT equality, not substring or fuzzy — this is the de-dup-
            by-key lookup. Use `/api/v1/search` for full-text.
        limit (int | Unset): Maximum matches to return. Capped at 100. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Record]
    """

    return (
        await asyncio_detailed(
            client=client,
            base_id=base_id,
            field_slug=field_slug,
            value_text=value_text,
            limit=limit,
        )
    ).parsed
