from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.air_app_node_detail import AirAppNodeDetail
from ...models.base_node_detail import BaseNodeDetail
from ...models.doc_node_detail import DocNodeDetail
from ...models.drive_node_detail import DriveNodeDetail
from ...models.file_node_detail import FileNodeDetail
from ...models.folder_node_detail import FolderNodeDetail
from ...models.form_node_detail import FormNodeDetail
from ...models.html_node_detail import HtmlNodeDetail
from ...models.nodes_get_type import NodesGetType
from ...models.skill_node_detail import SkillNodeDetail
from ...models.whiteboard_node_detail import WhiteboardNodeDetail
from ...models.workflow_node_detail import WorkflowNodeDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    type_: NodesGetType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/nodes/{node_id}".format(
            node_id=quote(str(node_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AirAppNodeDetail
    | BaseNodeDetail
    | DocNodeDetail
    | DriveNodeDetail
    | FileNodeDetail
    | FolderNodeDetail
    | FormNodeDetail
    | HtmlNodeDetail
    | SkillNodeDetail
    | WhiteboardNodeDetail
    | WorkflowNodeDetail
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            AirAppNodeDetail
            | BaseNodeDetail
            | DocNodeDetail
            | DriveNodeDetail
            | FileNodeDetail
            | FolderNodeDetail
            | FormNodeDetail
            | HtmlNodeDetail
            | SkillNodeDetail
            | WhiteboardNodeDetail
            | WorkflowNodeDetail
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_detail_type_0 = FolderNodeDetail.from_dict(data)

                return componentsschemas_node_detail_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_detail_type_1 = DocNodeDetail.from_dict(data)

                return componentsschemas_node_detail_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_detail_type_2 = FileNodeDetail.from_dict(data)

                return componentsschemas_node_detail_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_detail_type_3 = SkillNodeDetail.from_dict(data)

                return componentsschemas_node_detail_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_detail_type_4 = DriveNodeDetail.from_dict(data)

                return componentsschemas_node_detail_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_detail_type_5 = AirAppNodeDetail.from_dict(data)

                return componentsschemas_node_detail_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_detail_type_6 = BaseNodeDetail.from_dict(data)

                return componentsschemas_node_detail_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_detail_type_7 = FormNodeDetail.from_dict(data)

                return componentsschemas_node_detail_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_detail_type_8 = WhiteboardNodeDetail.from_dict(data)

                return componentsschemas_node_detail_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_detail_type_9 = WorkflowNodeDetail.from_dict(data)

                return componentsschemas_node_detail_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_node_detail_type_10 = HtmlNodeDetail.from_dict(data)

            return componentsschemas_node_detail_type_10

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AirAppNodeDetail
    | BaseNodeDetail
    | DocNodeDetail
    | DriveNodeDetail
    | FileNodeDetail
    | FolderNodeDetail
    | FormNodeDetail
    | HtmlNodeDetail
    | SkillNodeDetail
    | WhiteboardNodeDetail
    | WorkflowNodeDetail
]:
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
    type_: NodesGetType | Unset = UNSET,
) -> Response[
    AirAppNodeDetail
    | BaseNodeDetail
    | DocNodeDetail
    | DriveNodeDetail
    | FileNodeDetail
    | FolderNodeDetail
    | FormNodeDetail
    | HtmlNodeDetail
    | SkillNodeDetail
    | WhiteboardNodeDetail
    | WorkflowNodeDetail
]:
    """Get one node's typed detail

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesGetType | Unset): Optional disambiguation hint, only needed when `nodeId` is a
            slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirAppNodeDetail | BaseNodeDetail | DocNodeDetail | DriveNodeDetail | FileNodeDetail | FolderNodeDetail | FormNodeDetail | HtmlNodeDetail | SkillNodeDetail | WhiteboardNodeDetail | WorkflowNodeDetail]
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
    type_: NodesGetType | Unset = UNSET,
) -> (
    AirAppNodeDetail
    | BaseNodeDetail
    | DocNodeDetail
    | DriveNodeDetail
    | FileNodeDetail
    | FolderNodeDetail
    | FormNodeDetail
    | HtmlNodeDetail
    | SkillNodeDetail
    | WhiteboardNodeDetail
    | WorkflowNodeDetail
    | None
):
    """Get one node's typed detail

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesGetType | Unset): Optional disambiguation hint, only needed when `nodeId` is a
            slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirAppNodeDetail | BaseNodeDetail | DocNodeDetail | DriveNodeDetail | FileNodeDetail | FolderNodeDetail | FormNodeDetail | HtmlNodeDetail | SkillNodeDetail | WhiteboardNodeDetail | WorkflowNodeDetail
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
    type_: NodesGetType | Unset = UNSET,
) -> Response[
    AirAppNodeDetail
    | BaseNodeDetail
    | DocNodeDetail
    | DriveNodeDetail
    | FileNodeDetail
    | FolderNodeDetail
    | FormNodeDetail
    | HtmlNodeDetail
    | SkillNodeDetail
    | WhiteboardNodeDetail
    | WorkflowNodeDetail
]:
    """Get one node's typed detail

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesGetType | Unset): Optional disambiguation hint, only needed when `nodeId` is a
            slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirAppNodeDetail | BaseNodeDetail | DocNodeDetail | DriveNodeDetail | FileNodeDetail | FolderNodeDetail | FormNodeDetail | HtmlNodeDetail | SkillNodeDetail | WhiteboardNodeDetail | WorkflowNodeDetail]
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
    type_: NodesGetType | Unset = UNSET,
) -> (
    AirAppNodeDetail
    | BaseNodeDetail
    | DocNodeDetail
    | DriveNodeDetail
    | FileNodeDetail
    | FolderNodeDetail
    | FormNodeDetail
    | HtmlNodeDetail
    | SkillNodeDetail
    | WhiteboardNodeDetail
    | WorkflowNodeDetail
    | None
):
    """Get one node's typed detail

    Args:
        node_id (str): Node id, or a slug that is unique within its type.
        type_ (NodesGetType | Unset): Optional disambiguation hint, only needed when `nodeId` is a
            slug that exists under more than one node type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirAppNodeDetail | BaseNodeDetail | DocNodeDetail | DriveNodeDetail | FileNodeDetail | FolderNodeDetail | FormNodeDetail | HtmlNodeDetail | SkillNodeDetail | WhiteboardNodeDetail | WorkflowNodeDetail
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            type_=type_,
        )
    ).parsed
