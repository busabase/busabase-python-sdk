from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_content_kind import AssetContentKind, check_asset_content_kind
from ..models.asset_text_status import AssetTextStatus, check_asset_text_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_metadata import AssetMetadata


T = TypeVar("T", bound="Asset")


@_attrs_define
class Asset:
    """
    Attributes:
        id (str):
        attachment_id (str):
        name (str):
        content_kind (AssetContentKind):
        file_name (str):
        mime_type (str):
        size (int):
        url (str):
        content_hash (None | str):
        usage_count (int):
        text_status (AssetTextStatus):
        created_at (str):
        metadata (AssetMetadata | Unset):
    """

    id: str
    attachment_id: str
    name: str
    content_kind: AssetContentKind
    file_name: str
    mime_type: str
    size: int
    url: str
    content_hash: None | str
    usage_count: int
    text_status: AssetTextStatus
    created_at: str
    metadata: AssetMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        attachment_id = self.attachment_id

        name = self.name

        content_kind: str = self.content_kind

        file_name = self.file_name

        mime_type = self.mime_type

        size = self.size

        url = self.url

        content_hash: None | str
        content_hash = self.content_hash

        usage_count = self.usage_count

        text_status: str = self.text_status

        created_at = self.created_at

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "attachmentId": attachment_id,
                "name": name,
                "contentKind": content_kind,
                "fileName": file_name,
                "mimeType": mime_type,
                "size": size,
                "url": url,
                "contentHash": content_hash,
                "usageCount": usage_count,
                "textStatus": text_status,
                "createdAt": created_at,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.asset_metadata import AssetMetadata

        d = dict(src_dict)
        id = d.pop("id")

        attachment_id = d.pop("attachmentId")

        name = d.pop("name")

        content_kind = check_asset_content_kind(d.pop("contentKind"))

        file_name = d.pop("fileName")

        mime_type = d.pop("mimeType")

        size = d.pop("size")

        url = d.pop("url")

        def _parse_content_hash(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_hash = _parse_content_hash(d.pop("contentHash"))

        usage_count = d.pop("usageCount")

        text_status = check_asset_text_status(d.pop("textStatus"))

        created_at = d.pop("createdAt")

        _metadata = d.pop("metadata", UNSET)
        metadata: AssetMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AssetMetadata.from_dict(_metadata)

        asset = cls(
            id=id,
            attachment_id=attachment_id,
            name=name,
            content_kind=content_kind,
            file_name=file_name,
            mime_type=mime_type,
            size=size,
            url=url,
            content_hash=content_hash,
            usage_count=usage_count,
            text_status=text_status,
            created_at=created_at,
            metadata=metadata,
        )

        asset.additional_properties = d
        return asset

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
