from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.unavailable_file_preview_reason import UnavailableFilePreviewReason, check_unavailable_file_preview_reason

T = TypeVar("T", bound="UnavailableFilePreview")


@_attrs_define
class UnavailableFilePreview:
    """
    Attributes:
        state (Literal['unavailable']):
        provider (Literal['previewfile']):
        reason (UnavailableFilePreviewReason):
        retryable (bool):
    """

    state: Literal["unavailable"]
    provider: Literal["previewfile"]
    reason: UnavailableFilePreviewReason
    retryable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        provider = self.provider

        reason: str = self.reason

        retryable = self.retryable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "provider": provider,
                "reason": reason,
                "retryable": retryable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        state = cast(Literal["unavailable"], d.pop("state"))
        if state != "unavailable":
            raise ValueError(f"state must match const 'unavailable', got '{state}'")

        provider = cast(Literal["previewfile"], d.pop("provider"))
        if provider != "previewfile":
            raise ValueError(f"provider must match const 'previewfile', got '{provider}'")

        reason = check_unavailable_file_preview_reason(d.pop("reason"))

        retryable = d.pop("retryable")

        unavailable_file_preview = cls(
            state=state,
            provider=provider,
            reason=reason,
            retryable=retryable,
        )

        unavailable_file_preview.additional_properties = d
        return unavailable_file_preview

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
