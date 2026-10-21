from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbedFramePolicyAnywhere")


@_attrs_define
class EmbedFramePolicyAnywhere:
    """
    Attributes:
        mode (Literal['anywhere']):
        allowed_origins (list[str] | Unset):
    """

    mode: Literal["anywhere"]
    allowed_origins: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        allowed_origins: list[str] | Unset = UNSET
        if not isinstance(self.allowed_origins, Unset):
            allowed_origins = self.allowed_origins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if allowed_origins is not UNSET:
            field_dict["allowedOrigins"] = allowed_origins

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = cast(Literal["anywhere"], d.pop("mode"))
        if mode != "anywhere":
            raise ValueError(f"mode must match const 'anywhere', got '{mode}'")

        allowed_origins = cast(list[str], d.pop("allowedOrigins", UNSET))

        embed_frame_policy_anywhere = cls(
            mode=mode,
            allowed_origins=allowed_origins,
        )

        embed_frame_policy_anywhere.additional_properties = d
        return embed_frame_policy_anywhere

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
