from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.records_count_value_filters_item_type_1_any_item import RecordsCountValueFiltersItemType1AnyItem


T = TypeVar("T", bound="RecordsCountValueFiltersItemType1")


@_attrs_define
class RecordsCountValueFiltersItemType1:
    """
    Attributes:
        any_ (list[RecordsCountValueFiltersItemType1AnyItem]):
    """

    any_: list[RecordsCountValueFiltersItemType1AnyItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        any_ = []
        for any_item_data in self.any_:
            any_item = any_item_data.to_dict()
            any_.append(any_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "any": any_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.records_count_value_filters_item_type_1_any_item import RecordsCountValueFiltersItemType1AnyItem

        d = dict(src_dict)
        any_ = []
        _any_ = d.pop("any")
        for any_item_data in _any_:
            any_item = RecordsCountValueFiltersItemType1AnyItem.from_dict(any_item_data)

            any_.append(any_item)

        records_count_value_filters_item_type_1 = cls(
            any_=any_,
        )

        records_count_value_filters_item_type_1.additional_properties = d
        return records_count_value_filters_item_type_1

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
