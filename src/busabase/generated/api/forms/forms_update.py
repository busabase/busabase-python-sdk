from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.form import Form
from ...models.forms_update_body import FormsUpdateBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    body: FormsUpdateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/forms/{node_id}".format(
            node_id=quote(str(node_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Form | None:
    if response.status_code == 200:
        response_200 = Form.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Form]:
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
    body: FormsUpdateBody | Unset = UNSET,
) -> Response[Form]:
    """Update a form's config (owner-managed, not a change request)

    Args:
        node_id (str):
        body (FormsUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Form]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormsUpdateBody | Unset = UNSET,
) -> Form | None:
    """Update a form's config (owner-managed, not a change request)

    Args:
        node_id (str):
        body (FormsUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Form
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormsUpdateBody | Unset = UNSET,
) -> Response[Form]:
    """Update a form's config (owner-managed, not a change request)

    Args:
        node_id (str):
        body (FormsUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Form]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FormsUpdateBody | Unset = UNSET,
) -> Form | None:
    """Update a form's config (owner-managed, not a change request)

    Args:
        node_id (str):
        body (FormsUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Form
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            body=body,
        )
    ).parsed
