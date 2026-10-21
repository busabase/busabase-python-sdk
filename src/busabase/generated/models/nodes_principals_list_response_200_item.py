from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nodes_principals_list_response_200_item_principal_type import (
    NodesPrincipalsListResponse200ItemPrincipalType,
    check_nodes_principals_list_response_200_item_principal_type,
)
from ..models.nodes_principals_list_response_200_item_role import (
    NodesPrincipalsListResponse200ItemRole,
    check_nodes_principals_list_response_200_item_role,
)

T = TypeVar("T", bound="NodesPrincipalsListResponse200Item")


@_attrs_define
class NodesPrincipalsListResponse200Item:
    """
    Attributes:
        id (str):
        node_id (str):
        principal_type (NodesPrincipalsListResponse200ItemPrincipalType):
        principal_id (str):
        role (NodesPrincipalsListResponse200ItemRole):
        granted_by (str):
        created_at (str):
        updated_at (str):
    """

    id: str
    node_id: str
    principal_type: NodesPrincipalsListResponse200ItemPrincipalType
    principal_id: str
    role: NodesPrincipalsListResponse200ItemRole
    granted_by: str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        node_id = self.node_id

        principal_type: str = self.principal_type

        principal_id = self.principal_id

        role: str = self.role

        granted_by = self.granted_by

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nodeId": node_id,
                "principalType": principal_type,
                "principalId": principal_id,
                "role": role,
                "grantedBy": granted_by,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        node_id = d.pop("nodeId")

        principal_type = check_nodes_principals_list_response_200_item_principal_type(d.pop("principalType"))

        principal_id = d.pop("principalId")

        role = check_nodes_principals_list_response_200_item_role(d.pop("role"))

        granted_by = d.pop("grantedBy")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        nodes_principals_list_response_200_item = cls(
            id=id,
            node_id=node_id,
            principal_type=principal_type,
            principal_id=principal_id,
            role=role,
            granted_by=granted_by,
            created_at=created_at,
            updated_at=updated_at,
        )

        nodes_principals_list_response_200_item.additional_properties = d
        return nodes_principals_list_response_200_item

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
