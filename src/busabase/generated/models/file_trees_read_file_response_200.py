from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_trees_read_file_response_200_encoding import (
    FileTreesReadFileResponse200Encoding,
    check_file_trees_read_file_response_200_encoding,
)

T = TypeVar("T", bound="FileTreesReadFileResponse200")


@_attrs_define
class FileTreesReadFileResponse200:
    """
    Attributes:
        node_id (str):
        path (str):
        encoding (FileTreesReadFileResponse200Encoding):
        content (str):
        mime_type (str):
        asset_id (str):
        display_name (None | str):
        asset_url (None | str):
        content_hash (str):
    """

    node_id: str
    path: str
    encoding: FileTreesReadFileResponse200Encoding
    content: str
    mime_type: str
    asset_id: str
    display_name: None | str
    asset_url: None | str
    content_hash: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        path = self.path

        encoding: str = self.encoding

        content = self.content

        mime_type = self.mime_type

        asset_id = self.asset_id

        display_name: None | str
        display_name = self.display_name

        asset_url: None | str
        asset_url = self.asset_url

        content_hash = self.content_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeId": node_id,
                "path": path,
                "encoding": encoding,
                "content": content,
                "mimeType": mime_type,
                "assetId": asset_id,
                "displayName": display_name,
                "assetUrl": asset_url,
                "contentHash": content_hash,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        node_id = d.pop("nodeId")

        path = d.pop("path")

        encoding = check_file_trees_read_file_response_200_encoding(d.pop("encoding"))

        content = d.pop("content")

        mime_type = d.pop("mimeType")

        asset_id = d.pop("assetId")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("displayName"))

        def _parse_asset_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        asset_url = _parse_asset_url(d.pop("assetUrl"))

        content_hash = d.pop("contentHash")

        file_trees_read_file_response_200 = cls(
            node_id=node_id,
            path=path,
            encoding=encoding,
            content=content,
            mime_type=mime_type,
            asset_id=asset_id,
            display_name=display_name,
            asset_url=asset_url,
            content_hash=content_hash,
        )

        file_trees_read_file_response_200.additional_properties = d
        return file_trees_read_file_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
