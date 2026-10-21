from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FileTreesPreparePreviewResponse200Type1")


@_attrs_define
class FileTreesPreparePreviewResponse200Type1:
    """
    Attributes:
        state (Literal['ready']):
        provider (Literal['previewfile']):
        preview_url (str):
        expires_at (datetime.datetime):
    """

    state: Literal["ready"]
    provider: Literal["previewfile"]
    preview_url: str
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        provider = self.provider

        preview_url = self.preview_url

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "provider": provider,
                "previewUrl": preview_url,
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        state = cast(Literal["ready"], d.pop("state"))
        if state != "ready":
            raise ValueError(f"state must match const 'ready', got '{state}'")

        provider = cast(Literal["previewfile"], d.pop("provider"))
        if provider != "previewfile":
            raise ValueError(f"provider must match const 'previewfile', got '{provider}'")

        preview_url = d.pop("previewUrl")

        expires_at = datetime.datetime.fromisoformat(d.pop("expiresAt"))

        file_trees_prepare_preview_response_200_type_1 = cls(
            state=state,
            provider=provider,
            preview_url=preview_url,
            expires_at=expires_at,
        )

        file_trees_prepare_preview_response_200_type_1.additional_properties = d
        return file_trees_prepare_preview_response_200_type_1

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
