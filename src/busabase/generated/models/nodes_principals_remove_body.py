from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nodes_principals_remove_body_principal_type import (
    NodesPrincipalsRemoveBodyPrincipalType,
    check_nodes_principals_remove_body_principal_type,
)

T = TypeVar("T", bound="NodesPrincipalsRemoveBody")


@_attrs_define
class NodesPrincipalsRemoveBody:
    """
    Attributes:
        principal_type (NodesPrincipalsRemoveBodyPrincipalType):
        principal_id (str):
    """

    principal_type: NodesPrincipalsRemoveBodyPrincipalType
    principal_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        principal_type: str = self.principal_type

        principal_id = self.principal_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "principalType": principal_type,
                "principalId": principal_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        principal_type = check_nodes_principals_remove_body_principal_type(d.pop("principalType"))

        principal_id = d.pop("principalId")

        nodes_principals_remove_body = cls(
            principal_type=principal_type,
            principal_id=principal_id,
        )

        nodes_principals_remove_body.additional_properties = d
        return nodes_principals_remove_body

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
