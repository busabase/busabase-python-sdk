from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmbedLinksCreateBodyFramePolicyType1")


@_attrs_define
class EmbedLinksCreateBodyFramePolicyType1:
    """
    Attributes:
        mode (Literal['origins']):
        allowed_origins (list[str]):
    """

    mode: Literal["origins"]
    allowed_origins: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        allowed_origins = self.allowed_origins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "allowedOrigins": allowed_origins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = cast(Literal["origins"], d.pop("mode"))
        if mode != "origins":
            raise ValueError(f"mode must match const 'origins', got '{mode}'")

        allowed_origins = cast(list[str], d.pop("allowedOrigins"))

        embed_links_create_body_frame_policy_type_1 = cls(
            mode=mode,
            allowed_origins=allowed_origins,
        )

        embed_links_create_body_frame_policy_type_1.additional_properties = d
        return embed_links_create_body_frame_policy_type_1

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
