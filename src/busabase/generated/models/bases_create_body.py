from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bases_create_body_fields_item import BasesCreateBodyFieldsItem


T = TypeVar("T", bound="BasesCreateBody")


@_attrs_define
class BasesCreateBody:
    """
    Attributes:
        slug (str):
        name (str):
        parent_node_id (str | Unset): Parent node id. Must be a folder or the space root; container-incapable node types
            (Base, Doc, AirApp, etc.) cannot hold children.
        description (str | Unset):  Default: ''.
        fields (list[BasesCreateBodyFieldsItem] | Unset):
        default_view (bool | Unset): Whether the new Base gets its default "Grid view" (a table view showing every
            record and field). Defaults to true. Pass false only when you add your own views right away — a Base must always
            keep at least one view, and the leftmost one is what it opens on.
        auto_merge (bool | Unset):
    """

    slug: str
    name: str
    parent_node_id: str | Unset = UNSET
    description: str | Unset = ""
    fields: list[BasesCreateBodyFieldsItem] | Unset = UNSET
    default_view: bool | Unset = UNSET
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        parent_node_id = self.parent_node_id

        description = self.description

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        default_view = self.default_view

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
        if fields is not UNSET:
            field_dict["fields"] = fields
        if default_view is not UNSET:
            field_dict["defaultView"] = default_view
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bases_create_body_fields_item import BasesCreateBodyFieldsItem

        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        parent_node_id = d.pop("parentNodeId", UNSET)

        description = d.pop("description", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[BasesCreateBodyFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = BasesCreateBodyFieldsItem.from_dict(fields_item_data)

                fields.append(fields_item)

        default_view = d.pop("defaultView", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        bases_create_body = cls(
            slug=slug,
            name=name,
            parent_node_id=parent_node_id,
            description=description,
            fields=fields,
            default_view=default_view,
            auto_merge=auto_merge,
        )

        bases_create_body.additional_properties = d
        return bases_create_body

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
