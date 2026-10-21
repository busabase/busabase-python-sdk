from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodesMoveBody")


@_attrs_define
class NodesMoveBody:
    """
    Attributes:
        parent_node_id (str | Unset): New parent folder node id. Omit to keep the current parent and only reorder.
        position (int | Unset): New position among the target parent's children.
        message (str | Unset): Reviewer-facing Change Request message.
        submitted_by (str | Unset):
    """

    parent_node_id: str | Unset = UNSET
    position: int | Unset = UNSET
    message: str | Unset = UNSET
    submitted_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_node_id = self.parent_node_id

        position = self.position

        message = self.message

        submitted_by = self.submitted_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_node_id is not UNSET:
            field_dict["parentNodeId"] = parent_node_id
        if position is not UNSET:
            field_dict["position"] = position
        if message is not UNSET:
            field_dict["message"] = message
        if submitted_by is not UNSET:
            field_dict["submittedBy"] = submitted_by

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        parent_node_id = d.pop("parentNodeId", UNSET)

        position = d.pop("position", UNSET)

        message = d.pop("message", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        nodes_move_body = cls(
            parent_node_id=parent_node_id,
            position=position,
            message=message,
            submitted_by=submitted_by,
        )

        nodes_move_body.additional_properties = d
        return nodes_move_body

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
