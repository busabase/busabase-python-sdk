from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.record_filter_operator import RecordFilterOperator, check_record_filter_operator
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordFilter")


@_attrs_define
class RecordFilter:
    """
    Attributes:
        field_slug (str):
        operator (RecordFilterOperator):
        field_type (str | Unset):
        value (Any | Unset):
    """

    field_slug: str
    operator: RecordFilterOperator
    field_type: str | Unset = UNSET
    value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_slug = self.field_slug

        operator: str = self.operator

        field_type = self.field_type

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldSlug": field_slug,
                "operator": operator,
            }
        )
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        field_slug = d.pop("fieldSlug")

        operator = check_record_filter_operator(d.pop("operator"))

        field_type = d.pop("fieldType", UNSET)

        value = d.pop("value", UNSET)

        record_filter = cls(
            field_slug=field_slug,
            operator=operator,
            field_type=field_type,
            value=value,
        )

        record_filter.additional_properties = d
        return record_filter

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
