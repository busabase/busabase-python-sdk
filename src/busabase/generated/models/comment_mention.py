from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comment_mention_dispatch_status import CommentMentionDispatchStatus, check_comment_mention_dispatch_status
from ..models.comment_mention_type import CommentMentionType, check_comment_mention_type

T = TypeVar("T", bound="CommentMention")


@_attrs_define
class CommentMention:
    """
    Attributes:
        id (str):
        type_ (CommentMentionType):
        target_id (str):
        label (str):
        start (int):
        end (int):
        dispatch_status (CommentMentionDispatchStatus):
        session_id (None | str):
        error (None | str):
    """

    id: str
    type_: CommentMentionType
    target_id: str
    label: str
    start: int
    end: int
    dispatch_status: CommentMentionDispatchStatus
    session_id: None | str
    error: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        target_id = self.target_id

        label = self.label

        start = self.start

        end = self.end

        dispatch_status: str = self.dispatch_status

        session_id: None | str
        session_id = self.session_id

        error: None | str
        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "targetId": target_id,
                "label": label,
                "start": start,
                "end": end,
                "dispatchStatus": dispatch_status,
                "sessionId": session_id,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_comment_mention_type(d.pop("type"))

        target_id = d.pop("targetId")

        label = d.pop("label")

        start = d.pop("start")

        end = d.pop("end")

        dispatch_status = check_comment_mention_dispatch_status(d.pop("dispatchStatus"))

        def _parse_session_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        session_id = _parse_session_id(d.pop("sessionId"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        comment_mention = cls(
            id=id,
            type_=type_,
            target_id=target_id,
            label=label,
            start=start,
            end=end,
            dispatch_status=dispatch_status,
            session_id=session_id,
            error=error,
        )

        comment_mention.additional_properties = d
        return comment_mention

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
