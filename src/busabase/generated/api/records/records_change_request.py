from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.materialized_record import MaterializedRecord
from ...models.pending_change_request import PendingChangeRequest
from ...models.records_change_request_body import RecordsChangeRequestBody
from ...types import Response


def _get_kwargs(
    record_id: str,
    *,
    body: RecordsChangeRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/records/{record_id}/change-requests".format(
            record_id=quote(str(record_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MaterializedRecord | PendingChangeRequest | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> MaterializedRecord | PendingChangeRequest:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = MaterializedRecord.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = PendingChangeRequest.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MaterializedRecord | PendingChangeRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RecordsChangeRequestBody,
) -> Response[MaterializedRecord | PendingChangeRequest]:
    """Create record change request

    Args:
        record_id (str):
        body (RecordsChangeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaterializedRecord | PendingChangeRequest]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RecordsChangeRequestBody,
) -> MaterializedRecord | PendingChangeRequest | None:
    """Create record change request

    Args:
        record_id (str):
        body (RecordsChangeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaterializedRecord | PendingChangeRequest
    """

    return sync_detailed(
        record_id=record_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RecordsChangeRequestBody,
) -> Response[MaterializedRecord | PendingChangeRequest]:
    """Create record change request

    Args:
        record_id (str):
        body (RecordsChangeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaterializedRecord | PendingChangeRequest]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RecordsChangeRequestBody,
) -> MaterializedRecord | PendingChangeRequest | None:
    """Create record change request

    Args:
        record_id (str):
        body (RecordsChangeRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaterializedRecord | PendingChangeRequest
    """

    return (
        await asyncio_detailed(
            record_id=record_id,
            client=client,
            body=body,
        )
    ).parsed
