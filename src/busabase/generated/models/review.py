from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.review_verdict import ReviewVerdict, check_review_verdict
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_visible_operation_heads import ReviewVisibleOperationHeads
    from ..models.user_ref import UserRef


T = TypeVar("T", bound="Review")


@_attrs_define
class Review:
    """
    Attributes:
        id (str):
        change_request_id (str):
        reviewer_id (str):
        verdict (ReviewVerdict):
        reason (None | str):
        visible_operation_heads (ReviewVisibleOperationHeads):
        created_at (str):
        reviewer (None | Unset | UserRef):
    """

    id: str
    change_request_id: str
    reviewer_id: str
    verdict: ReviewVerdict
    reason: None | str
    visible_operation_heads: ReviewVisibleOperationHeads
    created_at: str
    reviewer: None | Unset | UserRef = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_ref import UserRef

        id = self.id

        change_request_id = self.change_request_id

        reviewer_id = self.reviewer_id

        verdict: str = self.verdict

        reason: None | str
        reason = self.reason

        visible_operation_heads = self.visible_operation_heads.to_dict()

        created_at = self.created_at

        reviewer: dict[str, Any] | None | Unset
        if isinstance(self.reviewer, Unset):
            reviewer = UNSET
        elif isinstance(self.reviewer, UserRef):
            reviewer = self.reviewer.to_dict()
        else:
            reviewer = self.reviewer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "changeRequestId": change_request_id,
                "reviewerId": reviewer_id,
                "verdict": verdict,
                "reason": reason,
                "visibleOperationHeads": visible_operation_heads,
                "createdAt": created_at,
            }
        )
        if reviewer is not UNSET:
            field_dict["reviewer"] = reviewer

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.review_visible_operation_heads import ReviewVisibleOperationHeads
        from ..models.user_ref import UserRef

        d = dict(src_dict)
        id = d.pop("id")

        change_request_id = d.pop("changeRequestId")

        reviewer_id = d.pop("reviewerId")

        verdict = check_review_verdict(d.pop("verdict"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        visible_operation_heads = ReviewVisibleOperationHeads.from_dict(d.pop("visibleOperationHeads"))

        created_at = d.pop("createdAt")

        def _parse_reviewer(data: object) -> None | Unset | UserRef:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reviewer_type_0 = UserRef.from_dict(data)

                return reviewer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserRef, data)

        reviewer = _parse_reviewer(d.pop("reviewer", UNSET))

        review = cls(
            id=id,
            change_request_id=change_request_id,
            reviewer_id=reviewer_id,
            verdict=verdict,
            reason=reason,
            visible_operation_heads=visible_operation_heads,
            created_at=created_at,
            reviewer=reviewer,
        )

        review.additional_properties = d
        return review

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
