from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChangeRequestsCountsResponse200")


@_attrs_define
class ChangeRequestsCountsResponse200:
    """
    Attributes:
        review (int):
        changes (int):
        created (int):
        approved (int):
        merged (int):
        rejected (int):
    """

    review: int
    changes: int
    created: int
    approved: int
    merged: int
    rejected: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        review = self.review

        changes = self.changes

        created = self.created

        approved = self.approved

        merged = self.merged

        rejected = self.rejected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "review": review,
                "changes": changes,
                "created": created,
                "approved": approved,
                "merged": merged,
                "rejected": rejected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        review = d.pop("review")

        changes = d.pop("changes")

        created = d.pop("created")

        approved = d.pop("approved")

        merged = d.pop("merged")

        rejected = d.pop("rejected")

        change_requests_counts_response_200 = cls(
            review=review,
            changes=changes,
            created=created,
            approved=approved,
            merged=merged,
            rejected=rejected,
        )

        change_requests_counts_response_200.additional_properties = d
        return change_requests_counts_response_200

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
