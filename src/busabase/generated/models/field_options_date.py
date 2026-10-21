from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldOptionsDate")


@_attrs_define
class FieldOptionsDate:
    """
    Attributes:
        include_time (bool | Unset):
        timezone (str | Unset): IANA time zone, e.g. "Asia/Shanghai". Omit to show each reader their own local time.
    """

    include_time: bool | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_time = self.include_time

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_time is not UNSET:
            field_dict["includeTime"] = include_time
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        include_time = d.pop("includeTime", UNSET)

        timezone = d.pop("timezone", UNSET)

        field_options_date = cls(
            include_time=include_time,
            timezone=timezone,
        )

        field_options_date.additional_properties = d
        return field_options_date

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
