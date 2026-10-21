from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_document_nodes_item_type_6_position import WorkflowDocumentNodesItemType6Position


T = TypeVar("T", bound="WorkflowDocumentNodesItemType6")


@_attrs_define
class WorkflowDocumentNodesItemType6:
    """
    Attributes:
        id (str):
        position (WorkflowDocumentNodesItemType6Position):
        label (str):
        kind (Literal['action']):
        description (str | Unset):  Default: ''.
        action_name (str | Unset):  Default: ''.
    """

    id: str
    position: WorkflowDocumentNodesItemType6Position
    label: str
    kind: Literal["action"]
    description: str | Unset = ""
    action_name: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position.to_dict()

        label = self.label

        kind = self.kind

        description = self.description

        action_name = self.action_name

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
        if action_name is not UNSET:
            field_dict["actionName"] = action_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_document_nodes_item_type_6_position import WorkflowDocumentNodesItemType6Position

        d = dict(src_dict)
        id = d.pop("id")

        position = WorkflowDocumentNodesItemType6Position.from_dict(d.pop("position"))

        label = d.pop("label")

        kind = cast(Literal["action"], d.pop("kind"))
        if kind != "action":
            raise ValueError(f"kind must match const 'action', got '{kind}'")

        description = d.pop("description", UNSET)

        action_name = d.pop("actionName", UNSET)

        workflow_document_nodes_item_type_6 = cls(
            id=id,
            position=position,
            label=label,
            kind=kind,
            description=description,
            action_name=action_name,
        )

        workflow_document_nodes_item_type_6.additional_properties = d
        return workflow_document_nodes_item_type_6

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
