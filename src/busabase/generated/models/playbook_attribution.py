from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.playbook_attribution_kind import PlaybookAttributionKind, check_playbook_attribution_kind

T = TypeVar("T", bound="PlaybookAttribution")


@_attrs_define
class PlaybookAttribution:
    """
    Attributes:
        kind (PlaybookAttributionKind):
        accessible (bool):
        node_id (None | str):
        key (None | str):
        node_type (None | str):
        node_slug (None | str):
        label (None | str):
    """

    kind: PlaybookAttributionKind
    accessible: bool
    node_id: None | str
    key: None | str
    node_type: None | str
    node_slug: None | str
    label: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        accessible = self.accessible

        node_id: None | str
        node_id = self.node_id

        key: None | str
        key = self.key

        node_type: None | str
        node_type = self.node_type

        node_slug: None | str
        node_slug = self.node_slug

        label: None | str
        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "accessible": accessible,
                "nodeId": node_id,
                "key": key,
                "nodeType": node_type,
                "nodeSlug": node_slug,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_playbook_attribution_kind(d.pop("kind"))

        accessible = d.pop("accessible")

        def _parse_node_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        node_id = _parse_node_id(d.pop("nodeId"))

        def _parse_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key = _parse_key(d.pop("key"))

        def _parse_node_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        node_type = _parse_node_type(d.pop("nodeType"))

        def _parse_node_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        node_slug = _parse_node_slug(d.pop("nodeSlug"))

        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))

        playbook_attribution = cls(
            kind=kind,
            accessible=accessible,
            node_id=node_id,
            key=key,
            node_type=node_type,
            node_slug=node_slug,
            label=label,
        )

        playbook_attribution.additional_properties = d
        return playbook_attribution

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
