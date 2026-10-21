from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.record import Record


T = TypeVar("T", bound="RecordsListPageResponse200")


@_attrs_define
class RecordsListPageResponse200:
    """
    Attributes:
        records (list[Record]):
        total (int):
        total_pages (int):
        page (int):
        page_size (int):
    """

    records: list[Record]
    total: int
    total_pages: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        total = self.total

        total_pages = self.total_pages

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "records": records,
                "total": total,
                "totalPages": total_pages,
                "page": page,
                "pageSize": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.record import Record

        d = dict(src_dict)
        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = Record.from_dict(records_item_data)

            records.append(records_item)

        total = d.pop("total")

        total_pages = d.pop("totalPages")

        page = d.pop("page")

        page_size = d.pop("pageSize")

        records_list_page_response_200 = cls(
            records=records,
            total=total,
            total_pages=total_pages,
            page=page,
            page_size=page_size,
        )

        records_list_page_response_200.additional_properties = d
        return records_list_page_response_200

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
