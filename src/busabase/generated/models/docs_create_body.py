from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocsCreateBody")


@_attrs_define
class DocsCreateBody:
    """
    Attributes:
        slug (str):
        name (str):
        parent_node_id (str | Unset): Parent folder: a node id or a folder slug (default: the space root). Must be a
            folder or the space root; container-incapable node types (Base, Doc, AirApp, etc.) cannot hold children.
        description (str | Unset):  Default: ''.
        body (str | Unset):  Default: ''.
        auto_merge (bool | Unset):
    """

    slug: str
    name: str
    parent_node_id: str | Unset = UNSET
    description: str | Unset = ""
    body: str | Unset = ""
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        parent_node_id = self.parent_node_id

        description = self.description

        body = self.body

        auto_merge = self.auto_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "name": name,
            }
        )
        if parent_node_id is not UNSET:
            field_dict["parentNodeId"] = parent_node_id
        if description is not UNSET:
            field_dict["description"] = description
        if body is not UNSET:
            field_dict["body"] = body
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        parent_node_id = d.pop("parentNodeId", UNSET)

        description = d.pop("description", UNSET)

        body = d.pop("body", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        docs_create_body = cls(
            slug=slug,
            name=name,
            parent_node_id=parent_node_id,
            description=description,
            body=body,
            auto_merge=auto_merge,
        )

        docs_create_body.additional_properties = d
        return docs_create_body

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
