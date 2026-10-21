from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GrepBodyScopeRecords")


@_attrs_define
class GrepBodyScopeRecords:
    """
    Attributes:
        base_ids (list[str] | Unset):
        base_slugs (list[str] | Unset):
    """

    base_ids: list[str] | Unset = UNSET
    base_slugs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_ids: list[str] | Unset = UNSET
        if not isinstance(self.base_ids, Unset):
            base_ids = self.base_ids

        base_slugs: list[str] | Unset = UNSET
        if not isinstance(self.base_slugs, Unset):
            base_slugs = self.base_slugs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_ids is not UNSET:
            field_dict["baseIds"] = base_ids
        if base_slugs is not UNSET:
            field_dict["baseSlugs"] = base_slugs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        base_ids = cast(list[str], d.pop("baseIds", UNSET))

        base_slugs = cast(list[str], d.pop("baseSlugs", UNSET))

        grep_body_scope_records = cls(
            base_ids=base_ids,
            base_slugs=base_slugs,
        )

        grep_body_scope_records.additional_properties = d
        return grep_body_scope_records

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
