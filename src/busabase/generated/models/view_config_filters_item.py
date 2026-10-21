from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.view_config_filters_item_operator import (
    ViewConfigFiltersItemOperator,
    check_view_config_filters_item_operator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewConfigFiltersItem")


@_attrs_define
class ViewConfigFiltersItem:
    """
    Attributes:
        field_slug (str):
        operator (ViewConfigFiltersItemOperator):
        field_id (str | Unset):
        value (Any | Unset):
    """

    field_slug: str
    operator: ViewConfigFiltersItemOperator
    field_id: str | Unset = UNSET
    value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_slug = self.field_slug

        operator: str = self.operator

        field_id = self.field_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldSlug": field_slug,
                "operator": operator,
            }
        )
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        field_slug = d.pop("fieldSlug")

        operator = check_view_config_filters_item_operator(d.pop("operator"))

        field_id = d.pop("fieldId", UNSET)

        value = d.pop("value", UNSET)

        view_config_filters_item = cls(
            field_slug=field_slug,
            operator=operator,
            field_id=field_id,
            value=value,
        )

        view_config_filters_item.additional_properties = d
        return view_config_filters_item

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
