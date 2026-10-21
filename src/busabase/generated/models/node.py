from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_explicit_visibility_type_0 import NodeExplicitVisibilityType0, check_node_explicit_visibility_type_0
from ..models.node_type import NodeType, check_node_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_icon_attachment import NodeIconAttachment
    from ..models.node_icon_emoji import NodeIconEmoji
    from ..models.node_metadata import NodeMetadata
    from ..models.node_settings import NodeSettings


T = TypeVar("T", bound="Node")


@_attrs_define
class Node:
    """
    Attributes:
        id (str):
        parent_id (None | str):
        type_ (NodeType):
        slug (str):
        name (str):
        description (str):
        position (float):
        created_at (str):
        updated_at (str):
        base_id (None | str):
        children (list[Node]):
        metadata (NodeMetadata | Unset):
        settings (NodeSettings | Unset):
        explicit_visibility (NodeExplicitVisibilityType0 | None | Unset):
        icon (NodeIconAttachment | NodeIconEmoji | None | Unset):
        has_children (bool | Unset):
        shared (bool | Unset):
        shared_via_ancestor (bool | Unset):
    """

    id: str
    parent_id: None | str
    type_: NodeType
    slug: str
    name: str
    description: str
    position: float
    created_at: str
    updated_at: str
    base_id: None | str
    children: list[Node]
    metadata: NodeMetadata | Unset = UNSET
    settings: NodeSettings | Unset = UNSET
    explicit_visibility: NodeExplicitVisibilityType0 | None | Unset = UNSET
    icon: NodeIconAttachment | NodeIconEmoji | None | Unset = UNSET
    has_children: bool | Unset = UNSET
    shared: bool | Unset = UNSET
    shared_via_ancestor: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.node_icon_attachment import NodeIconAttachment
        from ..models.node_icon_emoji import NodeIconEmoji

        id = self.id

        parent_id: None | str
        parent_id = self.parent_id

        type_: str = self.type_

        slug = self.slug

        name = self.name

        description = self.description

        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        base_id: None | str
        base_id = self.base_id

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        explicit_visibility: None | str | Unset
        if isinstance(self.explicit_visibility, Unset):
            explicit_visibility = UNSET
        elif isinstance(self.explicit_visibility, str):
            explicit_visibility = self.explicit_visibility
        else:
            explicit_visibility = self.explicit_visibility

        icon: dict[str, Any] | None | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        elif isinstance(self.icon, NodeIconEmoji) or isinstance(self.icon, NodeIconAttachment):
            icon = self.icon.to_dict()
        else:
            icon = self.icon

        has_children = self.has_children

        shared = self.shared

        shared_via_ancestor = self.shared_via_ancestor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "parentId": parent_id,
                "type": type_,
                "slug": slug,
                "name": name,
                "description": description,
                "position": position,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "baseId": base_id,
                "children": children,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if settings is not UNSET:
            field_dict["settings"] = settings
        if explicit_visibility is not UNSET:
            field_dict["explicitVisibility"] = explicit_visibility
        if icon is not UNSET:
            field_dict["icon"] = icon
        if has_children is not UNSET:
            field_dict["hasChildren"] = has_children
        if shared is not UNSET:
            field_dict["shared"] = shared
        if shared_via_ancestor is not UNSET:
            field_dict["sharedViaAncestor"] = shared_via_ancestor

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.node_icon_attachment import NodeIconAttachment
        from ..models.node_icon_emoji import NodeIconEmoji
        from ..models.node_metadata import NodeMetadata
        from ..models.node_settings import NodeSettings

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_parent_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_id = _parse_parent_id(d.pop("parentId"))

        type_ = check_node_type(d.pop("type"))

        slug = d.pop("slug")

        name = d.pop("name")

        description = d.pop("description")

        position = d.pop("position")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_base_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        base_id = _parse_base_id(d.pop("baseId"))

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = Node.from_dict(children_item_data)

            children.append(children_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: NodeMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = NodeMetadata.from_dict(_metadata)

        _settings = d.pop("settings", UNSET)
        settings: NodeSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = NodeSettings.from_dict(_settings)

        def _parse_explicit_visibility(data: object) -> NodeExplicitVisibilityType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                explicit_visibility_type_0 = check_node_explicit_visibility_type_0(data)

                return explicit_visibility_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NodeExplicitVisibilityType0 | None | Unset, data)

        explicit_visibility = _parse_explicit_visibility(d.pop("explicitVisibility", UNSET))

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

        has_children = d.pop("hasChildren", UNSET)

        shared = d.pop("shared", UNSET)

        shared_via_ancestor = d.pop("sharedViaAncestor", UNSET)

        node = cls(
            id=id,
            parent_id=parent_id,
            type_=type_,
            slug=slug,
            name=name,
            description=description,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            base_id=base_id,
            children=children,
            metadata=metadata,
            settings=settings,
            explicit_visibility=explicit_visibility,
            icon=icon,
            has_children=has_children,
            shared=shared,
            shared_via_ancestor=shared_via_ancestor,
        )

        node.additional_properties = d
        return node

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
