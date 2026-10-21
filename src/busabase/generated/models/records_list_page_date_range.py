from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecordsListPageDateRange")


@_attrs_define
class RecordsListPageDateRange:
    """Scope the page to a `date`/`created_time`/`updated_time` field falling in `[gte, lt)` — a half-open range of
    absolute UTC instants, not a `filters` condition. Resolve the bounds yourself: a day or a month only means something
    in a timezone, and the server does not know the viewer's.

        Attributes:
            field_slug (str):
            gte (str): Inclusive lower bound, ISO 8601 UTC instant.
            lt (str): EXCLUSIVE upper bound, ISO 8601 UTC instant.
    """

    field_slug: str
    gte: str
    lt: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_slug = self.field_slug

        gte = self.gte

        lt = self.lt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldSlug": field_slug,
                "gte": gte,
                "lt": lt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        field_slug = d.pop("fieldSlug")

        gte = d.pop("gte")

        lt = d.pop("lt")

        records_list_page_date_range = cls(
            field_slug=field_slug,
            gte=gte,
            lt=lt,
        )

        records_list_page_date_range.additional_properties = d
        return records_list_page_date_range

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
