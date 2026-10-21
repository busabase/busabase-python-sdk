from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vault_item_environment import VaultItemEnvironment, check_vault_item_environment
from ..models.vault_item_kind import VaultItemKind, check_vault_item_kind
from ..models.vault_item_scope_type import VaultItemScopeType, check_vault_item_scope_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vault_item_access import VaultItemAccess


T = TypeVar("T", bound="VaultItem")


@_attrs_define
class VaultItem:
    """
    Attributes:
        id (str):
        kind (VaultItemKind):
        key (str):
        value (str):
        scope_id (None | str):
        updated_at (str):
        created_at (str):
        last_used_at (None | str):
        scope_type (VaultItemScopeType | Unset):  Default: 'personal'.
        environment (VaultItemEnvironment | Unset):  Default: 'local'.
        description (str | Unset):  Default: ''.
        access (VaultItemAccess | Unset):
    """

    id: str
    kind: VaultItemKind
    key: str
    value: str
    scope_id: None | str
    updated_at: str
    created_at: str
    last_used_at: None | str
    scope_type: VaultItemScopeType | Unset = "personal"
    environment: VaultItemEnvironment | Unset = "local"
    description: str | Unset = ""
    access: VaultItemAccess | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind: str = self.kind

        key = self.key

        value = self.value

        scope_id: None | str
        scope_id = self.scope_id

        updated_at = self.updated_at

        created_at = self.created_at

        last_used_at: None | str
        last_used_at = self.last_used_at

        scope_type: str | Unset = UNSET
        if not isinstance(self.scope_type, Unset):
            scope_type = self.scope_type

        environment: str | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment

        description = self.description

        access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "key": key,
                "value": value,
                "scopeId": scope_id,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "lastUsedAt": last_used_at,
            }
        )
        if scope_type is not UNSET:
            field_dict["scopeType"] = scope_type
        if environment is not UNSET:
            field_dict["environment"] = environment
        if description is not UNSET:
            field_dict["description"] = description
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vault_item_access import VaultItemAccess

        d = dict(src_dict)
        id = d.pop("id")

        kind = check_vault_item_kind(d.pop("kind"))

        key = d.pop("key")

        value = d.pop("value")

        def _parse_scope_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        scope_id = _parse_scope_id(d.pop("scopeId"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        def _parse_last_used_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_used_at = _parse_last_used_at(d.pop("lastUsedAt"))

        _scope_type = d.pop("scopeType", UNSET)
        scope_type: VaultItemScopeType | Unset
        if isinstance(_scope_type, Unset):
            scope_type = UNSET
        else:
            scope_type = check_vault_item_scope_type(_scope_type)

        _environment = d.pop("environment", UNSET)
        environment: VaultItemEnvironment | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = check_vault_item_environment(_environment)

        description = d.pop("description", UNSET)

        _access = d.pop("access", UNSET)
        access: VaultItemAccess | Unset
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = VaultItemAccess.from_dict(_access)

        vault_item = cls(
            id=id,
            kind=kind,
            key=key,
            value=value,
            scope_id=scope_id,
            updated_at=updated_at,
            created_at=created_at,
            last_used_at=last_used_at,
            scope_type=scope_type,
            environment=environment,
            description=description,
            access=access,
        )

        vault_item.additional_properties = d
        return vault_item

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
