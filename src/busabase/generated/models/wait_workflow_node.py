from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wait_workflow_node_unit import WaitWorkflowNodeUnit, check_wait_workflow_node_unit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_node_position import WorkflowNodePosition


T = TypeVar("T", bound="WaitWorkflowNode")


@_attrs_define
class WaitWorkflowNode:
    """
    Attributes:
        id (str):
        position (WorkflowNodePosition):
        label (str):
        kind (Literal['wait']):
        description (str | Unset):  Default: ''.
        duration (int | Unset):  Default: 1.
        unit (WaitWorkflowNodeUnit | Unset):  Default: 'hours'.
    """

    id: str
    position: WorkflowNodePosition
    label: str
    kind: Literal["wait"]
    description: str | Unset = ""
    duration: int | Unset = 1
    unit: WaitWorkflowNodeUnit | Unset = "hours"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position.to_dict()

        label = self.label

        kind = self.kind

        description = self.description

        duration = self.duration

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit

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
        if duration is not UNSET:
            field_dict["duration"] = duration
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_node_position import WorkflowNodePosition

        d = dict(src_dict)
        id = d.pop("id")

        position = WorkflowNodePosition.from_dict(d.pop("position"))

        label = d.pop("label")

        kind = cast(Literal["wait"], d.pop("kind"))
        if kind != "wait":
            raise ValueError(f"kind must match const 'wait', got '{kind}'")

        description = d.pop("description", UNSET)

        duration = d.pop("duration", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: WaitWorkflowNodeUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = check_wait_workflow_node_unit(_unit)

        wait_workflow_node = cls(
            id=id,
            position=position,
            label=label,
            kind=kind,
            description=description,
            duration=duration,
            unit=unit,
        )

        wait_workflow_node.additional_properties = d
        return wait_workflow_node

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
