from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_node_position import WorkflowNodePosition


T = TypeVar("T", bound="ApprovalWorkflowNode")


@_attrs_define
class ApprovalWorkflowNode:
    """
    Attributes:
        id (str):
        position (WorkflowNodePosition):
        label (str):
        kind (Literal['approval']):
        description (str | Unset):  Default: ''.
        approver (str | Unset):  Default: ''.
    """

    id: str
    position: WorkflowNodePosition
    label: str
    kind: Literal["approval"]
    description: str | Unset = ""
    approver: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position.to_dict()

        label = self.label

        kind = self.kind

        description = self.description

        approver = self.approver

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "position": position,
                "label": label,
                "kind": kind,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if approver is not UNSET:
            field_dict["approver"] = approver

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_node_position import WorkflowNodePosition

        d = dict(src_dict)
        id = d.pop("id")

        position = WorkflowNodePosition.from_dict(d.pop("position"))

        label = d.pop("label")

        kind = cast(Literal["approval"], d.pop("kind"))
        if kind != "approval":
            raise ValueError(f"kind must match const 'approval', got '{kind}'")

        description = d.pop("description", UNSET)

        approver = d.pop("approver", UNSET)

        approval_workflow_node = cls(
            id=id,
            position=position,
            label=label,
            kind=kind,
            description=description,
            approver=approver,
        )

        approval_workflow_node.additional_properties = d
        return approval_workflow_node

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
