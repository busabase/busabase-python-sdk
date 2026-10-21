from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.view_config_sorts_item_direction import (
    ViewConfigSortsItemDirection,
    check_view_config_sorts_item_direction,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewConfigSortsItem")


@_attrs_define
class ViewConfigSortsItem:
    """
    Attributes:
        direction (ViewConfigSortsItemDirection):
        field_slug (str):
        field_id (str | Unset):
    """

    direction: ViewConfigSortsItemDirection
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
        direction = check_view_config_sorts_item_direction(d.pop("direction"))

        field_slug = d.pop("fieldSlug")

        field_id = d.pop("fieldId", UNSET)

        view_config_sorts_item = cls(
            direction=direction,
            field_slug=field_slug,
            field_id=field_id,
        )

        view_config_sorts_item.additional_properties = d
        return view_config_sorts_item

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
