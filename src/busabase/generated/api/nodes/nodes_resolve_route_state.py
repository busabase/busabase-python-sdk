from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.active_node_route_state import ActiveNodeRouteState
from ...models.archived_node_route_state import ArchivedNodeRouteState
from ...models.nodes_resolve_route_state_type import NodesResolveRouteStateType
from ...models.unavailable_node_route_state import UnavailableNodeRouteState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    type_: NodesResolveRouteStateType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/nodes/route-state/{node_id}".format(
            node_id=quote(str(node_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActiveNodeRouteState | ArchivedNodeRouteState | UnavailableNodeRouteState | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> ActiveNodeRouteState | ArchivedNodeRouteState | UnavailableNodeRouteState:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ActiveNodeRouteState.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = ArchivedNodeRouteState.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = UnavailableNodeRouteState.from_dict(data)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActiveNodeRouteState | ArchivedNodeRouteState | UnavailableNodeRouteState]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: NodesResolveRouteStateType | Unset = UNSET,
) -> Response[ActiveNodeRouteState | ArchivedNodeRouteState | UnavailableNodeRouteState]:
    """Resolve whether a dashboard node route is active, archived, or unavailable

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesResolveRouteStateType | Unset): Optional disambiguation hint, only needed when
            `nodeId` is a slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActiveNodeRouteState | ArchivedNodeRouteState | UnavailableNodeRouteState]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: NodesResolveRouteStateType | Unset = UNSET,
) -> ActiveNodeRouteState | ArchivedNodeRouteState | UnavailableNodeRouteState | None:
    """Resolve whether a dashboard node route is active, archived, or unavailable

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesResolveRouteStateType | Unset): Optional disambiguation hint, only needed when
            `nodeId` is a slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActiveNodeRouteState | ArchivedNodeRouteState | UnavailableNodeRouteState
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: NodesResolveRouteStateType | Unset = UNSET,
) -> Response[ActiveNodeRouteState | ArchivedNodeRouteState | UnavailableNodeRouteState]:
    """Resolve whether a dashboard node route is active, archived, or unavailable

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesResolveRouteStateType | Unset): Optional disambiguation hint, only needed when
            `nodeId` is a slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActiveNodeRouteState | ArchivedNodeRouteState | UnavailableNodeRouteState]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: NodesResolveRouteStateType | Unset = UNSET,
) -> ActiveNodeRouteState | ArchivedNodeRouteState | UnavailableNodeRouteState | None:
    """Resolve whether a dashboard node route is active, archived, or unavailable

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesResolveRouteStateType | Unset): Optional disambiguation hint, only needed when
            `nodeId` is a slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActiveNodeRouteState | ArchivedNodeRouteState | UnavailableNodeRouteState
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            type_=type_,
        )
    ).parsed
