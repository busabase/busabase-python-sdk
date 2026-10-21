from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_document_nodes_item_type_1_method import (
    WorkflowDocumentNodesItemType1Method,
    check_workflow_document_nodes_item_type_1_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_document_nodes_item_type_1_position import WorkflowDocumentNodesItemType1Position


T = TypeVar("T", bound="WorkflowDocumentNodesItemType1")


@_attrs_define
class WorkflowDocumentNodesItemType1:
    """
    Attributes:
        id (str):
        position (WorkflowDocumentNodesItemType1Position):
        label (str):
        kind (Literal['webhook']):
        description (str | Unset):  Default: ''.
        method (WorkflowDocumentNodesItemType1Method | Unset):  Default: 'POST'.
        url (str | Unset):  Default: ''.
    """

    id: str
    position: WorkflowDocumentNodesItemType1Position
    label: str
    kind: Literal["webhook"]
    description: str | Unset = ""
    method: WorkflowDocumentNodesItemType1Method | Unset = "POST"
    url: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position.to_dict()

        label = self.label

        kind = self.kind

        description = self.description

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method

        url = self.url

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
        if method is not UNSET:
            field_dict["method"] = method
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_document_nodes_item_type_1_position import WorkflowDocumentNodesItemType1Position

        d = dict(src_dict)
        id = d.pop("id")

        position = WorkflowDocumentNodesItemType1Position.from_dict(d.pop("position"))

        label = d.pop("label")

        kind = cast(Literal["webhook"], d.pop("kind"))
        if kind != "webhook":
            raise ValueError(f"kind must match const 'webhook', got '{kind}'")

        description = d.pop("description", UNSET)

        _method = d.pop("method", UNSET)
        method: WorkflowDocumentNodesItemType1Method | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = check_workflow_document_nodes_item_type_1_method(_method)

        url = d.pop("url", UNSET)

        workflow_document_nodes_item_type_1 = cls(
            id=id,
            position=position,
            label=label,
            kind=kind,
            description=description,
            method=method,
            url=url,
        )

        workflow_document_nodes_item_type_1.additional_properties = d
        return workflow_document_nodes_item_type_1

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
