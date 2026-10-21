from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_options_number_format import FieldOptionsNumberFormat, check_field_options_number_format
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldOptionsNumber")


@_attrs_define
class FieldOptionsNumber:
    """
    Attributes:
        format_ (FieldOptionsNumberFormat | Unset):
        currency (str | Unset):
        locale (str | Unset):
    """

    format_: FieldOptionsNumberFormat | Unset = UNSET
    currency: str | Unset = UNSET
    locale: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        currency = self.currency

        locale = self.locale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if currency is not UNSET:
            field_dict["currency"] = currency
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _format_ = d.pop("format", UNSET)
        format_: FieldOptionsNumberFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_field_options_number_format(_format_)

        currency = d.pop("currency", UNSET)

        locale = d.pop("locale", UNSET)

        field_options_number = cls(
            format_=format_,
            currency=currency,
            locale=locale,
        )

        field_options_number.additional_properties = d
        return field_options_number

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
