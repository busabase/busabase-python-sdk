from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasesPreviewFieldConversionResponse200ConflictsItem")


@_attrs_define
class BasesPreviewFieldConversionResponse200ConflictsItem:
    """
    Attributes:
        record_id (str):
        current_value (Any | Unset):
    """

    record_id: str
    current_value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        current_value = self.current_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recordId": record_id,
            }
        )
        if current_value is not UNSET:
            field_dict["currentValue"] = current_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        record_id = d.pop("recordId")

        current_value = d.pop("currentValue", UNSET)

        bases_preview_field_conversion_response_200_conflicts_item = cls(
            record_id=record_id,
            current_value=current_value,
        )

        bases_preview_field_conversion_response_200_conflicts_item.additional_properties = d
        return bases_preview_field_conversion_response_200_conflicts_item

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
