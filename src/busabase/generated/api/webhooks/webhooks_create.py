from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_webhook_rule import HttpWebhookRule
from ...models.http_webhook_rule_input import HttpWebhookRuleInput
from ...models.notify_agent_webhook_rule import NotifyAgentWebhookRule
from ...models.notify_agent_webhook_rule_input import NotifyAgentWebhookRuleInput
from ...models.run_function_webhook_rule import RunFunctionWebhookRule
from ...models.run_function_webhook_rule_input import RunFunctionWebhookRuleInput
from ...types import Response


def _get_kwargs(
    *,
    body: HttpWebhookRuleInput | NotifyAgentWebhookRuleInput | RunFunctionWebhookRuleInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/webhooks",
    }

    if isinstance(body, HttpWebhookRuleInput) or isinstance(body, NotifyAgentWebhookRuleInput):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient | Client,
    body: HttpWebhookRuleInput | NotifyAgentWebhookRuleInput | RunFunctionWebhookRuleInput,
) -> Response[HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule]:
    """Create webhook automation rule

    Args:
        body (HttpWebhookRuleInput | NotifyAgentWebhookRuleInput | RunFunctionWebhookRuleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: HttpWebhookRuleInput | NotifyAgentWebhookRuleInput | RunFunctionWebhookRuleInput,
) -> HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule | None:
    """Create webhook automation rule

    Args:
        body (HttpWebhookRuleInput | NotifyAgentWebhookRuleInput | RunFunctionWebhookRuleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: HttpWebhookRuleInput | NotifyAgentWebhookRuleInput | RunFunctionWebhookRuleInput,
) -> Response[HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule]:
    """Create webhook automation rule

    Args:
        body (HttpWebhookRuleInput | NotifyAgentWebhookRuleInput | RunFunctionWebhookRuleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: HttpWebhookRuleInput | NotifyAgentWebhookRuleInput | RunFunctionWebhookRuleInput,
) -> HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule | None:
    """Create webhook automation rule

    Args:
        body (HttpWebhookRuleInput | NotifyAgentWebhookRuleInput | RunFunctionWebhookRuleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpWebhookRule | NotifyAgentWebhookRule | RunFunctionWebhookRule
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
