from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bases_list_views_status import BasesListViewsStatus
from ...models.view import View
from ...types import UNSET, Response, Unset


def _get_kwargs(
    base_id: str,
    *,
    status: BasesListViewsStatus | Unset = "active",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/bases/{base_id}/views".format(
            base_id=quote(str(base_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[View] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = View.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[View]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    base_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: BasesListViewsStatus | Unset = "active",
) -> Response[list[View]]:
    """List views for a Base

    Args:
        base_id (str):
        status (BasesListViewsStatus | Unset): `active` (default) or the soft-archived set.
            Archived rows have the SAME shape as live ones — this is a predicate, not a different
            resource. Default: 'active'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[View]]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    base_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: BasesListViewsStatus | Unset = "active",
) -> list[View] | None:
    """List views for a Base

    Args:
        base_id (str):
        status (BasesListViewsStatus | Unset): `active` (default) or the soft-archived set.
            Archived rows have the SAME shape as live ones — this is a predicate, not a different
            resource. Default: 'active'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[View]
    """

    return sync_detailed(
        base_id=base_id,
        client=client,
        status=status,
    ).parsed


async def asyncio_detailed(
    base_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: BasesListViewsStatus | Unset = "active",
) -> Response[list[View]]:
    """List views for a Base

    Args:
        base_id (str):
        status (BasesListViewsStatus | Unset): `active` (default) or the soft-archived set.
            Archived rows have the SAME shape as live ones — this is a predicate, not a different
            resource. Default: 'active'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[View]]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    base_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: BasesListViewsStatus | Unset = "active",
) -> list[View] | None:
    """List views for a Base

    Args:
        base_id (str):
        status (BasesListViewsStatus | Unset): `active` (default) or the soft-archived set.
            Archived rows have the SAME shape as live ones — this is a predicate, not a different
            resource. Default: 'active'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[View]
    """

    return (
        await asyncio_detailed(
            base_id=base_id,
            client=client,
            status=status,
        )
    ).parsed
