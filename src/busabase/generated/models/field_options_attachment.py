from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldOptionsAttachment")


@_attrs_define
class FieldOptionsAttachment:
    """
    Attributes:
        max_files (int | Unset):
        allowed_mime_types (list[str] | Unset):
        max_file_size (int | Unset):
    """

    max_files: int | Unset = UNSET
    allowed_mime_types: list[str] | Unset = UNSET
    max_file_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_files = self.max_files

        allowed_mime_types: list[str] | Unset = UNSET
        if not isinstance(self.allowed_mime_types, Unset):
            allowed_mime_types = self.allowed_mime_types

        max_file_size = self.max_file_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_files is not UNSET:
            field_dict["maxFiles"] = max_files
        if allowed_mime_types is not UNSET:
            field_dict["allowedMimeTypes"] = allowed_mime_types
        if max_file_size is not UNSET:
            field_dict["maxFileSize"] = max_file_size

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        max_files = d.pop("maxFiles", UNSET)

        allowed_mime_types = cast(list[str], d.pop("allowedMimeTypes", UNSET))

        max_file_size = d.pop("maxFileSize", UNSET)

        field_options_attachment = cls(
            max_files=max_files,
            allowed_mime_types=allowed_mime_types,
            max_file_size=max_file_size,
        )

        field_options_attachment.additional_properties = d
        return field_options_attachment

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
