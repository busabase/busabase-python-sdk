from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.playbook import Playbook
from ...models.playbooks_get_kind import PlaybooksGetKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    kind: PlaybooksGetKind,
    node_id: str,
    *,
    key: str | Unset = UNSET,
    locale: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["key"] = key

    params["locale"] = locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/playbooks/{kind}/{node_id}".format(
            kind=quote(str(kind), safe=""),
            node_id=quote(str(node_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Playbook | None:
    if response.status_code == 200:
        response_200 = Playbook.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Playbook]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    kind: PlaybooksGetKind,
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    key: str | Unset = UNSET,
    locale: str | Unset = UNSET,
) -> Response[Playbook]:
    """Open one playbook: a rendered custom prompt, or a skill's SKILL.md

    Args:
        kind (PlaybooksGetKind):
        node_id (str):
        key (str | Unset): Required for a prompt: the `key` from `playbooks.search`.
        locale (str | Unset): Locale for the prompt label and rendered body, e.g. "en" or "zh-CN"
            — pass the user's. Without one (or with a locale the dashboard does not speak) the body is
            rendered in English and its footer says "Reply in the user's language." instead of naming
            a language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Playbook]
    """

    kwargs = _get_kwargs(
        kind=kind,
        node_id=node_id,
        key=key,
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    kind: PlaybooksGetKind,
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    key: str | Unset = UNSET,
    locale: str | Unset = UNSET,
) -> Playbook | None:
    """Open one playbook: a rendered custom prompt, or a skill's SKILL.md

    Args:
        kind (PlaybooksGetKind):
        node_id (str):
        key (str | Unset): Required for a prompt: the `key` from `playbooks.search`.
        locale (str | Unset): Locale for the prompt label and rendered body, e.g. "en" or "zh-CN"
            — pass the user's. Without one (or with a locale the dashboard does not speak) the body is
            rendered in English and its footer says "Reply in the user's language." instead of naming
            a language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Playbook
    """

    return sync_detailed(
        kind=kind,
        node_id=node_id,
        client=client,
        key=key,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    kind: PlaybooksGetKind,
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    key: str | Unset = UNSET,
    locale: str | Unset = UNSET,
) -> Response[Playbook]:
    """Open one playbook: a rendered custom prompt, or a skill's SKILL.md

    Args:
        kind (PlaybooksGetKind):
        node_id (str):
        key (str | Unset): Required for a prompt: the `key` from `playbooks.search`.
        locale (str | Unset): Locale for the prompt label and rendered body, e.g. "en" or "zh-CN"
            — pass the user's. Without one (or with a locale the dashboard does not speak) the body is
            rendered in English and its footer says "Reply in the user's language." instead of naming
            a language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Playbook]
    """

    kwargs = _get_kwargs(
        kind=kind,
        node_id=node_id,
        key=key,
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    kind: PlaybooksGetKind,
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    key: str | Unset = UNSET,
    locale: str | Unset = UNSET,
) -> Playbook | None:
    """Open one playbook: a rendered custom prompt, or a skill's SKILL.md

    Args:
        kind (PlaybooksGetKind):
        node_id (str):
        key (str | Unset): Required for a prompt: the `key` from `playbooks.search`.
        locale (str | Unset): Locale for the prompt label and rendered body, e.g. "en" or "zh-CN"
            — pass the user's. Without one (or with a locale the dashboard does not speak) the body is
            rendered in English and its footer says "Reply in the user's language." instead of naming
            a language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Playbook
    """

    return (
        await asyncio_detailed(
            kind=kind,
            node_id=node_id,
            client=client,
            key=key,
            locale=locale,
        )
    ).parsed
