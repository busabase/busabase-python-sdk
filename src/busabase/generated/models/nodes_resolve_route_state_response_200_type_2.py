from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NodesResolveRouteStateResponse200Type2")


@_attrs_define
class NodesResolveRouteStateResponse200Type2:
    """
    Attributes:
        status (Literal['unavailable']):
    """

    status: Literal["unavailable"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = cast(Literal["unavailable"], d.pop("status"))
        if status != "unavailable":
            raise ValueError(f"status must match const 'unavailable', got '{status}'")

        nodes_resolve_route_state_response_200_type_2 = cls(
            status=status,
        )

        nodes_resolve_route_state_response_200_type_2.additional_properties = d
        return nodes_resolve_route_state_response_200_type_2

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
