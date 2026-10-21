from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_trees_create_body_merge_mode import (
    FileTreesCreateBodyMergeMode,
    check_file_trees_create_body_merge_mode,
)
from ..models.file_trees_create_body_type import FileTreesCreateBodyType, check_file_trees_create_body_type
from ..models.file_trees_create_body_visibility import (
    FileTreesCreateBodyVisibility,
    check_file_trees_create_body_visibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_file_input import AssetFileInput
    from ..models.file_trees_create_body_metadata import FileTreesCreateBodyMetadata
    from ..models.text_file_input import TextFileInput


T = TypeVar("T", bound="FileTreesCreateBody")


@_attrs_define
class FileTreesCreateBody:
    """
    Attributes:
        slug (str):
        name (str):
        type_ (FileTreesCreateBodyType):
        parent_node_id (str | Unset): Parent node id. Must be a folder or the space root; container-incapable node types
            (Base, Doc, AirApp, etc.) cannot hold children.
        description (str | Unset):  Default: ''.
        visibility (FileTreesCreateBodyVisibility | Unset):
        version (str | Unset):  Default: '0.1.0'.
        metadata (FileTreesCreateBodyMetadata | Unset):
        files (list[AssetFileInput | TextFileInput] | Unset):
        auto_merge (bool | Unset):
        merge_mode (FileTreesCreateBodyMergeMode | Unset):  Default: 'merge'.
    """

    slug: str
    name: str
    type_: FileTreesCreateBodyType
    parent_node_id: str | Unset = UNSET
    description: str | Unset = ""
    visibility: FileTreesCreateBodyVisibility | Unset = UNSET
    version: str | Unset = "0.1.0"
    metadata: FileTreesCreateBodyMetadata | Unset = UNSET
    files: list[AssetFileInput | TextFileInput] | Unset = UNSET
    auto_merge: bool | Unset = UNSET
    merge_mode: FileTreesCreateBodyMergeMode | Unset = "merge"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_file_input import AssetFileInput

        slug = self.slug

        name = self.name

        type_: str = self.type_

        parent_node_id = self.parent_node_id

        description = self.description

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility

        version = self.version

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item: dict[str, Any]
                if isinstance(files_item_data, AssetFileInput):
                    files_item = files_item_data.to_dict()
                else:
                    files_item = files_item_data.to_dict()

                files.append(files_item)

        auto_merge = self.auto_merge

        merge_mode: str | Unset = UNSET
        if not isinstance(self.merge_mode, Unset):
            merge_mode = self.merge_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "name": name,
                "type": type_,
            }
        )
        if parent_node_id is not UNSET:
            field_dict["parentNodeId"] = parent_node_id
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if version is not UNSET:
            field_dict["version"] = version
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if files is not UNSET:
            field_dict["files"] = files
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge
        if merge_mode is not UNSET:
            field_dict["mergeMode"] = merge_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.asset_file_input import AssetFileInput
        from ..models.file_trees_create_body_metadata import FileTreesCreateBodyMetadata
        from ..models.text_file_input import TextFileInput

        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        type_ = check_file_trees_create_body_type(d.pop("type"))

        parent_node_id = d.pop("parentNodeId", UNSET)

        description = d.pop("description", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: FileTreesCreateBodyVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = check_file_trees_create_body_visibility(_visibility)

        version = d.pop("version", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: FileTreesCreateBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = FileTreesCreateBodyMetadata.from_dict(_metadata)

        _files = d.pop("files", UNSET)
        files: list[AssetFileInput | TextFileInput] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:

                def _parse_files_item(data: object) -> AssetFileInput | TextFileInput:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        files_item_type_0 = AssetFileInput.from_dict(data)

                        return files_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    files_item_type_1 = TextFileInput.from_dict(data)

                    return files_item_type_1

                files_item = _parse_files_item(files_item_data)

                files.append(files_item)

        auto_merge = d.pop("autoMerge", UNSET)

        _merge_mode = d.pop("mergeMode", UNSET)
        merge_mode: FileTreesCreateBodyMergeMode | Unset
        if isinstance(_merge_mode, Unset):
            merge_mode = UNSET
        else:
            merge_mode = check_file_trees_create_body_merge_mode(_merge_mode)

        file_trees_create_body = cls(
            slug=slug,
            name=name,
            type_=type_,
            parent_node_id=parent_node_id,
            description=description,
            visibility=visibility,
            version=version,
            metadata=metadata,
            files=files,
            auto_merge=auto_merge,
            merge_mode=merge_mode,
        )

        file_trees_create_body.additional_properties = d
        return file_trees_create_body

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
