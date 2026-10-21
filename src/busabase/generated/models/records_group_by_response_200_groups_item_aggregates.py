from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecordsGroupByResponse200GroupsItemAggregates")


@_attrs_define
class RecordsGroupByResponse200GroupsItemAggregates:
    """Present only when `aggregates` was requested, keyed `"<fn>:<fieldSlug>"`. A null value means the bucket held no
    records with that field set — not zero.

    """

    additional_properties: dict[str, float | None] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        records_group_by_response_200_groups_item_aggregates = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> float | None:
                if data is None:
                    return data
                return cast(float | None, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        records_group_by_response_200_groups_item_aggregates.additional_properties = additional_properties
        return records_group_by_response_200_groups_item_aggregates

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> float | None:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: float | None) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
