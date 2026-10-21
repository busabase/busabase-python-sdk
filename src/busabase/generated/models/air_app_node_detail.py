from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.air_app_node_detail_visibility import AirAppNodeDetailVisibility, check_air_app_node_detail_visibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_tree_file import FileTreeFile
    from ..models.node import Node


T = TypeVar("T", bound="AirAppNodeDetail")


@_attrs_define
class AirAppNodeDetail:
    """
    Attributes:
        node (Node):
        entry_file (str):
        visibility (AirAppNodeDetailVisibility):
        version (str):
        files (list[FileTreeFile]):
        type_ (Literal['airapp']):
        skipped_gitignore_paths (list[str] | Unset):
    """

    node: Node
    entry_file: str
    visibility: AirAppNodeDetailVisibility
    version: str
    files: list[FileTreeFile]
    type_: Literal["airapp"]
    skipped_gitignore_paths: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node = self.node.to_dict()

        entry_file = self.entry_file

        visibility: str = self.visibility

        version = self.version

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        type_ = self.type_

        skipped_gitignore_paths: list[str] | Unset = UNSET
        if not isinstance(self.skipped_gitignore_paths, Unset):
            skipped_gitignore_paths = self.skipped_gitignore_paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node": node,
                "entryFile": entry_file,
                "visibility": visibility,
                "version": version,
                "files": files,
                "type": type_,
            }
        )
        if skipped_gitignore_paths is not UNSET:
            field_dict["skippedGitignorePaths"] = skipped_gitignore_paths

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.file_tree_file import FileTreeFile
        from ..models.node import Node

        d = dict(src_dict)
        node = Node.from_dict(d.pop("node"))

        entry_file = d.pop("entryFile")

        visibility = check_air_app_node_detail_visibility(d.pop("visibility"))

        version = d.pop("version")

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = FileTreeFile.from_dict(files_item_data)

            files.append(files_item)

        type_ = cast(Literal["airapp"], d.pop("type"))
        if type_ != "airapp":
            raise ValueError(f"type must match const 'airapp', got '{type_}'")

        skipped_gitignore_paths = cast(list[str], d.pop("skippedGitignorePaths", UNSET))

        air_app_node_detail = cls(
            node=node,
            entry_file=entry_file,
            visibility=visibility,
            version=version,
            files=files,
            type_=type_,
            skipped_gitignore_paths=skipped_gitignore_paths,
        )

        air_app_node_detail.additional_properties = d
        return air_app_node_detail

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
