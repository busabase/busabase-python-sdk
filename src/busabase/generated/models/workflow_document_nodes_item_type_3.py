from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_document_nodes_item_type_3_position import WorkflowDocumentNodesItemType3Position


T = TypeVar("T", bound="WorkflowDocumentNodesItemType3")


@_attrs_define
class WorkflowDocumentNodesItemType3:
    """
    Attributes:
        id (str):
        position (WorkflowDocumentNodesItemType3Position):
        label (str):
        kind (Literal['condition']):
        description (str | Unset):  Default: ''.
        expression (str | Unset):  Default: ''.
    """

    id: str
    position: WorkflowDocumentNodesItemType3Position
    label: str
    kind: Literal["condition"]
    description: str | Unset = ""
    expression: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position.to_dict()

        label = self.label

        kind = self.kind

        description = self.description

        expression = self.expression

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
        if expression is not UNSET:
            field_dict["expression"] = expression

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_document_nodes_item_type_3_position import WorkflowDocumentNodesItemType3Position

        d = dict(src_dict)
        id = d.pop("id")

        position = WorkflowDocumentNodesItemType3Position.from_dict(d.pop("position"))

        label = d.pop("label")

        kind = cast(Literal["condition"], d.pop("kind"))
        if kind != "condition":
            raise ValueError(f"kind must match const 'condition', got '{kind}'")

        description = d.pop("description", UNSET)

        expression = d.pop("expression", UNSET)

        workflow_document_nodes_item_type_3 = cls(
            id=id,
            position=position,
            label=label,
            kind=kind,
            description=description,
            expression=expression,
        )

        workflow_document_nodes_item_type_3.additional_properties = d
        return workflow_document_nodes_item_type_3

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
