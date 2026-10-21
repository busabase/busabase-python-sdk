from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_activity import AuditActivity
from ...models.change_request_activity import ChangeRequestActivity
from ...models.operation_activity import OperationActivity
from ...models.record_activity import RecordActivity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    record_id: str,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["recordId"] = record_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/activity/record",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
                data: object,
            ) -> AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_activity_item_type_0 = ChangeRequestActivity.from_dict(data)

                    return componentsschemas_activity_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_activity_item_type_1 = OperationActivity.from_dict(data)

                    return componentsschemas_activity_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_activity_item_type_2 = RecordActivity.from_dict(data)

                    return componentsschemas_activity_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_activity_item_type_3 = AuditActivity.from_dict(data)

                return componentsschemas_activity_item_type_3

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity]]:
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
) -> Response[list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity]]:
    """List a single record's raw activity stream

    Args:
        record_id (str): Activity for this record's own history.
        limit (int | Unset): Most recent events to return, capped at 100. This stream has NO
            cursor — it is a recent window, not a pageable history; use `/api/v1/activity/paged` to
            walk further back. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        limit=limit,
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
) -> list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity] | None:
    """List a single record's raw activity stream

    Args:
        record_id (str): Activity for this record's own history.
        limit (int | Unset): Most recent events to return, capped at 100. This stream has NO
            cursor — it is a recent window, not a pageable history; use `/api/v1/activity/paged` to
            walk further back. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity]
    """

    return sync_detailed(
        client=client,
        record_id=record_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    record_id: str,
    limit: int | Unset = 50,
) -> Response[list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity]]:
    """List a single record's raw activity stream

    Args:
        record_id (str): Activity for this record's own history.
        limit (int | Unset): Most recent events to return, capped at 100. This stream has NO
            cursor — it is a recent window, not a pageable history; use `/api/v1/activity/paged` to
            walk further back. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    record_id: str,
    limit: int | Unset = 50,
) -> list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity] | None:
    """List a single record's raw activity stream

    Args:
        record_id (str): Activity for this record's own history.
        limit (int | Unset): Most recent events to return, capped at 100. This stream has NO
            cursor — it is a recent window, not a pageable history; use `/api/v1/activity/paged` to
            walk further back. Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity]
    """

    return (
        await asyncio_detailed(
            client=client,
            record_id=record_id,
            limit=limit,
        )
    ).parsed
