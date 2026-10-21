from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.change_requests_review_body_verdict import (
    ChangeRequestsReviewBodyVerdict,
    check_change_requests_review_body_verdict,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeRequestsReviewBody")


@_attrs_define
class ChangeRequestsReviewBody:
    """
    Attributes:
        verdict (ChangeRequestsReviewBodyVerdict):
        change_request_ids (list[str]):
        reason (str | Unset):
    """

    verdict: ChangeRequestsReviewBodyVerdict
    change_request_ids: list[str]
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        verdict: str = self.verdict

        change_request_ids = self.change_request_ids

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "verdict": verdict,
                "changeRequestIds": change_request_ids,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        verdict = check_change_requests_review_body_verdict(d.pop("verdict"))

        change_request_ids = cast(list[str], d.pop("changeRequestIds"))

        reason = d.pop("reason", UNSET)

        change_requests_review_body = cls(
            verdict=verdict,
            change_request_ids=change_request_ids,
            reason=reason,
        )

        change_requests_review_body.additional_properties = d
        return change_requests_review_body

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
