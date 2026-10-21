from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_list_for_record_paged_response_200 import ActivityListForRecordPagedResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    record_id: str,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["recordId"] = record_id

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/activity/record/paged",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityListForRecordPagedResponse200 | None:
    if response.status_code == 200:
        response_200 = ActivityListForRecordPagedResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivityListForRecordPagedResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    record_id: str,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ActivityListForRecordPagedResponse200]:
    """List a record's activity with keyset pagination

    Args:
        record_id (str): Activity is scoped to this record's own history.
        limit (int | Unset): Items per page. Defaults to 50 and is capped at 100. Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityListForRecordPagedResponse200]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    record_id: str,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ActivityListForRecordPagedResponse200 | None:
    """List a record's activity with keyset pagination

    Args:
        record_id (str): Activity is scoped to this record's own history.
        limit (int | Unset): Items per page. Defaults to 50 and is capped at 100. Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityListForRecordPagedResponse200
    """

    return sync_detailed(
        client=client,
        record_id=record_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    record_id: str,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ActivityListForRecordPagedResponse200]:
    """List a record's activity with keyset pagination

    Args:
        record_id (str): Activity is scoped to this record's own history.
        limit (int | Unset): Items per page. Defaults to 50 and is capped at 100. Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivityListForRecordPagedResponse200]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    record_id: str,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ActivityListForRecordPagedResponse200 | None:
    """List a record's activity with keyset pagination

    Args:
        record_id (str): Activity is scoped to this record's own history.
        limit (int | Unset): Items per page. Defaults to 50 and is capped at 100. Default: 50.
        cursor (str | Unset): Opaque page cursor: pass back the `nextCursor` from the previous
            response. Do not construct or parse it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivityListForRecordPagedResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            record_id=record_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
