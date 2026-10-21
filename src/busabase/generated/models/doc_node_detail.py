from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node import Node


T = TypeVar("T", bound="DocNodeDetail")


@_attrs_define
class DocNodeDetail:
    """
    Attributes:
        node (Node):
        storage_prefix (str):
        body (str):
        type_ (Literal['doc']):
    """

    node: Node
    storage_prefix: str
    body: str
    type_: Literal["doc"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node = self.node.to_dict()

        storage_prefix = self.storage_prefix

        body = self.body

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node": node,
                "storagePrefix": storage_prefix,
                "body": body,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.node import Node

        d = dict(src_dict)
        node = Node.from_dict(d.pop("node"))

        storage_prefix = d.pop("storagePrefix")

        body = d.pop("body")

        type_ = cast(Literal["doc"], d.pop("type"))
        if type_ != "doc":
            raise ValueError(f"type must match const 'doc', got '{type_}'")

        doc_node_detail = cls(
            node=node,
            storage_prefix=storage_prefix,
            body=body,
            type_=type_,
        )

        doc_node_detail.additional_properties = d
        return doc_node_detail

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
