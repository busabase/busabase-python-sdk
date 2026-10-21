from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assets_confirm_body_metadata import AssetsConfirmBodyMetadata


T = TypeVar("T", bound="AssetsConfirmBody")


@_attrs_define
class AssetsConfirmBody:
    """
    Attributes:
        storage_key (str):
        file_name (str):
        mime_type (str):
        size_bytes (int):
        space_id (str | Unset):
        context (str | Unset):
        metadata (AssetsConfirmBodyMetadata | Unset):
        content_hash (str | Unset):
    """

    storage_key: str
    file_name: str
    mime_type: str
    size_bytes: int
    space_id: str | Unset = UNSET
    context: str | Unset = UNSET
    metadata: AssetsConfirmBodyMetadata | Unset = UNSET
    content_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        storage_key = self.storage_key

        file_name = self.file_name

        mime_type = self.mime_type

        size_bytes = self.size_bytes

        space_id = self.space_id

        context = self.context

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        content_hash = self.content_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storageKey": storage_key,
                "fileName": file_name,
                "mimeType": mime_type,
                "sizeBytes": size_bytes,
            }
        )
        if space_id is not UNSET:
            field_dict["spaceId"] = space_id
        if context is not UNSET:
            field_dict["context"] = context
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if content_hash is not UNSET:
            field_dict["contentHash"] = content_hash

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assets_confirm_body_metadata import AssetsConfirmBodyMetadata

        d = dict(src_dict)
        storage_key = d.pop("storageKey")

        file_name = d.pop("fileName")

        mime_type = d.pop("mimeType")

        size_bytes = d.pop("sizeBytes")

        space_id = d.pop("spaceId", UNSET)

        context = d.pop("context", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AssetsConfirmBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AssetsConfirmBodyMetadata.from_dict(_metadata)

        content_hash = d.pop("contentHash", UNSET)

        assets_confirm_body = cls(
            storage_key=storage_key,
            file_name=file_name,
            mime_type=mime_type,
            size_bytes=size_bytes,
            space_id=space_id,
            context=context,
            metadata=metadata,
            content_hash=content_hash,
        )

        assets_confirm_body.additional_properties = d
        return assets_confirm_body

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
