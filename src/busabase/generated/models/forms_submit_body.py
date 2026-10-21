from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.forms_submit_body_values import FormsSubmitBodyValues


T = TypeVar("T", bound="FormsSubmitBody")


@_attrs_define
class FormsSubmitBody:
    """
    Attributes:
        values (FormsSubmitBodyValues):
        captcha_token (str | Unset):
    """

    values: FormsSubmitBodyValues
    captcha_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values = self.values.to_dict()

        captcha_token = self.captcha_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "values": values,
            }
        )
        if captcha_token is not UNSET:
            field_dict["captchaToken"] = captcha_token

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.forms_submit_body_values import FormsSubmitBodyValues

        d = dict(src_dict)
        values = FormsSubmitBodyValues.from_dict(d.pop("values"))

        captcha_token = d.pop("captchaToken", UNSET)

        forms_submit_body = cls(
            values=values,
            captcha_token=captcha_token,
        )

        forms_submit_body.additional_properties = d
        return forms_submit_body

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
