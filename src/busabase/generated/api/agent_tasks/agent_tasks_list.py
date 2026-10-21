from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_tasks_list_response_200 import AgentTasksListResponse200
from ...models.agent_tasks_list_status import AgentTasksListStatus
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    status: AgentTasksListStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/agent-tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentTasksListResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = AgentTasksListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentTasksListResponse200 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    status: AgentTasksListStatus | Unset = UNSET,
) -> Response[AgentTasksListResponse200 | Error]:
    """List agent tasks

    Args:
        limit (str | Unset):
        offset (str | Unset):
        status (AgentTasksListStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentTasksListResponse200 | Error]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    status: AgentTasksListStatus | Unset = UNSET,
) -> AgentTasksListResponse200 | Error | None:
    """List agent tasks

    Args:
        limit (str | Unset):
        offset (str | Unset):
        status (AgentTasksListStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentTasksListResponse200 | Error
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    status: AgentTasksListStatus | Unset = UNSET,
) -> Response[AgentTasksListResponse200 | Error]:
    """List agent tasks

    Args:
        limit (str | Unset):
        offset (str | Unset):
        status (AgentTasksListStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentTasksListResponse200 | Error]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    status: AgentTasksListStatus | Unset = UNSET,
) -> AgentTasksListResponse200 | Error | None:
    """List agent tasks

    Args:
        limit (str | Unset):
        offset (str | Unset):
        status (AgentTasksListStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentTasksListResponse200 | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            status=status,
        )
    ).parsed
