from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comments_list_mentions_response_200_items_item_subject_type import (
    CommentsListMentionsResponse200ItemsItemSubjectType,
    check_comments_list_mentions_response_200_items_item_subject_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_ref import UserRef


T = TypeVar("T", bound="CommentsListMentionsResponse200ItemsItem")


@_attrs_define
class CommentsListMentionsResponse200ItemsItem:
    """
    Attributes:
        comment_id (str):
        subject_type (CommentsListMentionsResponse200ItemsItemSubjectType):
        body (str):
        author_id (str):
        created_at (str):
        unread (bool):
        href (None | str):
        author (None | Unset | UserRef):
    """

    comment_id: str
    subject_type: CommentsListMentionsResponse200ItemsItemSubjectType
    body: str
    author_id: str
    created_at: str
    unread: bool
    href: None | str
    author: None | Unset | UserRef = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_ref import UserRef

        comment_id = self.comment_id

        subject_type: str = self.subject_type

        body = self.body

        author_id = self.author_id

        created_at = self.created_at

        unread = self.unread

        href: None | str
        href = self.href

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, UserRef):
            author = self.author.to_dict()
        else:
            author = self.author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentId": comment_id,
                "subjectType": subject_type,
                "body": body,
                "authorId": author_id,
                "createdAt": created_at,
                "unread": unread,
                "href": href,
            }
        )
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_ref import UserRef

        d = dict(src_dict)
        comment_id = d.pop("commentId")

        subject_type = check_comments_list_mentions_response_200_items_item_subject_type(d.pop("subjectType"))

        body = d.pop("body")

        author_id = d.pop("authorId")

        created_at = d.pop("createdAt")

        unread = d.pop("unread")

        def _parse_href(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        href = _parse_href(d.pop("href"))

        def _parse_author(data: object) -> None | Unset | UserRef:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = UserRef.from_dict(data)

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserRef, data)

        author = _parse_author(d.pop("author", UNSET))

        comments_list_mentions_response_200_items_item = cls(
            comment_id=comment_id,
            subject_type=subject_type,
            body=body,
            author_id=author_id,
            created_at=created_at,
            unread=unread,
            href=href,
            author=author,
        )

        comments_list_mentions_response_200_items_item.additional_properties = d
        return comments_list_mentions_response_200_items_item

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
