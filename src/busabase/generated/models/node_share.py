from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_share_capability import NodeShareCapability, check_node_share_capability
from ..models.node_share_scope import NodeShareScope, check_node_share_scope

T = TypeVar("T", bound="NodeShare")


@_attrs_define
class NodeShare:
    """
    Attributes:
        node_id (str):
        scope (NodeShareScope):
        capability (NodeShareCapability):
        has_password (bool):
        expires_at (None | str):
        updated_at (str):
    """

    node_id: str
    scope: NodeShareScope
    capability: NodeShareCapability
    has_password: bool
    expires_at: None | str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        scope: str = self.scope

        capability: str = self.capability

        has_password = self.has_password

        expires_at: None | str
        expires_at = self.expires_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeId": node_id,
                "scope": scope,
                "capability": capability,
                "hasPassword": has_password,
                "expiresAt": expires_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        node_id = d.pop("nodeId")

        scope = check_node_share_scope(d.pop("scope"))

        capability = check_node_share_capability(d.pop("capability"))

        has_password = d.pop("hasPassword")

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        updated_at = d.pop("updatedAt")

        node_share = cls(
            node_id=node_id,
            scope=scope,
            capability=capability,
            has_password=has_password,
            expires_at=expires_at,
            updated_at=updated_at,
        )

        node_share.additional_properties = d
        return node_share

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
