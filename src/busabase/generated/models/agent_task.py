from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_task_trigger import AgentTaskTrigger, check_agent_task_trigger

if TYPE_CHECKING:
    from ..models.change_request import ChangeRequest
    from ..models.comment import Comment


T = TypeVar("T", bound="AgentTask")


@_attrs_define
class AgentTask:
    """
    Attributes:
        change_request (ChangeRequest):
        trigger (AgentTaskTrigger):
        review_reason (None | str):
        ai_comments (list[Comment]):
    """

    change_request: ChangeRequest
    trigger: AgentTaskTrigger
    review_reason: None | str
    ai_comments: list[Comment]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_request = self.change_request.to_dict()

        trigger: str = self.trigger

        review_reason: None | str
        review_reason = self.review_reason

        ai_comments = []
        for ai_comments_item_data in self.ai_comments:
            ai_comments_item = ai_comments_item_data.to_dict()
            ai_comments.append(ai_comments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changeRequest": change_request,
                "trigger": trigger,
                "reviewReason": review_reason,
                "aiComments": ai_comments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.change_request import ChangeRequest
        from ..models.comment import Comment

        d = dict(src_dict)
        change_request = ChangeRequest.from_dict(d.pop("changeRequest"))

        trigger = check_agent_task_trigger(d.pop("trigger"))

        def _parse_review_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        review_reason = _parse_review_reason(d.pop("reviewReason"))

        ai_comments = []
        _ai_comments = d.pop("aiComments")
        for ai_comments_item_data in _ai_comments:
            ai_comments_item = Comment.from_dict(ai_comments_item_data)

            ai_comments.append(ai_comments_item)

        agent_task = cls(
            change_request=change_request,
            trigger=trigger,
            review_reason=review_reason,
            ai_comments=ai_comments,
        )

        agent_task.additional_properties = d
        return agent_task

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
