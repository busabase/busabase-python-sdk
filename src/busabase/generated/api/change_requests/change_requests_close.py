from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_request import ChangeRequest
from ...models.change_requests_close_body import ChangeRequestsCloseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    change_request_id: str,
    *,
    body: ChangeRequestsCloseBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/change-requests/{change_request_id}/close".format(
            change_request_id=quote(str(change_request_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChangeRequest | None:
    if response.status_code == 200:
        response_200 = ChangeRequest.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChangeRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    change_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ChangeRequestsCloseBody | Unset = UNSET,
) -> Response[ChangeRequest]:
    """Close change request

    Args:
        change_request_id (str):
        body (ChangeRequestsCloseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeRequest]
    """

    kwargs = _get_kwargs(
        change_request_id=change_request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    change_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ChangeRequestsCloseBody | Unset = UNSET,
) -> ChangeRequest | None:
    """Close change request

    Args:
        change_request_id (str):
        body (ChangeRequestsCloseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeRequest
    """

    return sync_detailed(
        change_request_id=change_request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    change_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ChangeRequestsCloseBody | Unset = UNSET,
) -> Response[ChangeRequest]:
    """Close change request

    Args:
        change_request_id (str):
        body (ChangeRequestsCloseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeRequest]
    """

    kwargs = _get_kwargs(
        change_request_id=change_request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    change_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ChangeRequestsCloseBody | Unset = UNSET,
) -> ChangeRequest | None:
    """Close change request

    Args:
        change_request_id (str):
        body (ChangeRequestsCloseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeRequest
    """

    return (
        await asyncio_detailed(
            change_request_id=change_request_id,
            client=client,
            body=body,
        )
    ).parsed
