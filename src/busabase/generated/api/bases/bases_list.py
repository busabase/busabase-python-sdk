from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base import Base
from ...models.bases_list_fields import BasesListFields
from ...models.bases_list_status import BasesListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: BasesListStatus | Unset = "active",
    fields: BasesListFields | Unset = "all",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_fields: str | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/bases",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Base] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Base.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Base]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: BasesListStatus | Unset = "active",
    fields: BasesListFields | Unset = "all",
) -> Response[list[Base]]:
    """List Bases

    Args:
        status (BasesListStatus | Unset): `active` (default) or the soft-archived set. Archived
            rows have the SAME shape as live ones — this is a predicate, not a different resource.
            Default: 'active'.
        fields (BasesListFields | Unset): `all` (default): every live field. `links`: only
            relation and lookup fields — enough to see how Bases connect (relation targets, lookups,
            inverse relations) across a large space, not to read or edit records. Fetch one Base with
            `bases.get` for its full schema. Default: 'all'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Base]]
    """

    kwargs = _get_kwargs(
        status=status,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: BasesListStatus | Unset = "active",
    fields: BasesListFields | Unset = "all",
) -> list[Base] | None:
    """List Bases

    Args:
        status (BasesListStatus | Unset): `active` (default) or the soft-archived set. Archived
            rows have the SAME shape as live ones — this is a predicate, not a different resource.
            Default: 'active'.
        fields (BasesListFields | Unset): `all` (default): every live field. `links`: only
            relation and lookup fields — enough to see how Bases connect (relation targets, lookups,
            inverse relations) across a large space, not to read or edit records. Fetch one Base with
            `bases.get` for its full schema. Default: 'all'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Base]
    """

    return sync_detailed(
        client=client,
        status=status,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: BasesListStatus | Unset = "active",
    fields: BasesListFields | Unset = "all",
) -> Response[list[Base]]:
    """List Bases

    Args:
        status (BasesListStatus | Unset): `active` (default) or the soft-archived set. Archived
            rows have the SAME shape as live ones — this is a predicate, not a different resource.
            Default: 'active'.
        fields (BasesListFields | Unset): `all` (default): every live field. `links`: only
            relation and lookup fields — enough to see how Bases connect (relation targets, lookups,
            inverse relations) across a large space, not to read or edit records. Fetch one Base with
            `bases.get` for its full schema. Default: 'all'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Base]]
    """

    kwargs = _get_kwargs(
        status=status,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: BasesListStatus | Unset = "active",
    fields: BasesListFields | Unset = "all",
) -> list[Base] | None:
    """List Bases

    Args:
        status (BasesListStatus | Unset): `active` (default) or the soft-archived set. Archived
            rows have the SAME shape as live ones — this is a predicate, not a different resource.
            Default: 'active'.
        fields (BasesListFields | Unset): `all` (default): every live field. `links`: only
            relation and lookup fields — enough to see how Bases connect (relation targets, lookups,
            inverse relations) across a large space, not to read or edit records. Fetch one Base with
            `bases.get` for its full schema. Default: 'all'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Base]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            fields=fields,
        )
    ).parsed
