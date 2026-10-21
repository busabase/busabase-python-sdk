from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.guides_read_response_200_kind import GuidesReadResponse200Kind, check_guides_read_response_200_kind

T = TypeVar("T", bound="GuidesReadResponse200")


@_attrs_define
class GuidesReadResponse200:
    """
    Attributes:
        topic (str):
        title (str):
        kind (GuidesReadResponse200Kind):
        content (str):
        other_topics (list[str]):
    """

    topic: str
    title: str
    kind: GuidesReadResponse200Kind
    content: str
    other_topics: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topic = self.topic

        title = self.title

        kind: str = self.kind

        content = self.content

        other_topics = self.other_topics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topic": topic,
                "title": title,
                "kind": kind,
                "content": content,
                "otherTopics": other_topics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        topic = d.pop("topic")

        title = d.pop("title")

        kind = check_guides_read_response_200_kind(d.pop("kind"))

        content = d.pop("content")

        other_topics = cast(list[str], d.pop("otherTopics"))

        guides_read_response_200 = cls(
            topic=topic,
            title=title,
            kind=kind,
            content=content,
            other_topics=other_topics,
        )

        guides_read_response_200.additional_properties = d
        return guides_read_response_200

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
