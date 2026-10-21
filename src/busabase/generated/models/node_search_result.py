from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_search_result_type import NodeSearchResultType, check_node_search_result_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_icon_attachment import NodeIconAttachment
    from ..models.node_icon_emoji import NodeIconEmoji


T = TypeVar("T", bound="NodeSearchResult")


@_attrs_define
class NodeSearchResult:
    """
    Attributes:
        id (str):
        type_ (NodeSearchResultType):
        name (str):
        slug (str):
        path (str):
        updated_at (str):
        icon (NodeIconAttachment | NodeIconEmoji | None | Unset):
    """

    id: str
    type_: NodeSearchResultType
    name: str
    slug: str
    path: str
    updated_at: str
    icon: NodeIconAttachment | NodeIconEmoji | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.node_icon_attachment import NodeIconAttachment
        from ..models.node_icon_emoji import NodeIconEmoji

        id = self.id

        type_: str = self.type_

        name = self.name

        slug = self.slug

        path = self.path

        updated_at = self.updated_at

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
                "id": id,
                "type": type_,
                "name": name,
                "slug": slug,
                "path": path,
                "updatedAt": updated_at,
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
        id = d.pop("id")

        type_ = check_node_search_result_type(d.pop("type"))

        name = d.pop("name")

        slug = d.pop("slug")

        path = d.pop("path")

        updated_at = d.pop("updatedAt")

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

        node_search_result = cls(
            id=id,
            type_=type_,
            name=name,
            slug=slug,
            path=path,
            updated_at=updated_at,
            icon=icon,
        )

        node_search_result.additional_properties = d
        return node_search_result

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
