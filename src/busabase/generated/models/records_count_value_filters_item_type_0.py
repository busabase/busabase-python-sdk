from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.records_count_value_filters_item_type_0_operator import (
    RecordsCountValueFiltersItemType0Operator,
    check_records_count_value_filters_item_type_0_operator,
)

T = TypeVar("T", bound="RecordsCountValueFiltersItemType0")


@_attrs_define
class RecordsCountValueFiltersItemType0:
    """
    Attributes:
        field_slug (str):
        operator (RecordsCountValueFiltersItemType0Operator):
        value (bool | float | str):
    """

    field_slug: str
    operator: RecordsCountValueFiltersItemType0Operator
    value: bool | float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_slug = self.field_slug

        operator: str = self.operator

        value: bool | float | str
        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldSlug": field_slug,
                "operator": operator,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        field_slug = d.pop("fieldSlug")

        operator = check_records_count_value_filters_item_type_0_operator(d.pop("operator"))

        def _parse_value(data: object) -> bool | float | str:
            return cast(bool | float | str, data)

        value = _parse_value(d.pop("value"))

        records_count_value_filters_item_type_0 = cls(
            field_slug=field_slug,
            operator=operator,
            value=value,
        )

        records_count_value_filters_item_type_0.additional_properties = d
        return records_count_value_filters_item_type_0

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
