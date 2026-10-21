from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetsCreateTextUploadUrlBody")


@_attrs_define
class AssetsCreateTextUploadUrlBody:
    """
    Attributes:
        asset_id (str):
        size_bytes (int):
        content_hash (str | Unset):
    """

    asset_id: str
    size_bytes: int
    content_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        size_bytes = self.size_bytes

        content_hash = self.content_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
                "sizeBytes": size_bytes,
            }
        )
        if content_hash is not UNSET:
            field_dict["contentHash"] = content_hash

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        asset_id = d.pop("assetId")

        size_bytes = d.pop("sizeBytes")

        content_hash = d.pop("contentHash", UNSET)

        assets_create_text_upload_url_body = cls(
            asset_id=asset_id,
            size_bytes=size_bytes,
            content_hash=content_hash,
        )

        assets_create_text_upload_url_body.additional_properties = d
        return assets_create_text_upload_url_body

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
