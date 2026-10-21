from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grep_body_scope_nodes_types_item import (
    GrepBodyScopeNodesTypesItem,
    check_grep_body_scope_nodes_types_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GrepBodyScopeNodes")


@_attrs_define
class GrepBodyScopeNodes:
    """
    Attributes:
        node_ids (list[str] | Unset):
        types (list[GrepBodyScopeNodesTypesItem] | Unset):
    """

    node_ids: list[str] | Unset = UNSET
    types: list[GrepBodyScopeNodesTypesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_ids: list[str] | Unset = UNSET
        if not isinstance(self.node_ids, Unset):
            node_ids = self.node_ids

        types: list[str] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item: str = types_item_data
                types.append(types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_ids is not UNSET:
            field_dict["nodeIds"] = node_ids
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        node_ids = cast(list[str], d.pop("nodeIds", UNSET))

        _types = d.pop("types", UNSET)
        types: list[GrepBodyScopeNodesTypesItem] | Unset = UNSET
        if _types is not UNSET:
            types = []
            for types_item_data in _types:
                types_item = check_grep_body_scope_nodes_types_item(types_item_data)

                types.append(types_item)

        grep_body_scope_nodes = cls(
            node_ids=node_ids,
            types=types,
        )

        grep_body_scope_nodes.additional_properties = d
        return grep_body_scope_nodes

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
