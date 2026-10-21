from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.html_document import HtmlDocument
    from ..models.node import Node


T = TypeVar("T", bound="HtmlNodeDetail")


@_attrs_define
class HtmlNodeDetail:
    """
    Attributes:
        type_ (Literal['html']):
        node (Node):
        document (HtmlDocument):
    """

    type_: Literal["html"]
    node: Node
    document: HtmlDocument
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        node = self.node.to_dict()

        document = self.document.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "node": node,
                "document": document,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.html_document import HtmlDocument
        from ..models.node import Node

        d = dict(src_dict)
        type_ = cast(Literal["html"], d.pop("type"))
        if type_ != "html":
            raise ValueError(f"type must match const 'html', got '{type_}'")

        node = Node.from_dict(d.pop("node"))

        document = HtmlDocument.from_dict(d.pop("document"))

        html_node_detail = cls(
            type_=type_,
            node=node,
            document=document,
        )

        html_node_detail.additional_properties = d
        return html_node_detail

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
