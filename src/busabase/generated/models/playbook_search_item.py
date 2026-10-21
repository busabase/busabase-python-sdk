from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.playbook_search_item_intent import PlaybookSearchItemIntent, check_playbook_search_item_intent
from ..models.playbook_search_item_kind import PlaybookSearchItemKind, check_playbook_search_item_kind
from ..models.playbook_search_item_matched_on_item import (
    PlaybookSearchItemMatchedOnItem,
    check_playbook_search_item_matched_on_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaybookSearchItem")


@_attrs_define
class PlaybookSearchItem:
    """
    Attributes:
        kind (PlaybookSearchItemKind):
        node_id (str):
        node_type (str):
        node_name (str):
        node_slug (str):
        path (list[str]):
        matched_on (list[PlaybookSearchItemMatchedOnItem]):
        score (float):
        updated_at (str):
        key (str | Unset):
        label (str | Unset):
        intent (PlaybookSearchItemIntent | Unset):
        name (str | Unset):
        description (str | Unset):
    """

    kind: PlaybookSearchItemKind
    node_id: str
    node_type: str
    node_name: str
    node_slug: str
    path: list[str]
    matched_on: list[PlaybookSearchItemMatchedOnItem]
    score: float
    updated_at: str
    key: str | Unset = UNSET
    label: str | Unset = UNSET
    intent: PlaybookSearchItemIntent | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        node_id = self.node_id

        node_type = self.node_type

        node_name = self.node_name

        node_slug = self.node_slug

        path = self.path

        matched_on = []
        for matched_on_item_data in self.matched_on:
            matched_on_item: str = matched_on_item_data
            matched_on.append(matched_on_item)

        score = self.score

        updated_at = self.updated_at

        key = self.key

        label = self.label

        intent: str | Unset = UNSET
        if not isinstance(self.intent, Unset):
            intent = self.intent

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "nodeId": node_id,
                "nodeType": node_type,
                "nodeName": node_name,
                "nodeSlug": node_slug,
                "path": path,
                "matchedOn": matched_on,
                "score": score,
                "updatedAt": updated_at,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label
        if intent is not UNSET:
            field_dict["intent"] = intent
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_playbook_search_item_kind(d.pop("kind"))

        node_id = d.pop("nodeId")

        node_type = d.pop("nodeType")

        node_name = d.pop("nodeName")

        node_slug = d.pop("nodeSlug")

        path = cast(list[str], d.pop("path"))

        matched_on = []
        _matched_on = d.pop("matchedOn")
        for matched_on_item_data in _matched_on:
            matched_on_item = check_playbook_search_item_matched_on_item(matched_on_item_data)

            matched_on.append(matched_on_item)

        score = d.pop("score")

        updated_at = d.pop("updatedAt")

        key = d.pop("key", UNSET)

        label = d.pop("label", UNSET)

        _intent = d.pop("intent", UNSET)
        intent: PlaybookSearchItemIntent | Unset
        if isinstance(_intent, Unset):
            intent = UNSET
        else:
            intent = check_playbook_search_item_intent(_intent)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        playbook_search_item = cls(
            kind=kind,
            node_id=node_id,
            node_type=node_type,
            node_name=node_name,
            node_slug=node_slug,
            path=path,
            matched_on=matched_on,
            score=score,
            updated_at=updated_at,
            key=key,
            label=label,
            intent=intent,
            name=name,
            description=description,
        )

        playbook_search_item.additional_properties = d
        return playbook_search_item

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
