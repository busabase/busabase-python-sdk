from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsersMeResponse200")


@_attrs_define
class UsersMeResponse200:
    """
    Attributes:
        id (str):
        name (str):
        email (str):
        email_verified (bool):
        image (None | str):
        created_at (str):
    """

    id: str
    name: str
    email: str
    email_verified: bool
    image: None | str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        email = self.email

        email_verified = self.email_verified

        image: None | str
        image = self.image

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "email": email,
                "emailVerified": email_verified,
                "image": image,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        email = d.pop("email")

        email_verified = d.pop("emailVerified")

        def _parse_image(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image = _parse_image(d.pop("image"))

        created_at = d.pop("createdAt")

        users_me_response_200 = cls(
            id=id,
            name=name,
            email=email,
            email_verified=email_verified,
            image=image,
            created_at=created_at,
        )

        users_me_response_200.additional_properties = d
        return users_me_response_200

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
