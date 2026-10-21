from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveNodeOperation")


@_attrs_define
class MoveNodeOperation:
    """
    Attributes:
        kind (Literal['move']):
        node_id (str):
        parent_node_id (str | Unset):
        parent_node_ref (str | Unset):
        position (int | Unset):
    """

    kind: Literal["move"]
    node_id: str
    parent_node_id: str | Unset = UNSET
    parent_node_ref: str | Unset = UNSET
    position: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        node_id = self.node_id

        parent_node_id = self.parent_node_id

        parent_node_ref = self.parent_node_ref

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "nodeId": node_id,
            }
        )
        if parent_node_id is not UNSET:
            field_dict["parentNodeId"] = parent_node_id
        if parent_node_ref is not UNSET:
            field_dict["parentNodeRef"] = parent_node_ref
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = cast(Literal["move"], d.pop("kind"))
        if kind != "move":
            raise ValueError(f"kind must match const 'move', got '{kind}'")

        node_id = d.pop("nodeId")

        parent_node_id = d.pop("parentNodeId", UNSET)

        parent_node_ref = d.pop("parentNodeRef", UNSET)

        position = d.pop("position", UNSET)

        move_node_operation = cls(
            kind=kind,
            node_id=node_id,
            parent_node_id=parent_node_id,
            parent_node_ref=parent_node_ref,
            position=position,
        )

        move_node_operation.additional_properties = d
        return move_node_operation

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
