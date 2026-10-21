from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_document_nodes_item_type_7_position import WorkflowDocumentNodesItemType7Position


T = TypeVar("T", bound="WorkflowDocumentNodesItemType7")


@_attrs_define
class WorkflowDocumentNodesItemType7:
    """
    Attributes:
        id (str):
        position (WorkflowDocumentNodesItemType7Position):
        label (str):
        kind (Literal['end']):
        description (str | Unset):  Default: ''.
        outcome (str | Unset):  Default: 'completed'.
    """

    id: str
    position: WorkflowDocumentNodesItemType7Position
    label: str
    kind: Literal["end"]
    description: str | Unset = ""
    outcome: str | Unset = "completed"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position.to_dict()

        label = self.label

        kind = self.kind

        description = self.description

        outcome = self.outcome

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
        if outcome is not UNSET:
            field_dict["outcome"] = outcome

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_document_nodes_item_type_7_position import WorkflowDocumentNodesItemType7Position

        d = dict(src_dict)
        id = d.pop("id")

        position = WorkflowDocumentNodesItemType7Position.from_dict(d.pop("position"))

        label = d.pop("label")

        kind = cast(Literal["end"], d.pop("kind"))
        if kind != "end":
            raise ValueError(f"kind must match const 'end', got '{kind}'")

        description = d.pop("description", UNSET)

        outcome = d.pop("outcome", UNSET)

        workflow_document_nodes_item_type_7 = cls(
            id=id,
            position=position,
            label=label,
            kind=kind,
            description=description,
            outcome=outcome,
        )

        workflow_document_nodes_item_type_7.additional_properties = d
        return workflow_document_nodes_item_type_7

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
