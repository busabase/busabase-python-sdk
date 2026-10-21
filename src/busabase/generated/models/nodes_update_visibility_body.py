from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nodes_update_visibility_body_visibility_type_0 import (
    NodesUpdateVisibilityBodyVisibilityType0,
    check_nodes_update_visibility_body_visibility_type_0,
)

T = TypeVar("T", bound="NodesUpdateVisibilityBody")


@_attrs_define
class NodesUpdateVisibilityBody:
    """
    Attributes:
        visibility (NodesUpdateVisibilityBodyVisibilityType0 | None):
    """

    visibility: NodesUpdateVisibilityBodyVisibilityType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visibility: None | str
        if isinstance(self.visibility, str):
            visibility = self.visibility
        else:
            visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visibility": visibility,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_visibility(data: object) -> NodesUpdateVisibilityBodyVisibilityType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                visibility_type_0 = check_nodes_update_visibility_body_visibility_type_0(data)

                return visibility_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NodesUpdateVisibilityBodyVisibilityType0 | None, data)

        visibility = _parse_visibility(d.pop("visibility"))

        nodes_update_visibility_body = cls(
            visibility=visibility,
        )

        nodes_update_visibility_body.additional_properties = d
        return nodes_update_visibility_body

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
