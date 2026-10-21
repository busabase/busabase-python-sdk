from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PendingChangeRequestMergeSummary")


@_attrs_define
class PendingChangeRequestMergeSummary:
    """Filled in when the change request merges. `slugChanges` (present only when non-empty) lists items a restore brought
    back under a new slug because another item took the old one while they were in the Trash: `{ nodeId, nodeType, name,
    fromSlug, toSlug }`. Read the new slug from here instead of assuming the old one.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pending_change_request_merge_summary = cls()

        pending_change_request_merge_summary.additional_properties = d
        return pending_change_request_merge_summary

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
