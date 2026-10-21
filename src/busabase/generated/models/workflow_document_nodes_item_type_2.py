from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_document_nodes_item_type_2_position import WorkflowDocumentNodesItemType2Position


T = TypeVar("T", bound="WorkflowDocumentNodesItemType2")


@_attrs_define
class WorkflowDocumentNodesItemType2:
    """
    Attributes:
        id (str):
        position (WorkflowDocumentNodesItemType2Position):
        label (str):
        kind (Literal['function']):
        description (str | Unset):  Default: ''.
        webhook_rule_id (str | Unset):  Default: ''.
        function_name (str | Unset):  Default: ''.
    """

    id: str
    position: WorkflowDocumentNodesItemType2Position
    label: str
    kind: Literal["function"]
    description: str | Unset = ""
    webhook_rule_id: str | Unset = ""
    function_name: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position.to_dict()

        label = self.label

        kind = self.kind

        description = self.description

        webhook_rule_id = self.webhook_rule_id

        function_name = self.function_name

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
        if webhook_rule_id is not UNSET:
            field_dict["webhookRuleId"] = webhook_rule_id
        if function_name is not UNSET:
            field_dict["functionName"] = function_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_document_nodes_item_type_2_position import WorkflowDocumentNodesItemType2Position

        d = dict(src_dict)
        id = d.pop("id")

        position = WorkflowDocumentNodesItemType2Position.from_dict(d.pop("position"))

        label = d.pop("label")

        kind = cast(Literal["function"], d.pop("kind"))
        if kind != "function":
            raise ValueError(f"kind must match const 'function', got '{kind}'")

        description = d.pop("description", UNSET)

        webhook_rule_id = d.pop("webhookRuleId", UNSET)

        function_name = d.pop("functionName", UNSET)

        workflow_document_nodes_item_type_2 = cls(
            id=id,
            position=position,
            label=label,
            kind=kind,
            description=description,
            webhook_rule_id=webhook_rule_id,
            function_name=function_name,
        )

        workflow_document_nodes_item_type_2.additional_properties = d
        return workflow_document_nodes_item_type_2

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
