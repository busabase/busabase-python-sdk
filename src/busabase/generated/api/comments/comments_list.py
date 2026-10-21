from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.comment import Comment
from ...models.comments_list_subject_type import CommentsListSubjectType
from ...types import UNSET, Response


def _get_kwargs(
    *,
    subject_type: CommentsListSubjectType,
    subject_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_subject_type: str = subject_type
    params["subjectType"] = json_subject_type

    params["subjectId"] = subject_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/comments",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Comment] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Comment.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Comment]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    subject_type: CommentsListSubjectType,
    subject_id: str,
) -> Response[list[Comment]]:
    """List comments

    Args:
        subject_type (CommentsListSubjectType): What the comment thread hangs off, which decides
            how `subjectId` is interpreted.
        subject_id (str): The subject's id, interpreted according to `subjectType`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Comment]]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        subject_id=subject_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    subject_type: CommentsListSubjectType,
    subject_id: str,
) -> list[Comment] | None:
    """List comments

    Args:
        subject_type (CommentsListSubjectType): What the comment thread hangs off, which decides
            how `subjectId` is interpreted.
        subject_id (str): The subject's id, interpreted according to `subjectType`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Comment]
    """

    return sync_detailed(
        client=client,
        subject_type=subject_type,
        subject_id=subject_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    subject_type: CommentsListSubjectType,
    subject_id: str,
) -> Response[list[Comment]]:
    """List comments

    Args:
        subject_type (CommentsListSubjectType): What the comment thread hangs off, which decides
            how `subjectId` is interpreted.
        subject_id (str): The subject's id, interpreted according to `subjectType`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Comment]]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        subject_id=subject_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    subject_type: CommentsListSubjectType,
    subject_id: str,
) -> list[Comment] | None:
    """List comments

    Args:
        subject_type (CommentsListSubjectType): What the comment thread hangs off, which decides
            how `subjectId` is interpreted.
        subject_id (str): The subject's id, interpreted according to `subjectType`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Comment]
    """

    return (
        await asyncio_detailed(
            client=client,
            subject_type=subject_type,
            subject_id=subject_id,
        )
    ).parsed
