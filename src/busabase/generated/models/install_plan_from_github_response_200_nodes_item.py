from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.install_plan_from_github_response_200_nodes_item_type import (
    InstallPlanFromGithubResponse200NodesItemType,
    check_install_plan_from_github_response_200_nodes_item_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstallPlanFromGithubResponse200NodesItem")


@_attrs_define
class InstallPlanFromGithubResponse200NodesItem:
    """
    Attributes:
        path (str):
        slug (str):
        name (str):
        type_ (InstallPlanFromGithubResponse200NodesItemType):
        depth (int):
        field_count (int | Unset):
        record_count (int | Unset):
        file_count (int | Unset):
    """

    path: str
    slug: str
    name: str
    type_: InstallPlanFromGithubResponse200NodesItemType
    depth: int
    field_count: int | Unset = UNSET
    record_count: int | Unset = UNSET
    file_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        slug = self.slug

        name = self.name

        type_: str = self.type_

        depth = self.depth

        field_count = self.field_count

        record_count = self.record_count

        file_count = self.file_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "slug": slug,
                "name": name,
                "type": type_,
                "depth": depth,
            }
        )
        if field_count is not UNSET:
            field_dict["fieldCount"] = field_count
        if record_count is not UNSET:
            field_dict["recordCount"] = record_count
        if file_count is not UNSET:
            field_dict["fileCount"] = file_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        path = d.pop("path")

        slug = d.pop("slug")

        name = d.pop("name")

        type_ = check_install_plan_from_github_response_200_nodes_item_type(d.pop("type"))

        depth = d.pop("depth")

        field_count = d.pop("fieldCount", UNSET)

        record_count = d.pop("recordCount", UNSET)

        file_count = d.pop("fileCount", UNSET)

        install_plan_from_github_response_200_nodes_item = cls(
            path=path,
            slug=slug,
            name=name,
            type_=type_,
            depth=depth,
            field_count=field_count,
            record_count=record_count,
            file_count=file_count,
        )

        install_plan_from_github_response_200_nodes_item.additional_properties = d
        return install_plan_from_github_response_200_nodes_item

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
