from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_document import WorkflowDocument


T = TypeVar("T", bound="WorkflowNodeContent")


@_attrs_define
class WorkflowNodeContent:
    """
    Attributes:
        kind (Literal['workflow']):
        document (WorkflowDocument):
    """

    kind: Literal["workflow"]
    document: WorkflowDocument
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        document = self.document.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "document": document,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_document import WorkflowDocument

        d = dict(src_dict)
        kind = cast(Literal["workflow"], d.pop("kind"))
        if kind != "workflow":
            raise ValueError(f"kind must match const 'workflow', got '{kind}'")

        document = WorkflowDocument.from_dict(d.pop("document"))

        workflow_node_content = cls(
            kind=kind,
            document=document,
        )

        workflow_node_content.additional_properties = d
        return workflow_node_content

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
