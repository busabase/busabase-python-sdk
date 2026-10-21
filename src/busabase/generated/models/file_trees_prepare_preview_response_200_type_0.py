from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FileTreesPreparePreviewResponse200Type0")


@_attrs_define
class FileTreesPreparePreviewResponse200Type0:
    """
    Attributes:
        state (Literal['builtin']):
        provider (Literal['builtin']):
    """

    state: Literal["builtin"]
    provider: Literal["builtin"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        state = cast(Literal["builtin"], d.pop("state"))
        if state != "builtin":
            raise ValueError(f"state must match const 'builtin', got '{state}'")

        provider = cast(Literal["builtin"], d.pop("provider"))
        if provider != "builtin":
            raise ValueError(f"provider must match const 'builtin', got '{provider}'")

        file_trees_prepare_preview_response_200_type_0 = cls(
            state=state,
            provider=provider,
        )

        file_trees_prepare_preview_response_200_type_0.additional_properties = d
        return file_trees_prepare_preview_response_200_type_0

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
