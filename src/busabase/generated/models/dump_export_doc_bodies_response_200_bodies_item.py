from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DumpExportDocBodiesResponse200BodiesItem")


@_attrs_define
class DumpExportDocBodiesResponse200BodiesItem:
    """
    Attributes:
        node_id (str):
        markdown (str):
    """

    node_id: str
    markdown: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        markdown = self.markdown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeId": node_id,
                "markdown": markdown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        node_id = d.pop("nodeId")

        markdown = d.pop("markdown")

        dump_export_doc_bodies_response_200_bodies_item = cls(
            node_id=node_id,
            markdown=markdown,
        )

        dump_export_doc_bodies_response_200_bodies_item.additional_properties = d
        return dump_export_doc_bodies_response_200_bodies_item

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
