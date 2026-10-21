from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_trees_create_change_request_body_operations_item_type_3_metadata_visibility import (
    FileTreesCreateChangeRequestBodyOperationsItemType3MetadataVisibility,
    check_file_trees_create_change_request_body_operations_item_type_3_metadata_visibility,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileTreesCreateChangeRequestBodyOperationsItemType3Metadata")


@_attrs_define
class FileTreesCreateChangeRequestBodyOperationsItemType3Metadata:
    """
    Attributes:
        entry_file (str | Unset):
        visibility (FileTreesCreateChangeRequestBodyOperationsItemType3MetadataVisibility | Unset):
        version (str | Unset):
    """

    entry_file: str | Unset = UNSET
    visibility: FileTreesCreateChangeRequestBodyOperationsItemType3MetadataVisibility | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry_file = self.entry_file

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry_file is not UNSET:
            field_dict["entryFile"] = entry_file
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        entry_file = d.pop("entryFile", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: FileTreesCreateChangeRequestBodyOperationsItemType3MetadataVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = check_file_trees_create_change_request_body_operations_item_type_3_metadata_visibility(
                _visibility
            )

        version = d.pop("version", UNSET)

        file_trees_create_change_request_body_operations_item_type_3_metadata = cls(
            entry_file=entry_file,
            visibility=visibility,
            version=version,
        )

        file_trees_create_change_request_body_operations_item_type_3_metadata.additional_properties = d
        return file_trees_create_change_request_body_operations_item_type_3_metadata

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
