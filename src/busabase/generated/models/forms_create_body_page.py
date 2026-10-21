from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.forms_create_body_page_theme import FormsCreateBodyPageTheme


T = TypeVar("T", bound="FormsCreateBodyPage")


@_attrs_define
class FormsCreateBodyPage:
    """
    Attributes:
        code (str | Unset):
        theme (FormsCreateBodyPageTheme | Unset):
    """

    code: str | Unset = UNSET
    theme: FormsCreateBodyPageTheme | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        theme: dict[str, Any] | Unset = UNSET
        if not isinstance(self.theme, Unset):
            theme = self.theme.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if theme is not UNSET:
            field_dict["theme"] = theme

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.forms_create_body_page_theme import FormsCreateBodyPageTheme

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _theme = d.pop("theme", UNSET)
        theme: FormsCreateBodyPageTheme | Unset
        if isinstance(_theme, Unset):
            theme = UNSET
        else:
            theme = FormsCreateBodyPageTheme.from_dict(_theme)

        forms_create_body_page = cls(
            code=code,
            theme=theme,
        )

        forms_create_body_page.additional_properties = d
        return forms_create_body_page

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
