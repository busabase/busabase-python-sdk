from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_webhook_rule import HttpWebhookRule
from ...models.notify_agent_webhook_rule import NotifyAgentWebhookRule
from ...models.run_function_webhook_rule import RunFunctionWebhookRule
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/webhooks/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_rule_type_0 = HttpWebhookRule.from_dict(data)

                return componentsschemas_webhook_rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_rule_type_1 = NotifyAgentWebhookRule.from_dict(data)

                return componentsschemas_webhook_rule_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_webhook_rule_type_2 = RunFunctionWebhookRule.from_dict(data)

            return componentsschemas_webhook_rule_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule]:
    """Get webhook automation rule

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule | None:
    """Get webhook automation rule

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule]:
    """Get webhook automation rule

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule | None:
    """Get webhook automation rule

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
