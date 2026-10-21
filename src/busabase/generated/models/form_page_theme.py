from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormPageTheme")


@_attrs_define
class FormPageTheme:
    """
    Attributes:
        logo_url (str | Unset):
        cover_url (str | Unset):
        brand_color (str | Unset):
        hide_branding (bool | Unset):
    """

    logo_url: str | Unset = UNSET
    cover_url: str | Unset = UNSET
    brand_color: str | Unset = UNSET
    hide_branding: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logo_url = self.logo_url

        cover_url = self.cover_url

        brand_color = self.brand_color

        hide_branding = self.hide_branding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if cover_url is not UNSET:
            field_dict["coverUrl"] = cover_url
        if brand_color is not UNSET:
            field_dict["brandColor"] = brand_color
        if hide_branding is not UNSET:
            field_dict["hideBranding"] = hide_branding

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        logo_url = d.pop("logoUrl", UNSET)

        cover_url = d.pop("coverUrl", UNSET)

        brand_color = d.pop("brandColor", UNSET)

        hide_branding = d.pop("hideBranding", UNSET)

        form_page_theme = cls(
            logo_url=logo_url,
            cover_url=cover_url,
            brand_color=brand_color,
            hide_branding=hide_branding,
        )

        form_page_theme.additional_properties = d
        return form_page_theme

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
