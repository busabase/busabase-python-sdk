from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bases_field_change_request_body_patch_options_formula_format import (
    BasesFieldChangeRequestBodyPatchOptionsFormulaFormat,
    check_bases_field_change_request_body_patch_options_formula_format,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BasesFieldChangeRequestBodyPatchOptionsFormula")


@_attrs_define
class BasesFieldChangeRequestBodyPatchOptionsFormula:
    """
    Attributes:
        expression (str):
        format_ (BasesFieldChangeRequestBodyPatchOptionsFormulaFormat | Unset):
        precision (int | Unset):
        currency (str | Unset):
    """

    expression: str
    format_: BasesFieldChangeRequestBodyPatchOptionsFormulaFormat | Unset = UNSET
    precision: int | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expression = self.expression

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        precision = self.precision

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expression": expression,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if precision is not UNSET:
            field_dict["precision"] = precision
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        expression = d.pop("expression")

        _format_ = d.pop("format", UNSET)
        format_: BasesFieldChangeRequestBodyPatchOptionsFormulaFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_bases_field_change_request_body_patch_options_formula_format(_format_)

        precision = d.pop("precision", UNSET)

        currency = d.pop("currency", UNSET)

        bases_field_change_request_body_patch_options_formula = cls(
            expression=expression,
            format_=format_,
            precision=precision,
            currency=currency,
        )

        bases_field_change_request_body_patch_options_formula.additional_properties = d
        return bases_field_change_request_body_patch_options_formula

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
