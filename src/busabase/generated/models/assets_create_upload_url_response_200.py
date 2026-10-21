from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetsCreateUploadUrlResponse200")


@_attrs_define
class AssetsCreateUploadUrlResponse200:
    """
    Attributes:
        upload_url (str):
        storage_key (str):
        public_url (str):
        expires_in (float):
        duplicate (bool | Unset):
        attachment_id (str | Unset):
        asset_id (str | Unset):
    """

    upload_url: str
    storage_key: str
    public_url: str
    expires_in: float
    duplicate: bool | Unset = UNSET
    attachment_id: str | Unset = UNSET
    asset_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_url = self.upload_url

        storage_key = self.storage_key

        public_url = self.public_url

        expires_in = self.expires_in

        duplicate = self.duplicate

        attachment_id = self.attachment_id

        asset_id = self.asset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadUrl": upload_url,
                "storageKey": storage_key,
                "publicUrl": public_url,
                "expiresIn": expires_in,
            }
        )
        if duplicate is not UNSET:
            field_dict["duplicate"] = duplicate
        if attachment_id is not UNSET:
            field_dict["attachmentId"] = attachment_id
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        upload_url = d.pop("uploadUrl")

        storage_key = d.pop("storageKey")

        public_url = d.pop("publicUrl")

        expires_in = d.pop("expiresIn")

        duplicate = d.pop("duplicate", UNSET)

        attachment_id = d.pop("attachmentId", UNSET)

        asset_id = d.pop("assetId", UNSET)

        assets_create_upload_url_response_200 = cls(
            upload_url=upload_url,
            storage_key=storage_key,
            public_url=public_url,
            expires_in=expires_in,
            duplicate=duplicate,
            attachment_id=attachment_id,
            asset_id=asset_id,
        )

        assets_create_upload_url_response_200.additional_properties = d
        return assets_create_upload_url_response_200

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
