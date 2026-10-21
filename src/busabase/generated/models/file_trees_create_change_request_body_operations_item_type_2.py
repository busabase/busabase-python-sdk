from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileTreesCreateChangeRequestBodyOperationsItemType2")


@_attrs_define
class FileTreesCreateChangeRequestBodyOperationsItemType2:
    """
    Attributes:
        kind (Literal['delete']):
        path (str):
        base_content_hash (str | Unset): Optimistic-concurrency baseline hash of the file's current content, formatted
            exactly as `sha256:<64 lowercase hex characters>` (matches the `contentHash` on the file's backing Asset). Omit
            to skip the conflict check.
    """

    kind: Literal["delete"]
    path: str
    base_content_hash: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        path = self.path

        base_content_hash = self.base_content_hash

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "path": path,
            }
        )
        if base_content_hash is not UNSET:
            field_dict["baseContentHash"] = base_content_hash

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = cast(Literal["delete"], d.pop("kind"))
        if kind != "delete":
            raise ValueError(f"kind must match const 'delete', got '{kind}'")

        path = d.pop("path")

        base_content_hash = d.pop("baseContentHash", UNSET)

        file_trees_create_change_request_body_operations_item_type_2 = cls(
            kind=kind,
            path=path,
            base_content_hash=base_content_hash,
        )

        return file_trees_create_change_request_body_operations_item_type_2
