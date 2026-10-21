from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dump_export_doc_bodies_response_200_bodies_item import DumpExportDocBodiesResponse200BodiesItem


T = TypeVar("T", bound="DumpExportDocBodiesResponse200")


@_attrs_define
class DumpExportDocBodiesResponse200:
    """
    Attributes:
        bodies (list[DumpExportDocBodiesResponse200BodiesItem]):
    """

    bodies: list[DumpExportDocBodiesResponse200BodiesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bodies = []
        for bodies_item_data in self.bodies:
            bodies_item = bodies_item_data.to_dict()
            bodies.append(bodies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bodies": bodies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dump_export_doc_bodies_response_200_bodies_item import DumpExportDocBodiesResponse200BodiesItem

        d = dict(src_dict)
        bodies = []
        _bodies = d.pop("bodies")
        for bodies_item_data in _bodies:
            bodies_item = DumpExportDocBodiesResponse200BodiesItem.from_dict(bodies_item_data)

            bodies.append(bodies_item)

        dump_export_doc_bodies_response_200 = cls(
            bodies=bodies,
        )

        dump_export_doc_bodies_response_200.additional_properties = d
        return dump_export_doc_bodies_response_200

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
