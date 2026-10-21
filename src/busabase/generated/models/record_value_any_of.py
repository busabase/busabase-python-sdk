from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.record_value_comparison import RecordValueComparison


T = TypeVar("T", bound="RecordValueAnyOf")


@_attrs_define
class RecordValueAnyOf:
    """
    Attributes:
        any_ (list[RecordValueComparison]):
    """

    any_: list[RecordValueComparison]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        any_ = []
        for any_item_data in self.any_:
            any_item = any_item_data.to_dict()
            any_.append(any_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "any": any_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.record_value_comparison import RecordValueComparison

        d = dict(src_dict)
        any_ = []
        _any_ = d.pop("any")
        for any_item_data in _any_:
            any_item = RecordValueComparison.from_dict(any_item_data)

            any_.append(any_item)

        record_value_any_of = cls(
            any_=any_,
        )

        record_value_any_of.additional_properties = d
        return record_value_any_of

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
