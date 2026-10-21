from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GrepMatchOwner")


@_attrs_define
class GrepMatchOwner:
    """
    Attributes:
        node_id (str):
        node_type (str):
        node_name (str):
        path (list[str]):
    """

    node_id: str
    node_type: str
    node_name: str
    path: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        node_type = self.node_type

        node_name = self.node_name

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeId": node_id,
                "nodeType": node_type,
                "nodeName": node_name,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        node_id = d.pop("nodeId")

        node_type = d.pop("nodeType")

        node_name = d.pop("nodeName")

        path = cast(list[str], d.pop("path"))

        grep_match_owner = cls(
            node_id=node_id,
            node_type=node_type,
            node_name=node_name,
            path=path,
        )

        grep_match_owner.additional_properties = d
        return grep_match_owner

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
