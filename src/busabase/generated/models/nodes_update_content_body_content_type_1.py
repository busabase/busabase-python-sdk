from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nodes_update_content_body_content_type_1_document import NodesUpdateContentBodyContentType1Document


T = TypeVar("T", bound="NodesUpdateContentBodyContentType1")


@_attrs_define
class NodesUpdateContentBodyContentType1:
    """
    Attributes:
        kind (Literal['whiteboard']):
        document (NodesUpdateContentBodyContentType1Document):
    """

    kind: Literal["whiteboard"]
    document: NodesUpdateContentBodyContentType1Document
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
        from ..models.nodes_update_content_body_content_type_1_document import (
            NodesUpdateContentBodyContentType1Document,
        )

        d = dict(src_dict)
        kind = cast(Literal["whiteboard"], d.pop("kind"))
        if kind != "whiteboard":
            raise ValueError(f"kind must match const 'whiteboard', got '{kind}'")

        document = NodesUpdateContentBodyContentType1Document.from_dict(d.pop("document"))

        nodes_update_content_body_content_type_1 = cls(
            kind=kind,
            document=document,
        )

        nodes_update_content_body_content_type_1.additional_properties = d
        return nodes_update_content_body_content_type_1

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
