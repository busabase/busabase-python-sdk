from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_icon_attachment import NodeIconAttachment
    from ..models.node_icon_emoji import NodeIconEmoji


T = TypeVar("T", bound="RenameNodeOperation")


@_attrs_define
class RenameNodeOperation:
    """
    Attributes:
        kind (Literal['rename']):
        node_id (str):
        slug (str | Unset):
        name (str | Unset):
        description (str | Unset):
        icon (NodeIconAttachment | NodeIconEmoji | None | Unset):
    """

    kind: Literal["rename"]
    node_id: str
    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    icon: NodeIconAttachment | NodeIconEmoji | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.node_icon_attachment import NodeIconAttachment
        from ..models.node_icon_emoji import NodeIconEmoji

        kind = self.kind

        node_id = self.node_id

        slug = self.slug

        name = self.name

        description = self.description

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
                "kind": kind,
                "nodeId": node_id,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.node_icon_attachment import NodeIconAttachment
        from ..models.node_icon_emoji import NodeIconEmoji

        d = dict(src_dict)
        kind = cast(Literal["rename"], d.pop("kind"))
        if kind != "rename":
            raise ValueError(f"kind must match const 'rename', got '{kind}'")

        node_id = d.pop("nodeId")

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

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

        rename_node_operation = cls(
            kind=kind,
            node_id=node_id,
            slug=slug,
            name=name,
            description=description,
            icon=icon,
        )

        rename_node_operation.additional_properties = d
        return rename_node_operation

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
