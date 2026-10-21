from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nodes_share_list_response_200_item_capability import (
    NodesShareListResponse200ItemCapability,
    check_nodes_share_list_response_200_item_capability,
)
from ..models.nodes_share_list_response_200_item_type import (
    NodesShareListResponse200ItemType,
    check_nodes_share_list_response_200_item_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_icon_attachment import NodeIconAttachment
    from ..models.node_icon_emoji import NodeIconEmoji


T = TypeVar("T", bound="NodesShareListResponse200Item")


@_attrs_define
class NodesShareListResponse200Item:
    """
    Attributes:
        node_id (str):
        name (str):
        slug (str):
        type_ (NodesShareListResponse200ItemType):
        capability (NodesShareListResponse200ItemCapability):
        has_password (bool):
        expires_at (None | str):
        created_at (str):
        icon (NodeIconAttachment | NodeIconEmoji | None | Unset):
    """

    node_id: str
    name: str
    slug: str
    type_: NodesShareListResponse200ItemType
    capability: NodesShareListResponse200ItemCapability
    has_password: bool
    expires_at: None | str
    created_at: str
    icon: NodeIconAttachment | NodeIconEmoji | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.node_icon_attachment import NodeIconAttachment
        from ..models.node_icon_emoji import NodeIconEmoji

        node_id = self.node_id

        name = self.name

        slug = self.slug

        type_: str = self.type_

        capability: str = self.capability

        has_password = self.has_password

        expires_at: None | str
        expires_at = self.expires_at

        created_at = self.created_at

        icon: dict[str, Any] | None | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        elif isinstance(self.icon, NodeIconEmoji) or isinstance(self.icon, NodeIconAttachment):
            icon = self.icon.to_dict()
        else:
            icon = self.icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeId": node_id,
                "name": name,
                "slug": slug,
                "type": type_,
                "capability": capability,
                "hasPassword": has_password,
                "expiresAt": expires_at,
                "createdAt": created_at,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.node_icon_attachment import NodeIconAttachment
        from ..models.node_icon_emoji import NodeIconEmoji

        d = dict(src_dict)
        node_id = d.pop("nodeId")

        name = d.pop("name")

        slug = d.pop("slug")

        type_ = check_nodes_share_list_response_200_item_type(d.pop("type"))

        capability = check_nodes_share_list_response_200_item_capability(d.pop("capability"))

        has_password = d.pop("hasPassword")

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        created_at = d.pop("createdAt")

        def _parse_icon(data: object) -> NodeIconAttachment | NodeIconEmoji | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_icon_type_0 = NodeIconEmoji.from_dict(data)

                return componentsschemas_node_icon_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_node_icon_type_1 = NodeIconAttachment.from_dict(data)

                return componentsschemas_node_icon_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NodeIconAttachment | NodeIconEmoji | None | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        nodes_share_list_response_200_item = cls(
            node_id=node_id,
            name=name,
            slug=slug,
            type_=type_,
            capability=capability,
            has_password=has_password,
            expires_at=expires_at,
            created_at=created_at,
            icon=icon,
        )

        nodes_share_list_response_200_item.additional_properties = d
        return nodes_share_list_response_200_item

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
