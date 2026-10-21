from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_tree_metadata_operation_metadata import FileTreeMetadataOperationMetadata


T = TypeVar("T", bound="FileTreeMetadataOperation")


@_attrs_define
class FileTreeMetadataOperation:
    """
    Attributes:
        kind (Literal['metadata_update']):
        metadata (FileTreeMetadataOperationMetadata | Unset):
    """

    kind: Literal["metadata_update"]
    metadata: FileTreeMetadataOperationMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.file_tree_metadata_operation_metadata import FileTreeMetadataOperationMetadata

        d = dict(src_dict)
        kind = cast(Literal["metadata_update"], d.pop("kind"))
        if kind != "metadata_update":
            raise ValueError(f"kind must match const 'metadata_update', got '{kind}'")

        _metadata = d.pop("metadata", UNSET)
        metadata: FileTreeMetadataOperationMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = FileTreeMetadataOperationMetadata.from_dict(_metadata)

        file_tree_metadata_operation = cls(
            kind=kind,
            metadata=metadata,
        )

        return file_tree_metadata_operation
