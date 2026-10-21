from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowDocumentEdgesItem")


@_attrs_define
class WorkflowDocumentEdgesItem:
    """
    Attributes:
        id (str):
        source (str):
        target (str):
        label (str | Unset):  Default: ''.
        outcome (str | Unset):  Default: 'default'.
    """

    id: str
    source: str
    target: str
    label: str | Unset = ""
    outcome: str | Unset = "default"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        source = self.source

        target = self.target

        label = self.label

        outcome = self.outcome

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source": source,
                "target": target,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if outcome is not UNSET:
            field_dict["outcome"] = outcome

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        source = d.pop("source")

        target = d.pop("target")

        label = d.pop("label", UNSET)

        outcome = d.pop("outcome", UNSET)

        workflow_document_edges_item = cls(
            id=id,
            source=source,
            target=target,
            label=label,
            outcome=outcome,
        )

        workflow_document_edges_item.additional_properties = d
        return workflow_document_edges_item

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
