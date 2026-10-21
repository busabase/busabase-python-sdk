from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comment_subject_type import CommentSubjectType, check_comment_subject_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_mention import CommentMention
    from ..models.user_ref import UserRef


T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        id (str):
        subject_type (CommentSubjectType):
        subject_id (str):
        record_id (None | str):
        change_request_id (None | str):
        operation_id (None | str):
        commit_id (None | str):
        author_id (str):
        body (str):
        created_at (str):
        updated_at (str):
        author (None | Unset | UserRef):
        mentions (list[CommentMention] | Unset):
    """

    id: str
    subject_type: CommentSubjectType
    subject_id: str
    record_id: None | str
    change_request_id: None | str
    operation_id: None | str
    commit_id: None | str
    author_id: str
    body: str
    created_at: str
    updated_at: str
    author: None | Unset | UserRef = UNSET
    mentions: list[CommentMention] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_ref import UserRef

        id = self.id

        subject_type: str = self.subject_type

        subject_id = self.subject_id

        record_id: None | str
        record_id = self.record_id

        change_request_id: None | str
        change_request_id = self.change_request_id

        operation_id: None | str
        operation_id = self.operation_id

        commit_id: None | str
        commit_id = self.commit_id

        author_id = self.author_id

        body = self.body

        created_at = self.created_at

        updated_at = self.updated_at

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, UserRef):
            author = self.author.to_dict()
        else:
            author = self.author

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
                "id": id,
                "subjectType": subject_type,
                "subjectId": subject_id,
                "recordId": record_id,
                "changeRequestId": change_request_id,
                "operationId": operation_id,
                "commitId": commit_id,
                "authorId": author_id,
                "body": body,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if author is not UNSET:
            field_dict["author"] = author
        if mentions is not UNSET:
            field_dict["mentions"] = mentions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.comment_mention import CommentMention
        from ..models.user_ref import UserRef

        d = dict(src_dict)
        id = d.pop("id")

        subject_type = check_comment_subject_type(d.pop("subjectType"))

        subject_id = d.pop("subjectId")

        def _parse_record_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        record_id = _parse_record_id(d.pop("recordId"))

        def _parse_change_request_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        change_request_id = _parse_change_request_id(d.pop("changeRequestId"))

        def _parse_operation_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        operation_id = _parse_operation_id(d.pop("operationId"))

        def _parse_commit_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        commit_id = _parse_commit_id(d.pop("commitId"))

        author_id = d.pop("authorId")

        body = d.pop("body")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

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

        _mentions = d.pop("mentions", UNSET)
        mentions: list[CommentMention] | Unset = UNSET
        if _mentions is not UNSET:
            mentions = []
            for mentions_item_data in _mentions:
                mentions_item = CommentMention.from_dict(mentions_item_data)

                mentions.append(mentions_item)

        comment = cls(
            id=id,
            subject_type=subject_type,
            subject_id=subject_id,
            record_id=record_id,
            change_request_id=change_request_id,
            operation_id=operation_id,
            commit_id=commit_id,
            author_id=author_id,
            body=body,
            created_at=created_at,
            updated_at=updated_at,
            author=author,
            mentions=mentions,
        )

        comment.additional_properties = d
        return comment

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
