from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.record import Record
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    record_id: str | Unset = UNSET,
    base_id: str | Unset = UNSET,
    field_slug: str | Unset = UNSET,
    value_text: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["recordId"] = record_id

    params["baseId"] = base_id

    params["fieldSlug"] = field_slug

    params["valueText"] = value_text

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/records/get",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Record | None:
    if response.status_code == 200:
        response_200 = Record.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Record]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    record_id: str | Unset = UNSET,
    base_id: str | Unset = UNSET,
    field_slug: str | Unset = UNSET,
    value_text: str | Unset = UNSET,
) -> Response[Error | Record]:
    """Get record

     Provide exactly one selector: recordId alone, or the complete baseId + fieldSlug + valueText tuple.
    Other combinations return 400.

    Args:
        record_id (str | Unset): Record id selector. Use alone; do not combine with field selector
            fields.
        base_id (str | Unset): Field selector: Base id. Requires fieldSlug and valueText.
        field_slug (str | Unset): Field selector: exact field slug. Requires baseId and valueText.
        value_text (str | Unset): Field selector: exact text value. Requires baseId and fieldSlug.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Record]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        base_id=base_id,
        field_slug=field_slug,
        value_text=value_text,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    record_id: str | Unset = UNSET,
    base_id: str | Unset = UNSET,
    field_slug: str | Unset = UNSET,
    value_text: str | Unset = UNSET,
) -> Error | Record | None:
    """Get record

     Provide exactly one selector: recordId alone, or the complete baseId + fieldSlug + valueText tuple.
    Other combinations return 400.

    Args:
        record_id (str | Unset): Record id selector. Use alone; do not combine with field selector
            fields.
        base_id (str | Unset): Field selector: Base id. Requires fieldSlug and valueText.
        field_slug (str | Unset): Field selector: exact field slug. Requires baseId and valueText.
        value_text (str | Unset): Field selector: exact text value. Requires baseId and fieldSlug.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Record
    """

    return sync_detailed(
        client=client,
        record_id=record_id,
        base_id=base_id,
        field_slug=field_slug,
        value_text=value_text,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    record_id: str | Unset = UNSET,
    base_id: str | Unset = UNSET,
    field_slug: str | Unset = UNSET,
    value_text: str | Unset = UNSET,
) -> Response[Error | Record]:
    """Get record

     Provide exactly one selector: recordId alone, or the complete baseId + fieldSlug + valueText tuple.
    Other combinations return 400.

    Args:
        record_id (str | Unset): Record id selector. Use alone; do not combine with field selector
            fields.
        base_id (str | Unset): Field selector: Base id. Requires fieldSlug and valueText.
        field_slug (str | Unset): Field selector: exact field slug. Requires baseId and valueText.
        value_text (str | Unset): Field selector: exact text value. Requires baseId and fieldSlug.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Record]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        base_id=base_id,
        field_slug=field_slug,
        value_text=value_text,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    record_id: str | Unset = UNSET,
    base_id: str | Unset = UNSET,
    field_slug: str | Unset = UNSET,
    value_text: str | Unset = UNSET,
) -> Error | Record | None:
    """Get record

     Provide exactly one selector: recordId alone, or the complete baseId + fieldSlug + valueText tuple.
    Other combinations return 400.

    Args:
        record_id (str | Unset): Record id selector. Use alone; do not combine with field selector
            fields.
        base_id (str | Unset): Field selector: Base id. Requires fieldSlug and valueText.
        field_slug (str | Unset): Field selector: exact field slug. Requires baseId and valueText.
        value_text (str | Unset): Field selector: exact text value. Requires baseId and fieldSlug.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Record
    """

    return (
        await asyncio_detailed(
            client=client,
            record_id=record_id,
            base_id=base_id,
            field_slug=field_slug,
            value_text=value_text,
        )
    ).parsed
