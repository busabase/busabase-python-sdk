from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.views_change_request_body_type_1_config_sorts_item_direction import (
    ViewsChangeRequestBodyType1ConfigSortsItemDirection,
    check_views_change_request_body_type_1_config_sorts_item_direction,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewsChangeRequestBodyType1ConfigSortsItem")


@_attrs_define
class ViewsChangeRequestBodyType1ConfigSortsItem:
    """
    Attributes:
        direction (ViewsChangeRequestBodyType1ConfigSortsItemDirection):
        field_slug (str):
        field_id (str | Unset):
    """

    direction: ViewsChangeRequestBodyType1ConfigSortsItemDirection
    field_slug: str
    field_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direction: str = self.direction

        field_slug = self.field_slug

        field_id = self.field_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "direction": direction,
                "fieldSlug": field_slug,
            }
        )
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        direction = check_views_change_request_body_type_1_config_sorts_item_direction(d.pop("direction"))

        field_slug = d.pop("fieldSlug")

        field_id = d.pop("fieldId", UNSET)

        views_change_request_body_type_1_config_sorts_item = cls(
            direction=direction,
            field_slug=field_slug,
            field_id=field_id,
        )

        views_change_request_body_type_1_config_sorts_item.additional_properties = d
        return views_change_request_body_type_1_config_sorts_item

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
