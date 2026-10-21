from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.records_group_by_response_200_groups_item import RecordsGroupByResponse200GroupsItem


T = TypeVar("T", bound="RecordsGroupByResponse200")


@_attrs_define
class RecordsGroupByResponse200:
    """
    Attributes:
        groups (list[RecordsGroupByResponse200GroupsItem]):
        total (int):
    """

    groups: list[RecordsGroupByResponse200GroupsItem]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groups": groups,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.records_group_by_response_200_groups_item import RecordsGroupByResponse200GroupsItem

        d = dict(src_dict)
        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = RecordsGroupByResponse200GroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        total = d.pop("total")

        records_group_by_response_200 = cls(
            groups=groups,
            total=total,
        )

        records_group_by_response_200.additional_properties = d
        return records_group_by_response_200

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
