from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.playbooks_search_body_kinds_item import (
    PlaybooksSearchBodyKindsItem,
    check_playbooks_search_body_kinds_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaybooksSearchBody")


@_attrs_define
class PlaybooksSearchBody:
    """
    Attributes:
        queries (list[str] | Unset): 2–5 phrasings of what the user wants, in the user's language AND in English (e.g.
            ["记录客户拜访", "log customer visit", "visit"]). Each is matched as a case-insensitive substring; an item hit by more
            phrasings ranks higher. Empty = browse: every playbook, nearest first (at most 30).
        kinds (list[PlaybooksSearchBodyKindsItem] | Unset): Restrict to "skill" and/or "prompt". Default: both.
        near_node_id (str | Unset): The node the user is on. Playbooks on that node rank first, then its folder, then
            ancestor folders (closest first).
        in_node_id (str | Unset): Only return playbooks on this node or inside its subtree.
        limit (int | Unset): Max items (1–50). Default 10 for a search; 30 for a browse.
        locale (str | Unset): Locale for prompt labels and the rendered prompt body, e.g. "en" or "zh-CN". Falls back to
            English, then to whatever locale the prompt has.
    """

    queries: list[str] | Unset = UNSET
    kinds: list[PlaybooksSearchBodyKindsItem] | Unset = UNSET
    near_node_id: str | Unset = UNSET
    in_node_id: str | Unset = UNSET
    limit: int | Unset = UNSET
    locale: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        queries: list[str] | Unset = UNSET
        if not isinstance(self.queries, Unset):
            queries = self.queries

        kinds: list[str] | Unset = UNSET
        if not isinstance(self.kinds, Unset):
            kinds = []
            for kinds_item_data in self.kinds:
                kinds_item: str = kinds_item_data
                kinds.append(kinds_item)

        near_node_id = self.near_node_id

        in_node_id = self.in_node_id

        limit = self.limit

        locale = self.locale

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if queries is not UNSET:
            field_dict["queries"] = queries
        if kinds is not UNSET:
            field_dict["kinds"] = kinds
        if near_node_id is not UNSET:
            field_dict["nearNodeId"] = near_node_id
        if in_node_id is not UNSET:
            field_dict["inNodeId"] = in_node_id
        if limit is not UNSET:
            field_dict["limit"] = limit
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        queries = cast(list[str], d.pop("queries", UNSET))

        _kinds = d.pop("kinds", UNSET)
        kinds: list[PlaybooksSearchBodyKindsItem] | Unset = UNSET
        if _kinds is not UNSET:
            kinds = []
            for kinds_item_data in _kinds:
                kinds_item = check_playbooks_search_body_kinds_item(kinds_item_data)

                kinds.append(kinds_item)

        near_node_id = d.pop("nearNodeId", UNSET)

        in_node_id = d.pop("inNodeId", UNSET)

        limit = d.pop("limit", UNSET)

        locale = d.pop("locale", UNSET)

        playbooks_search_body = cls(
            queries=queries,
            kinds=kinds,
            near_node_id=near_node_id,
            in_node_id=in_node_id,
            limit=limit,
            locale=locale,
        )

        return playbooks_search_body
