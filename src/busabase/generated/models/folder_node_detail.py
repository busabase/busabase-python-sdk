from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node import Node


T = TypeVar("T", bound="FolderNodeDetail")


@_attrs_define
class FolderNodeDetail:
    """
    Attributes:
        node (Node):
        children (list[Node]):
        type_ (Literal['folder']):
    """

    node: Node
    children: list[Node]
    type_: Literal["folder"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node = self.node.to_dict()

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node": node,
                "children": children,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.node import Node

        d = dict(src_dict)
        node = Node.from_dict(d.pop("node"))

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = Node.from_dict(children_item_data)

            children.append(children_item)

        type_ = cast(Literal["folder"], d.pop("type"))
        if type_ != "folder":
            raise ValueError(f"type must match const 'folder', got '{type_}'")

        folder_node_detail = cls(
            node=node,
            children=children,
            type_=type_,
        )

        folder_node_detail.additional_properties = d
        return folder_node_detail

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
