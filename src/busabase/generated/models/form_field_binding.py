from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormFieldBinding")


@_attrs_define
class FormFieldBinding:
    """
    Attributes:
        input_name (str):
        field_slug (str):
        required (bool | Unset):
        label (str | Unset):
        help_ (str | Unset):
    """

    input_name: str
    field_slug: str
    required: bool | Unset = UNSET
    label: str | Unset = UNSET
    help_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_name = self.input_name

        field_slug = self.field_slug

        required = self.required

        label = self.label

        help_ = self.help_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputName": input_name,
                "fieldSlug": field_slug,
            }
        )
        if required is not UNSET:
            field_dict["required"] = required
        if label is not UNSET:
            field_dict["label"] = label
        if help_ is not UNSET:
            field_dict["help"] = help_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        input_name = d.pop("inputName")

        field_slug = d.pop("fieldSlug")

        required = d.pop("required", UNSET)

        label = d.pop("label", UNSET)

        help_ = d.pop("help", UNSET)

        form_field_binding = cls(
            input_name=input_name,
            field_slug=field_slug,
            required=required,
            label=label,
            help_=help_,
        )

        form_field_binding.additional_properties = d
        return form_field_binding

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
