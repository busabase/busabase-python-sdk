from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_options_embed_aspect_ratio import (
    FieldOptionsEmbedAspectRatio,
    check_field_options_embed_aspect_ratio,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldOptionsEmbed")


@_attrs_define
class FieldOptionsEmbed:
    """
    Attributes:
        aspect_ratio (FieldOptionsEmbedAspectRatio | Unset):
        height (int | Unset):
        providers (list[str] | Unset):
    """

    aspect_ratio: FieldOptionsEmbedAspectRatio | Unset = UNSET
    height: int | Unset = UNSET
    providers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aspect_ratio: str | Unset = UNSET
        if not isinstance(self.aspect_ratio, Unset):
            aspect_ratio = self.aspect_ratio

        height = self.height

        providers: list[str] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspect_ratio is not UNSET:
            field_dict["aspectRatio"] = aspect_ratio
        if height is not UNSET:
            field_dict["height"] = height
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _aspect_ratio = d.pop("aspectRatio", UNSET)
        aspect_ratio: FieldOptionsEmbedAspectRatio | Unset
        if isinstance(_aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = check_field_options_embed_aspect_ratio(_aspect_ratio)

        height = d.pop("height", UNSET)

        providers = cast(list[str], d.pop("providers", UNSET))

        field_options_embed = cls(
            aspect_ratio=aspect_ratio,
            height=height,
            providers=providers,
        )

        field_options_embed.additional_properties = d
        return field_options_embed

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
