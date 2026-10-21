from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeRequestsReviewResponse200ResultsItemType1")


@_attrs_define
class ChangeRequestsReviewResponse200ResultsItemType1:
    """
    Attributes:
        change_request_id (str):
        ok (Literal[False]):
        error (str):
        code (str | Unset):
        data (Any | Unset):
    """

    change_request_id: str
    ok: Literal[False]
    error: str
    code: str | Unset = UNSET
    data: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_request_id = self.change_request_id

        ok = self.ok

        error = self.error

        code = self.code

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changeRequestId": change_request_id,
                "ok": ok,
                "error": error,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        change_request_id = d.pop("changeRequestId")

        ok = cast(Literal[False], d.pop("ok"))
        if ok != False:
            raise ValueError(f"ok must match const False, got '{ok}'")

        error = d.pop("error")

        code = d.pop("code", UNSET)

        data = d.pop("data", UNSET)

        change_requests_review_response_200_results_item_type_1 = cls(
            change_request_id=change_request_id,
            ok=ok,
            error=error,
            code=code,
            data=data,
        )

        change_requests_review_response_200_results_item_type_1.additional_properties = d
        return change_requests_review_response_200_results_item_type_1

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
