from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InstallFromGithubResponse200Created")


@_attrs_define
class InstallFromGithubResponse200Created:
    """
    Attributes:
        folders (int):
        docs (int):
        bases (int):
        views (int):
        records (int):
        file_tree_nodes (int):
        files (int):
    """

    folders: int
    docs: int
    bases: int
    views: int
    records: int
    file_tree_nodes: int
    files: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folders = self.folders

        docs = self.docs

        bases = self.bases

        views = self.views

        records = self.records

        file_tree_nodes = self.file_tree_nodes

        files = self.files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folders": folders,
                "docs": docs,
                "bases": bases,
                "views": views,
                "records": records,
                "fileTreeNodes": file_tree_nodes,
                "files": files,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        folders = d.pop("folders")

        docs = d.pop("docs")

        bases = d.pop("bases")

        views = d.pop("views")

        records = d.pop("records")

        file_tree_nodes = d.pop("fileTreeNodes")

        files = d.pop("files")

        install_from_github_response_200_created = cls(
            folders=folders,
            docs=docs,
            bases=bases,
            views=views,
            records=records,
            file_tree_nodes=file_tree_nodes,
            files=files,
        )

        install_from_github_response_200_created.additional_properties = d
        return install_from_github_response_200_created

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
