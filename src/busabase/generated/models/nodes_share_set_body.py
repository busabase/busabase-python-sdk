from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nodes_share_set_body_capability import NodesShareSetBodyCapability, check_nodes_share_set_body_capability
from ..models.nodes_share_set_body_scope import NodesShareSetBodyScope, check_nodes_share_set_body_scope
from ..types import UNSET, Unset

T = TypeVar("T", bound="NodesShareSetBody")


@_attrs_define
class NodesShareSetBody:
    """
    Attributes:
        scope (NodesShareSetBodyScope):
        capability (NodesShareSetBodyCapability | Unset):
        password (None | str | Unset):
        expires_at (datetime.datetime | None | Unset):
    """

    scope: NodesShareSetBodyScope
    capability: NodesShareSetBodyCapability | Unset = UNSET
    password: None | str | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope: str = self.scope

        capability: str | Unset = UNSET
        if not isinstance(self.capability, Unset):
            capability = self.capability

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scope": scope,
            }
        )
        if capability is not UNSET:
            field_dict["capability"] = capability
        if password is not UNSET:
            field_dict["password"] = password
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        scope = check_nodes_share_set_body_scope(d.pop("scope"))

        _capability = d.pop("capability", UNSET)
        capability: NodesShareSetBodyCapability | Unset
        if isinstance(_capability, Unset):
            capability = UNSET
        else:
            capability = check_nodes_share_set_body_capability(_capability)

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        nodes_share_set_body = cls(
            scope=scope,
            capability=capability,
            password=password,
            expires_at=expires_at,
        )

        nodes_share_set_body.additional_properties = d
        return nodes_share_set_body

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
