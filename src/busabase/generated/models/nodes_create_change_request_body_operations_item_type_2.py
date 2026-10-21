from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NodesCreateChangeRequestBodyOperationsItemType2")


@_attrs_define
class NodesCreateChangeRequestBodyOperationsItemType2:
    """
    Attributes:
        kind (Literal['delete']):
        node_id (str):
    """

    kind: Literal["delete"]
    node_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        node_id = self.node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "nodeId": node_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = cast(Literal["delete"], d.pop("kind"))
        if kind != "delete":
            raise ValueError(f"kind must match const 'delete', got '{kind}'")

        node_id = d.pop("nodeId")

        nodes_create_change_request_body_operations_item_type_2 = cls(
            kind=kind,
            node_id=node_id,
        )

        nodes_create_change_request_body_operations_item_type_2.additional_properties = d
        return nodes_create_change_request_body_operations_item_type_2

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
