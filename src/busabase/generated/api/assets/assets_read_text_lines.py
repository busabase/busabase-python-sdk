from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.read_lines_result import ReadLinesResult
from ...types import UNSET, Response


def _get_kwargs(
    asset_id: str,
    *,
    start_line: int,
    end_line: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["startLine"] = start_line

    params["endLine"] = end_line

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/assets/{asset_id}/text/lines".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ReadLinesResult | None:
    if response.status_code == 200:
        response_200 = ReadLinesResult.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ReadLinesResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_line: int,
    end_line: int,
) -> Response[ReadLinesResult]:
    """Read an exact line range from an asset's text

    Args:
        asset_id (str):
        start_line (int): First line to read. 1-indexed, and INCLUSIVE.
        end_line (int): Last line to read, INCLUSIVE. A range wider than 2000 lines is silently
            narrowed to the first 2000 rather than rejected — the response reports `lineCountCapped`
            when that happened, so check it before concluding the file ends there.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReadLinesResult]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        start_line=start_line,
        end_line=end_line,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_line: int,
    end_line: int,
) -> ReadLinesResult | None:
    """Read an exact line range from an asset's text

    Args:
        asset_id (str):
        start_line (int): First line to read. 1-indexed, and INCLUSIVE.
        end_line (int): Last line to read, INCLUSIVE. A range wider than 2000 lines is silently
            narrowed to the first 2000 rather than rejected — the response reports `lineCountCapped`
            when that happened, so check it before concluding the file ends there.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReadLinesResult
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        start_line=start_line,
        end_line=end_line,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_line: int,
    end_line: int,
) -> Response[ReadLinesResult]:
    """Read an exact line range from an asset's text

    Args:
        asset_id (str):
        start_line (int): First line to read. 1-indexed, and INCLUSIVE.
        end_line (int): Last line to read, INCLUSIVE. A range wider than 2000 lines is silently
            narrowed to the first 2000 rather than rejected — the response reports `lineCountCapped`
            when that happened, so check it before concluding the file ends there.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReadLinesResult]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        start_line=start_line,
        end_line=end_line,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_line: int,
    end_line: int,
) -> ReadLinesResult | None:
    """Read an exact line range from an asset's text

    Args:
        asset_id (str):
        start_line (int): First line to read. 1-indexed, and INCLUSIVE.
        end_line (int): Last line to read, INCLUSIVE. A range wider than 2000 lines is silently
            narrowed to the first 2000 rather than rejected — the response reports `lineCountCapped`
            when that happened, so check it before concluding the file ends there.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReadLinesResult
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            start_line=start_line,
            end_line=end_line,
        )
    ).parsed
