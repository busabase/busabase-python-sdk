from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetsPutTextBody")


@_attrs_define
class AssetsPutTextBody:
    """
    Attributes:
        text (str | Unset):
        storage_key (str | Unset):
        content_hash (str | Unset):
        none (bool | Unset):
    """

    text: str | Unset = UNSET
    storage_key: str | Unset = UNSET
    content_hash: str | Unset = UNSET
    none: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        storage_key = self.storage_key

        content_hash = self.content_hash

        none = self.none

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if storage_key is not UNSET:
            field_dict["storageKey"] = storage_key
        if content_hash is not UNSET:
            field_dict["contentHash"] = content_hash
        if none is not UNSET:
            field_dict["none"] = none

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        text = d.pop("text", UNSET)

        storage_key = d.pop("storageKey", UNSET)

        content_hash = d.pop("contentHash", UNSET)

        none = d.pop("none", UNSET)

        assets_put_text_body = cls(
            text=text,
            storage_key=storage_key,
            content_hash=content_hash,
            none=none,
        )

        assets_put_text_body.additional_properties = d
        return assets_put_text_body

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
