from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bases_preview_field_conversion_body_new_type import (
    BasesPreviewFieldConversionBodyNewType,
    check_bases_preview_field_conversion_body_new_type,
)
from ..models.bases_preview_field_conversion_body_select_choice_mode import (
    BasesPreviewFieldConversionBodySelectChoiceMode,
    check_bases_preview_field_conversion_body_select_choice_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BasesPreviewFieldConversionBody")


@_attrs_define
class BasesPreviewFieldConversionBody:
    """
    Attributes:
        field_id (str):
        new_type (BasesPreviewFieldConversionBodyNewType):
        select_choice_mode (BasesPreviewFieldConversionBodySelectChoiceMode | Unset):  Default: 'null_on_missing'.
    """

    field_id: str
    new_type: BasesPreviewFieldConversionBodyNewType
    select_choice_mode: BasesPreviewFieldConversionBodySelectChoiceMode | Unset = "null_on_missing"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        new_type: str = self.new_type

        select_choice_mode: str | Unset = UNSET
        if not isinstance(self.select_choice_mode, Unset):
            select_choice_mode = self.select_choice_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldId": field_id,
                "newType": new_type,
            }
        )
        if select_choice_mode is not UNSET:
            field_dict["selectChoiceMode"] = select_choice_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        field_id = d.pop("fieldId")

        new_type = check_bases_preview_field_conversion_body_new_type(d.pop("newType"))

        _select_choice_mode = d.pop("selectChoiceMode", UNSET)
        select_choice_mode: BasesPreviewFieldConversionBodySelectChoiceMode | Unset
        if isinstance(_select_choice_mode, Unset):
            select_choice_mode = UNSET
        else:
            select_choice_mode = check_bases_preview_field_conversion_body_select_choice_mode(_select_choice_mode)

        bases_preview_field_conversion_body = cls(
            field_id=field_id,
            new_type=new_type,
            select_choice_mode=select_choice_mode,
        )

        bases_preview_field_conversion_body.additional_properties = d
        return bases_preview_field_conversion_body

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
