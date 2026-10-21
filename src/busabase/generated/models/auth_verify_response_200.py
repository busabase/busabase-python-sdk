from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_verify_response_200_credential_permission_level import (
    AuthVerifyResponse200CredentialPermissionLevel,
    check_auth_verify_response_200_credential_permission_level,
)
from ..models.auth_verify_response_200_effective_permission_level import (
    AuthVerifyResponse200EffectivePermissionLevel,
    check_auth_verify_response_200_effective_permission_level,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_verify_response_200_member import AuthVerifyResponse200Member
    from ..models.auth_verify_response_200_space import AuthVerifyResponse200Space
    from ..models.auth_verify_response_200_spaces_item import AuthVerifyResponse200SpacesItem
    from ..models.auth_verify_response_200_user import AuthVerifyResponse200User


T = TypeVar("T", bound="AuthVerifyResponse200")


@_attrs_define
class AuthVerifyResponse200:
    """
    Attributes:
        space (AuthVerifyResponse200Space):
        user (AuthVerifyResponse200User):
        member (AuthVerifyResponse200Member):
        spaces (list[AuthVerifyResponse200SpacesItem]):
        created_space (bool | Unset):
        bootstrap_required (bool | Unset):
        credential_permission_level (AuthVerifyResponse200CredentialPermissionLevel | Unset):
        effective_permission_level (AuthVerifyResponse200EffectivePermissionLevel | Unset):
    """

    space: AuthVerifyResponse200Space
    user: AuthVerifyResponse200User
    member: AuthVerifyResponse200Member
    spaces: list[AuthVerifyResponse200SpacesItem]
    created_space: bool | Unset = UNSET
    bootstrap_required: bool | Unset = UNSET
    credential_permission_level: AuthVerifyResponse200CredentialPermissionLevel | Unset = UNSET
    effective_permission_level: AuthVerifyResponse200EffectivePermissionLevel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        space = self.space.to_dict()

        user = self.user.to_dict()

        member = self.member.to_dict()

        spaces = []
        for spaces_item_data in self.spaces:
            spaces_item = spaces_item_data.to_dict()
            spaces.append(spaces_item)

        created_space = self.created_space

        bootstrap_required = self.bootstrap_required

        credential_permission_level: str | Unset = UNSET
        if not isinstance(self.credential_permission_level, Unset):
            credential_permission_level = self.credential_permission_level

        effective_permission_level: str | Unset = UNSET
        if not isinstance(self.effective_permission_level, Unset):
            effective_permission_level = self.effective_permission_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "space": space,
                "user": user,
                "member": member,
                "spaces": spaces,
            }
        )
        if created_space is not UNSET:
            field_dict["createdSpace"] = created_space
        if bootstrap_required is not UNSET:
            field_dict["bootstrapRequired"] = bootstrap_required
        if credential_permission_level is not UNSET:
            field_dict["credentialPermissionLevel"] = credential_permission_level
        if effective_permission_level is not UNSET:
            field_dict["effectivePermissionLevel"] = effective_permission_level

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_verify_response_200_member import AuthVerifyResponse200Member
        from ..models.auth_verify_response_200_space import AuthVerifyResponse200Space
        from ..models.auth_verify_response_200_spaces_item import AuthVerifyResponse200SpacesItem
        from ..models.auth_verify_response_200_user import AuthVerifyResponse200User

        d = dict(src_dict)
        space = AuthVerifyResponse200Space.from_dict(d.pop("space"))

        user = AuthVerifyResponse200User.from_dict(d.pop("user"))

        member = AuthVerifyResponse200Member.from_dict(d.pop("member"))

        spaces = []
        _spaces = d.pop("spaces")
        for spaces_item_data in _spaces:
            spaces_item = AuthVerifyResponse200SpacesItem.from_dict(spaces_item_data)

            spaces.append(spaces_item)

        created_space = d.pop("createdSpace", UNSET)

        bootstrap_required = d.pop("bootstrapRequired", UNSET)

        _credential_permission_level = d.pop("credentialPermissionLevel", UNSET)
        credential_permission_level: AuthVerifyResponse200CredentialPermissionLevel | Unset
        if isinstance(_credential_permission_level, Unset):
            credential_permission_level = UNSET
        else:
            credential_permission_level = check_auth_verify_response_200_credential_permission_level(
                _credential_permission_level
            )

        _effective_permission_level = d.pop("effectivePermissionLevel", UNSET)
        effective_permission_level: AuthVerifyResponse200EffectivePermissionLevel | Unset
        if isinstance(_effective_permission_level, Unset):
            effective_permission_level = UNSET
        else:
            effective_permission_level = check_auth_verify_response_200_effective_permission_level(
                _effective_permission_level
            )

        auth_verify_response_200 = cls(
            space=space,
            user=user,
            member=member,
            spaces=spaces,
            created_space=created_space,
            bootstrap_required=bootstrap_required,
            credential_permission_level=credential_permission_level,
            effective_permission_level=effective_permission_level,
        )

        auth_verify_response_200.additional_properties = d
        return auth_verify_response_200

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
