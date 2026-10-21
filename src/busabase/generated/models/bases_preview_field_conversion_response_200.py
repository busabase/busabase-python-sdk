from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bases_preview_field_conversion_response_200_conflicts_item import (
        BasesPreviewFieldConversionResponse200ConflictsItem,
    )


T = TypeVar("T", bound="BasesPreviewFieldConversionResponse200")


@_attrs_define
class BasesPreviewFieldConversionResponse200:
    """
    Attributes:
        total_count (float):
        convertible_count (float):
        null_count (float):
        conflicts (list[BasesPreviewFieldConversionResponse200ConflictsItem]):
    """

    total_count: float
    convertible_count: float
    null_count: float
    conflicts: list[BasesPreviewFieldConversionResponse200ConflictsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        convertible_count = self.convertible_count

        null_count = self.null_count

        conflicts = []
        for conflicts_item_data in self.conflicts:
            conflicts_item = conflicts_item_data.to_dict()
            conflicts.append(conflicts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalCount": total_count,
                "convertibleCount": convertible_count,
                "nullCount": null_count,
                "conflicts": conflicts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bases_preview_field_conversion_response_200_conflicts_item import (
            BasesPreviewFieldConversionResponse200ConflictsItem,
        )

        d = dict(src_dict)
        total_count = d.pop("totalCount")

        convertible_count = d.pop("convertibleCount")

        null_count = d.pop("nullCount")

        conflicts = []
        _conflicts = d.pop("conflicts")
        for conflicts_item_data in _conflicts:
            conflicts_item = BasesPreviewFieldConversionResponse200ConflictsItem.from_dict(conflicts_item_data)

            conflicts.append(conflicts_item)

        bases_preview_field_conversion_response_200 = cls(
            total_count=total_count,
            convertible_count=convertible_count,
            null_count=null_count,
            conflicts=conflicts,
        )

        bases_preview_field_conversion_response_200.additional_properties = d
        return bases_preview_field_conversion_response_200

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
