from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comments_create_body_subject_type import (
    CommentsCreateBodySubjectType,
    check_comments_create_body_subject_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comments_create_body_mentions_item import CommentsCreateBodyMentionsItem


T = TypeVar("T", bound="CommentsCreateBody")


@_attrs_define
class CommentsCreateBody:
    """
    Attributes:
        subject_type (CommentsCreateBodySubjectType): What the comment thread hangs off, which decides how `subjectId`
            is interpreted.
        subject_id (str): The subject's id, interpreted according to `subjectType`.
        body (str):
        author_id (str | Unset):  Default: 'local-admin'.
        mentions (list[CommentsCreateBodyMentionsItem] | Unset):
    """

    subject_type: CommentsCreateBodySubjectType
    subject_id: str
    body: str
    author_id: str | Unset = "local-admin"
    mentions: list[CommentsCreateBodyMentionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject_type: str = self.subject_type

        subject_id = self.subject_id

        body = self.body

        author_id = self.author_id

        mentions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mentions, Unset):
            mentions = []
            for mentions_item_data in self.mentions:
                mentions_item = mentions_item_data.to_dict()
                mentions.append(mentions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subjectType": subject_type,
                "subjectId": subject_id,
                "body": body,
            }
        )
        if author_id is not UNSET:
            field_dict["authorId"] = author_id
        if mentions is not UNSET:
            field_dict["mentions"] = mentions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.comments_create_body_mentions_item import CommentsCreateBodyMentionsItem

        d = dict(src_dict)
        subject_type = check_comments_create_body_subject_type(d.pop("subjectType"))

        subject_id = d.pop("subjectId")

        body = d.pop("body")

        author_id = d.pop("authorId", UNSET)

        _mentions = d.pop("mentions", UNSET)
        mentions: list[CommentsCreateBodyMentionsItem] | Unset = UNSET
        if _mentions is not UNSET:
            mentions = []
            for mentions_item_data in _mentions:
                mentions_item = CommentsCreateBodyMentionsItem.from_dict(mentions_item_data)

                mentions.append(mentions_item)

        comments_create_body = cls(
            subject_type=subject_type,
            subject_id=subject_id,
            body=body,
            author_id=author_id,
            mentions=mentions,
        )

        comments_create_body.additional_properties = d
        return comments_create_body

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
