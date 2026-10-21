from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.whiteboard_node_content_document import WhiteboardNodeContentDocument


T = TypeVar("T", bound="WhiteboardNodeContent")


@_attrs_define
class WhiteboardNodeContent:
    """
    Attributes:
        kind (Literal['whiteboard']):
        document (WhiteboardNodeContentDocument):
    """

    kind: Literal["whiteboard"]
    document: WhiteboardNodeContentDocument
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
        from ..models.whiteboard_node_content_document import WhiteboardNodeContentDocument

        d = dict(src_dict)
        kind = cast(Literal["whiteboard"], d.pop("kind"))
        if kind != "whiteboard":
            raise ValueError(f"kind must match const 'whiteboard', got '{kind}'")

        document = WhiteboardNodeContentDocument.from_dict(d.pop("document"))

        whiteboard_node_content = cls(
            kind=kind,
            document=document,
        )

        whiteboard_node_content.additional_properties = d
        return whiteboard_node_content

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
