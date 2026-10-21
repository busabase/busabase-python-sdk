from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.records_list_page_sort_direction import (
    RecordsListPageSortDirection,
    check_records_list_page_sort_direction,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordsListPageSort")


@_attrs_define
class RecordsListPageSort:
    """Sort by one field. Only number and date fields sort authoritatively (their typed value column matches a client's own
    ordering); any other field type is returned in the default order and left for the caller to sort. Replaces the saved
    View's sort when `viewId` is also given (the View's filters still apply). Empty values sort last; ties are broken by
    record id, so pages never overlap.

        Attributes:
            field_slug (str):
            field_type (str | Unset):
            direction (RecordsListPageSortDirection | Unset):  Default: 'asc'.
    """

    field_slug: str
    field_type: str | Unset = UNSET
    direction: RecordsListPageSortDirection | Unset = "asc"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_slug = self.field_slug

        field_type = self.field_type

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldSlug": field_slug,
            }
        )
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        field_slug = d.pop("fieldSlug")

        field_type = d.pop("fieldType", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: RecordsListPageSortDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = check_records_list_page_sort_direction(_direction)

        records_list_page_sort = cls(
            field_slug=field_slug,
            field_type=field_type,
            direction=direction,
        )

        records_list_page_sort.additional_properties = d
        return records_list_page_sort

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
