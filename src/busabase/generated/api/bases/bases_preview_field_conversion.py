from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bases_preview_field_conversion_body import BasesPreviewFieldConversionBody
from ...models.bases_preview_field_conversion_response_200 import BasesPreviewFieldConversionResponse200
from ...types import Response


def _get_kwargs(
    base_id: str,
    *,
    body: BasesPreviewFieldConversionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/bases/{base_id}/fields/convert/preview".format(
            base_id=quote(str(base_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BasesPreviewFieldConversionResponse200 | None:
    if response.status_code == 200:
        response_200 = BasesPreviewFieldConversionResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BasesPreviewFieldConversionResponse200]:
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
    body: BasesPreviewFieldConversionBody,
) -> Response[BasesPreviewFieldConversionResponse200]:
    """Preview field type conversion

    Args:
        base_id (str):
        body (BasesPreviewFieldConversionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BasesPreviewFieldConversionResponse200]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    base_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BasesPreviewFieldConversionBody,
) -> BasesPreviewFieldConversionResponse200 | None:
    """Preview field type conversion

    Args:
        base_id (str):
        body (BasesPreviewFieldConversionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BasesPreviewFieldConversionResponse200
    """

    return sync_detailed(
        base_id=base_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    base_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BasesPreviewFieldConversionBody,
) -> Response[BasesPreviewFieldConversionResponse200]:
    """Preview field type conversion

    Args:
        base_id (str):
        body (BasesPreviewFieldConversionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BasesPreviewFieldConversionResponse200]
    """

    kwargs = _get_kwargs(
        base_id=base_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    base_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BasesPreviewFieldConversionBody,
) -> BasesPreviewFieldConversionResponse200 | None:
    """Preview field type conversion

    Args:
        base_id (str):
        body (BasesPreviewFieldConversionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BasesPreviewFieldConversionResponse200
    """

    return (
        await asyncio_detailed(
            base_id=base_id,
            client=client,
            body=body,
        )
    ).parsed
