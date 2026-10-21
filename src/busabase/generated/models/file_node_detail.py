from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset import Asset
    from ..models.node import Node


T = TypeVar("T", bound="FileNodeDetail")


@_attrs_define
class FileNodeDetail:
    """
    Attributes:
        node (Node):
        asset (Asset):
        type_ (Literal['file']):
    """

    node: Node
    asset: Asset
    type_: Literal["file"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node = self.node.to_dict()

        asset = self.asset.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node": node,
                "asset": asset,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.asset import Asset
        from ..models.node import Node

        d = dict(src_dict)
        node = Node.from_dict(d.pop("node"))

        asset = Asset.from_dict(d.pop("asset"))

        type_ = cast(Literal["file"], d.pop("type"))
        if type_ != "file":
            raise ValueError(f"type must match const 'file', got '{type_}'")

        file_node_detail = cls(
            node=node,
            asset=asset,
            type_=type_,
        )

        file_node_detail.additional_properties = d
        return file_node_detail

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
