from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhook_delivery import WebhookDelivery
from ...types import UNSET, Response, Unset


def _get_kwargs(
    rule_id: str,
    *,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/webhooks/{rule_id}/deliveries".format(
            rule_id=quote(str(rule_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[WebhookDelivery] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WebhookDelivery.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[WebhookDelivery]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
) -> Response[list[WebhookDelivery]]:
    """List webhook rule delivery attempts

    Args:
        rule_id (str):
        limit (int | Unset): Delivery attempts to return, newest first. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[WebhookDelivery]]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
) -> list[WebhookDelivery] | None:
    """List webhook rule delivery attempts

    Args:
        rule_id (str):
        limit (int | Unset): Delivery attempts to return, newest first. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[WebhookDelivery]
    """

    return sync_detailed(
        rule_id=rule_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
) -> Response[list[WebhookDelivery]]:
    """List webhook rule delivery attempts

    Args:
        rule_id (str):
        limit (int | Unset): Delivery attempts to return, newest first. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[WebhookDelivery]]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
) -> list[WebhookDelivery] | None:
    """List webhook rule delivery attempts

    Args:
        rule_id (str):
        limit (int | Unset): Delivery attempts to return, newest first. Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[WebhookDelivery]
    """

    return (
        await asyncio_detailed(
            rule_id=rule_id,
            client=client,
            limit=limit,
        )
    ).parsed
