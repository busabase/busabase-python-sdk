from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.file_trees_create_change_request_body_operations_item_type_1_kind import (
    FileTreesCreateChangeRequestBodyOperationsItemType1Kind,
    check_file_trees_create_change_request_body_operations_item_type_1_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileTreesCreateChangeRequestBodyOperationsItemType1")


@_attrs_define
class FileTreesCreateChangeRequestBodyOperationsItemType1:
    """
    Attributes:
        kind (FileTreesCreateChangeRequestBodyOperationsItemType1Kind):
        path (str):
        content (str):
        mime_type (str | Unset):
        base_content_hash (str | Unset): Optimistic-concurrency baseline hash of the file's current content, formatted
            exactly as `sha256:<64 lowercase hex characters>` (matches the `contentHash` on the file's backing Asset). Omit
            to skip the conflict check.
    """

    kind: FileTreesCreateChangeRequestBodyOperationsItemType1Kind
    path: str
    content: str
    mime_type: str | Unset = UNSET
    base_content_hash: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        path = self.path

        content = self.content

        mime_type = self.mime_type

        base_content_hash = self.base_content_hash

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "path": path,
                "content": content,
            }
        )
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if base_content_hash is not UNSET:
            field_dict["baseContentHash"] = base_content_hash

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_file_trees_create_change_request_body_operations_item_type_1_kind(d.pop("kind"))

        path = d.pop("path")

        content = d.pop("content")

        mime_type = d.pop("mimeType", UNSET)

        base_content_hash = d.pop("baseContentHash", UNSET)

        file_trees_create_change_request_body_operations_item_type_1 = cls(
            kind=kind,
            path=path,
            content=content,
            mime_type=mime_type,
            base_content_hash=base_content_hash,
        )

        return file_trees_create_change_request_body_operations_item_type_1
