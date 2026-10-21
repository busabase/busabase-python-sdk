from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.guides_list_response_200_item_kind import (
    GuidesListResponse200ItemKind,
    check_guides_list_response_200_item_kind,
)

T = TypeVar("T", bound="GuidesListResponse200Item")


@_attrs_define
class GuidesListResponse200Item:
    """
    Attributes:
        topic (str):
        title (str):
        kind (GuidesListResponse200ItemKind):
        summary (str):
    """

    topic: str
    title: str
    kind: GuidesListResponse200ItemKind
    summary: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topic = self.topic

        title = self.title

        kind: str = self.kind

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topic": topic,
                "title": title,
                "kind": kind,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        topic = d.pop("topic")

        title = d.pop("title")

        kind = check_guides_list_response_200_item_kind(d.pop("kind"))

        summary = d.pop("summary")

        guides_list_response_200_item = cls(
            topic=topic,
            title=title,
            kind=kind,
            summary=summary,
        )

        guides_list_response_200_item.additional_properties = d
        return guides_list_response_200_item

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
