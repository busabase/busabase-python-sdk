from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.file_trees_create_change_request_body_operations_item_type_0_kind import (
    FileTreesCreateChangeRequestBodyOperationsItemType0Kind,
    check_file_trees_create_change_request_body_operations_item_type_0_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileTreesCreateChangeRequestBodyOperationsItemType0")


@_attrs_define
class FileTreesCreateChangeRequestBodyOperationsItemType0:
    """
    Attributes:
        kind (FileTreesCreateChangeRequestBodyOperationsItemType0Kind):
        path (str):
        asset_id (str):
        display_name (str | Unset):
        mime_type (str | Unset):
        base_content_hash (str | Unset): Optimistic-concurrency baseline hash of the file's current content, formatted
            exactly as `sha256:<64 lowercase hex characters>` (matches the `contentHash` on the file's backing Asset). Omit
            to skip the conflict check.
    """

    kind: FileTreesCreateChangeRequestBodyOperationsItemType0Kind
    path: str
    asset_id: str
    display_name: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    base_content_hash: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        path = self.path

        asset_id = self.asset_id

        display_name = self.display_name

        mime_type = self.mime_type

        base_content_hash = self.base_content_hash

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "path": path,
                "assetId": asset_id,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if base_content_hash is not UNSET:
            field_dict["baseContentHash"] = base_content_hash

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_file_trees_create_change_request_body_operations_item_type_0_kind(d.pop("kind"))

        path = d.pop("path")

        asset_id = d.pop("assetId")

        display_name = d.pop("displayName", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        base_content_hash = d.pop("baseContentHash", UNSET)

        file_trees_create_change_request_body_operations_item_type_0 = cls(
            kind=kind,
            path=path,
            asset_id=asset_id,
            display_name=display_name,
            mime_type=mime_type,
            base_content_hash=base_content_hash,
        )

        return file_trees_create_change_request_body_operations_item_type_0
