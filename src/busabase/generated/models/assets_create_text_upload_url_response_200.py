from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetsCreateTextUploadUrlResponse200")


@_attrs_define
class AssetsCreateTextUploadUrlResponse200:
    """
    Attributes:
        upload_url (str):
        storage_key (str):
        expires_in (int):
    """

    upload_url: str
    storage_key: str
    expires_in: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_url = self.upload_url

        storage_key = self.storage_key

        expires_in = self.expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadUrl": upload_url,
                "storageKey": storage_key,
                "expiresIn": expires_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        upload_url = d.pop("uploadUrl")

        storage_key = d.pop("storageKey")

        expires_in = d.pop("expiresIn")

        assets_create_text_upload_url_response_200 = cls(
            upload_url=upload_url,
            storage_key=storage_key,
            expires_in=expires_in,
        )

        assets_create_text_upload_url_response_200.additional_properties = d
        return assets_create_text_upload_url_response_200

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
