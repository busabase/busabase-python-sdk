from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nodes_resolve_route_state_response_200_type_1_type import (
    NodesResolveRouteStateResponse200Type1Type,
    check_nodes_resolve_route_state_response_200_type_1_type,
)

T = TypeVar("T", bound="NodesResolveRouteStateResponse200Type1")


@_attrs_define
class NodesResolveRouteStateResponse200Type1:
    """
    Attributes:
        status (Literal['archived']):
        node_id (str):
        type_ (NodesResolveRouteStateResponse200Type1Type):
        name (str):
        slug (str):
        archived_at (str):
        can_restore (bool):
    """

    status: Literal["archived"]
    node_id: str
    type_: NodesResolveRouteStateResponse200Type1Type
    name: str
    slug: str
    archived_at: str
    can_restore: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        node_id = self.node_id

        type_: str = self.type_

        name = self.name

        slug = self.slug

        archived_at = self.archived_at

        can_restore = self.can_restore

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "nodeId": node_id,
                "type": type_,
                "name": name,
                "slug": slug,
                "archivedAt": archived_at,
                "canRestore": can_restore,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = cast(Literal["archived"], d.pop("status"))
        if status != "archived":
            raise ValueError(f"status must match const 'archived', got '{status}'")

        node_id = d.pop("nodeId")

        type_ = check_nodes_resolve_route_state_response_200_type_1_type(d.pop("type"))

        name = d.pop("name")

        slug = d.pop("slug")

        archived_at = d.pop("archivedAt")

        can_restore = d.pop("canRestore")

        nodes_resolve_route_state_response_200_type_1 = cls(
            status=status,
            node_id=node_id,
            type_=type_,
            name=name,
            slug=slug,
            archived_at=archived_at,
            can_restore=can_restore,
        )

        nodes_resolve_route_state_response_200_type_1.additional_properties = d
        return nodes_resolve_route_state_response_200_type_1

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
