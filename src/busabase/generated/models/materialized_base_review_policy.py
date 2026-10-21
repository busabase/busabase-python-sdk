from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MaterializedBaseReviewPolicy")


@_attrs_define
class MaterializedBaseReviewPolicy:
    """
    Attributes:
        kind (Literal['single']):
        required_approvals (float):
    """

    kind: Literal["single"]
    required_approvals: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        required_approvals = self.required_approvals

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "requiredApprovals": required_approvals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = cast(Literal["single"], d.pop("kind"))
        if kind != "single":
            raise ValueError(f"kind must match const 'single', got '{kind}'")

        required_approvals = d.pop("requiredApprovals")

        materialized_base_review_policy = cls(
            kind=kind,
            required_approvals=required_approvals,
        )

        materialized_base_review_policy.additional_properties = d
        return materialized_base_review_policy

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
