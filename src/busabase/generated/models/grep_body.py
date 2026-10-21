from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grep_body_sources_item import GrepBodySourcesItem, check_grep_body_sources_item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grep_body_scope import GrepBodyScope


T = TypeVar("T", bound="GrepBody")


@_attrs_define
class GrepBody:
    """
    Attributes:
        pattern (str):
        flags (str | Unset):  Default: ''.
        sources (list[GrepBodySourcesItem] | Unset):
        scope (GrepBodyScope | Unset):
        max_matches (int | Unset):  Default: 100.
        context_lines (int | Unset):  Default: 0.
    """

    pattern: str
    flags: str | Unset = ""
    sources: list[GrepBodySourcesItem] | Unset = UNSET
    scope: GrepBodyScope | Unset = UNSET
    max_matches: int | Unset = 100
    context_lines: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pattern = self.pattern

        flags = self.flags

        sources: list[str] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item: str = sources_item_data
                sources.append(sources_item)

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        max_matches = self.max_matches

        context_lines = self.context_lines

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pattern": pattern,
            }
        )
        if flags is not UNSET:
            field_dict["flags"] = flags
        if sources is not UNSET:
            field_dict["sources"] = sources
        if scope is not UNSET:
            field_dict["scope"] = scope
        if max_matches is not UNSET:
            field_dict["maxMatches"] = max_matches
        if context_lines is not UNSET:
            field_dict["contextLines"] = context_lines

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grep_body_scope import GrepBodyScope

        d = dict(src_dict)
        pattern = d.pop("pattern")

        flags = d.pop("flags", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[GrepBodySourcesItem] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = check_grep_body_sources_item(sources_item_data)

                sources.append(sources_item)

        _scope = d.pop("scope", UNSET)
        scope: GrepBodyScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = GrepBodyScope.from_dict(_scope)

        max_matches = d.pop("maxMatches", UNSET)

        context_lines = d.pop("contextLines", UNSET)

        grep_body = cls(
            pattern=pattern,
            flags=flags,
            sources=sources,
            scope=scope,
            max_matches=max_matches,
            context_lines=context_lines,
        )

        grep_body.additional_properties = d
        return grep_body

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
