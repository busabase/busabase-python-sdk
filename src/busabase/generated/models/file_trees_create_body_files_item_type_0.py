from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileTreesCreateBodyFilesItemType0")


@_attrs_define
class FileTreesCreateBodyFilesItemType0:
    """
    Attributes:
        path (str):
        asset_id (str):
        display_name (str | Unset):
        mime_type (str | Unset):
    """

    path: str
    asset_id: str
    display_name: str | Unset = UNSET
    mime_type: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        asset_id = self.asset_id

        display_name = self.display_name

        mime_type = self.mime_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "path": path,
                "assetId": asset_id,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        path = d.pop("path")

        asset_id = d.pop("assetId")

        display_name = d.pop("displayName", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        file_trees_create_body_files_item_type_0 = cls(
            path=path,
            asset_id=asset_id,
            display_name=display_name,
            mime_type=mime_type,
        )

        return file_trees_create_body_files_item_type_0
