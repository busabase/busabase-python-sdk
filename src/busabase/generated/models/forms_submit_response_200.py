from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.forms_submit_response_200_status import (
    FormsSubmitResponse200Status,
    check_forms_submit_response_200_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FormsSubmitResponse200")


@_attrs_define
class FormsSubmitResponse200:
    """
    Attributes:
        change_request_id (str):
        status (FormsSubmitResponse200Status):
        record_id (str | Unset):
    """

    change_request_id: str
    status: FormsSubmitResponse200Status
    record_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_request_id = self.change_request_id

        status: str = self.status

        record_id = self.record_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changeRequestId": change_request_id,
                "status": status,
            }
        )
        if record_id is not UNSET:
            field_dict["recordId"] = record_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        change_request_id = d.pop("changeRequestId")

        status = check_forms_submit_response_200_status(d.pop("status"))

        record_id = d.pop("recordId", UNSET)

        forms_submit_response_200 = cls(
            change_request_id=change_request_id,
            status=status,
            record_id=record_id,
        )

        forms_submit_response_200.additional_properties = d
        return forms_submit_response_200

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
