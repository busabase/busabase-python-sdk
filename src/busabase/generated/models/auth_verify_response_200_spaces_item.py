from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_verify_response_200_spaces_item_node_visibility_mode import (
    AuthVerifyResponse200SpacesItemNodeVisibilityMode,
    check_auth_verify_response_200_spaces_item_node_visibility_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthVerifyResponse200SpacesItem")


@_attrs_define
class AuthVerifyResponse200SpacesItem:
    """
    Attributes:
        id (str):
        name (str):
        slug (None | str):
        plan (None | str):
        node_visibility_mode (AuthVerifyResponse200SpacesItemNodeVisibilityMode | Unset):
    """

    id: str
    name: str
    slug: None | str
    plan: None | str
    node_visibility_mode: AuthVerifyResponse200SpacesItemNodeVisibilityMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug: None | str
        slug = self.slug

        plan: None | str
        plan = self.plan

        node_visibility_mode: str | Unset = UNSET
        if not isinstance(self.node_visibility_mode, Unset):
            node_visibility_mode = self.node_visibility_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "plan": plan,
            }
        )
        if node_visibility_mode is not UNSET:
            field_dict["nodeVisibilityMode"] = node_visibility_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_plan(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        plan = _parse_plan(d.pop("plan"))

        _node_visibility_mode = d.pop("nodeVisibilityMode", UNSET)
        node_visibility_mode: AuthVerifyResponse200SpacesItemNodeVisibilityMode | Unset
        if isinstance(_node_visibility_mode, Unset):
            node_visibility_mode = UNSET
        else:
            node_visibility_mode = check_auth_verify_response_200_spaces_item_node_visibility_mode(
                _node_visibility_mode
            )

        auth_verify_response_200_spaces_item = cls(
            id=id,
            name=name,
            slug=slug,
            plan=plan,
            node_visibility_mode=node_visibility_mode,
        )

        auth_verify_response_200_spaces_item.additional_properties = d
        return auth_verify_response_200_spaces_item

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
