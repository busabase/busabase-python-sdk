from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BasesCreateChangeRequestBodyFields")


@_attrs_define
class BasesCreateChangeRequestBodyFields:
    """Record field values keyed by field slug. A field id or its exact display name (any language, unambiguous) is mapped
    to the slug; a write in which no key names a field of the Base is a 400 listing the valid slugs. The base's PRIMARY
    field (its first field) becomes the record's display name and the change request title everywhere — always give it a
    short, human-readable value, never an id or placeholder.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bases_create_change_request_body_fields = cls()

        bases_create_change_request_body_fields.additional_properties = d
        return bases_create_change_request_body_fields

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
