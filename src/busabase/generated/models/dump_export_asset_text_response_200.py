from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DumpExportAssetTextResponse200")


@_attrs_define
class DumpExportAssetTextResponse200:
    """
    Attributes:
        asset_id (str):
        text_storage_key (str):
        download_url (None | str):
        text_content_hash (None | str):
        byte_count (int):
    """

    asset_id: str
    text_storage_key: str
    download_url: None | str
    text_content_hash: None | str
    byte_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        text_storage_key = self.text_storage_key

        download_url: None | str
        download_url = self.download_url

        text_content_hash: None | str
        text_content_hash = self.text_content_hash

        byte_count = self.byte_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
                "textStorageKey": text_storage_key,
                "downloadUrl": download_url,
                "textContentHash": text_content_hash,
                "byteCount": byte_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        asset_id = d.pop("assetId")

        text_storage_key = d.pop("textStorageKey")

        def _parse_download_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        download_url = _parse_download_url(d.pop("downloadUrl"))

        def _parse_text_content_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text_content_hash = _parse_text_content_hash(d.pop("textContentHash"))

        byte_count = d.pop("byteCount")

        dump_export_asset_text_response_200 = cls(
            asset_id=asset_id,
            text_storage_key=text_storage_key,
            download_url=download_url,
            text_content_hash=text_content_hash,
            byte_count=byte_count,
        )

        dump_export_asset_text_response_200.additional_properties = d
        return dump_export_asset_text_response_200

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
