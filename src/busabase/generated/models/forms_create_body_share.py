from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormsCreateBodyShare")


@_attrs_define
class FormsCreateBodyShare:
    """
    Attributes:
        is_public (bool | Unset):  Default: False.
        anonymous_submit (bool | Unset):  Default: False.
        submit_limit (int | Unset):
        require_captcha (bool | Unset):
    """

    is_public: bool | Unset = False
    anonymous_submit: bool | Unset = False
    submit_limit: int | Unset = UNSET
    require_captcha: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_public = self.is_public

        anonymous_submit = self.anonymous_submit

        submit_limit = self.submit_limit

        require_captcha = self.require_captcha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if anonymous_submit is not UNSET:
            field_dict["anonymousSubmit"] = anonymous_submit
        if submit_limit is not UNSET:
            field_dict["submitLimit"] = submit_limit
        if require_captcha is not UNSET:
            field_dict["requireCaptcha"] = require_captcha

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        is_public = d.pop("isPublic", UNSET)

        anonymous_submit = d.pop("anonymousSubmit", UNSET)

        submit_limit = d.pop("submitLimit", UNSET)

        require_captcha = d.pop("requireCaptcha", UNSET)

        forms_create_body_share = cls(
            is_public=is_public,
            anonymous_submit=anonymous_submit,
            submit_limit=submit_limit,
            require_captcha=require_captcha,
        )

        forms_create_body_share.additional_properties = d
        return forms_create_body_share

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
