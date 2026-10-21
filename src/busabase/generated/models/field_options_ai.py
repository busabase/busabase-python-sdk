from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldOptionsAi")


@_attrs_define
class FieldOptionsAi:
    """
    Attributes:
        model (str | Unset):
        prompt (str | Unset):
        review_required (bool | Unset):
        source_field_ids (list[str] | Unset):
    """

    model: str | Unset = UNSET
    prompt: str | Unset = UNSET
    review_required: bool | Unset = UNSET
    source_field_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        prompt = self.prompt

        review_required = self.review_required

        source_field_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_field_ids, Unset):
            source_field_ids = self.source_field_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if review_required is not UNSET:
            field_dict["reviewRequired"] = review_required
        if source_field_ids is not UNSET:
            field_dict["sourceFieldIds"] = source_field_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        model = d.pop("model", UNSET)

        prompt = d.pop("prompt", UNSET)

        review_required = d.pop("reviewRequired", UNSET)

        source_field_ids = cast(list[str], d.pop("sourceFieldIds", UNSET))

        field_options_ai = cls(
            model=model,
            prompt=prompt,
            review_required=review_required,
            source_field_ids=source_field_ids,
        )

        field_options_ai.additional_properties = d
        return field_options_ai

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
