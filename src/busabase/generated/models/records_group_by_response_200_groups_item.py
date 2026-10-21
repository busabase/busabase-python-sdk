from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.records_group_by_response_200_groups_item_aggregates import (
        RecordsGroupByResponse200GroupsItemAggregates,
    )


T = TypeVar("T", bound="RecordsGroupByResponse200GroupsItem")


@_attrs_define
class RecordsGroupByResponse200GroupsItem:
    """
    Attributes:
        value (bool | float | None | str): The bucket key. Under `grid` bucketing always a string or null (a select's
            choice, or `"true"`/`"false"` for a checkbox, with null meaning "no value"). Under `sql` bucketing it is the
            stored value in its own type, and null is the bucket of records that have no value for the field.
        count (int): Records in this bucket.
        aggregates (RecordsGroupByResponse200GroupsItemAggregates | Unset): Present only when `aggregates` was
            requested, keyed `"<fn>:<fieldSlug>"`. A null value means the bucket held no records with that field set — not
            zero.
    """

    value: bool | float | None | str
    count: int
    aggregates: RecordsGroupByResponse200GroupsItemAggregates | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: bool | float | None | str
        value = self.value

        count = self.count

        aggregates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aggregates, Unset):
            aggregates = self.aggregates.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "count": count,
            }
        )
        if aggregates is not UNSET:
            field_dict["aggregates"] = aggregates

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.records_group_by_response_200_groups_item_aggregates import (
            RecordsGroupByResponse200GroupsItemAggregates,
        )

        d = dict(src_dict)

        def _parse_value(data: object) -> bool | float | None | str:
            if data is None:
                return data
            return cast(bool | float | None | str, data)

        value = _parse_value(d.pop("value"))

        count = d.pop("count")

        _aggregates = d.pop("aggregates", UNSET)
        aggregates: RecordsGroupByResponse200GroupsItemAggregates | Unset
        if isinstance(_aggregates, Unset):
            aggregates = UNSET
        else:
            aggregates = RecordsGroupByResponse200GroupsItemAggregates.from_dict(_aggregates)

        records_group_by_response_200_groups_item = cls(
            value=value,
            count=count,
            aggregates=aggregates,
        )

        records_group_by_response_200_groups_item.additional_properties = d
        return records_group_by_response_200_groups_item

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
