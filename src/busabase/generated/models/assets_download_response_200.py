from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetsDownloadResponse200")


@_attrs_define
class AssetsDownloadResponse200:
    """
    Attributes:
        asset_id (str):
        download_url (str):
        file_name (str):
        mime_type (str):
        size (int):
        content_hash (None | str):
    """

    asset_id: str
    download_url: str
    file_name: str
    mime_type: str
    size: int
    content_hash: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        download_url = self.download_url

        file_name = self.file_name

        mime_type = self.mime_type

        size = self.size

        content_hash: None | str
        content_hash = self.content_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
                "downloadUrl": download_url,
                "fileName": file_name,
                "mimeType": mime_type,
                "size": size,
                "contentHash": content_hash,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        asset_id = d.pop("assetId")

        download_url = d.pop("downloadUrl")

        file_name = d.pop("fileName")

        mime_type = d.pop("mimeType")

        size = d.pop("size")

        def _parse_content_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_hash = _parse_content_hash(d.pop("contentHash"))

        assets_download_response_200 = cls(
            asset_id=asset_id,
            download_url=download_url,
            file_name=file_name,
            mime_type=mime_type,
            size=size,
            content_hash=content_hash,
        )

        assets_download_response_200.additional_properties = d
        return assets_download_response_200

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
