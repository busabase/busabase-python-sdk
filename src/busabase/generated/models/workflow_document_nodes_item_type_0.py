from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_document_nodes_item_type_0_position import WorkflowDocumentNodesItemType0Position


T = TypeVar("T", bound="WorkflowDocumentNodesItemType0")


@_attrs_define
class WorkflowDocumentNodesItemType0:
    """
    Attributes:
        id (str):
        position (WorkflowDocumentNodesItemType0Position):
        label (str):
        kind (Literal['trigger']):
        description (str | Unset):  Default: ''.
        event_name (str | Unset):  Default: 'manual'.
    """

    id: str
    position: WorkflowDocumentNodesItemType0Position
    label: str
    kind: Literal["trigger"]
    description: str | Unset = ""
    event_name: str | Unset = "manual"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position.to_dict()

        label = self.label

        kind = self.kind

        description = self.description

        event_name = self.event_name

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
        if event_name is not UNSET:
            field_dict["eventName"] = event_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_document_nodes_item_type_0_position import WorkflowDocumentNodesItemType0Position

        d = dict(src_dict)
        id = d.pop("id")

        position = WorkflowDocumentNodesItemType0Position.from_dict(d.pop("position"))

        label = d.pop("label")

        kind = cast(Literal["trigger"], d.pop("kind"))
        if kind != "trigger":
            raise ValueError(f"kind must match const 'trigger', got '{kind}'")

        description = d.pop("description", UNSET)

        event_name = d.pop("eventName", UNSET)

        workflow_document_nodes_item_type_0 = cls(
            id=id,
            position=position,
            label=label,
            kind=kind,
            description=description,
            event_name=event_name,
        )

        workflow_document_nodes_item_type_0.additional_properties = d
        return workflow_document_nodes_item_type_0

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
