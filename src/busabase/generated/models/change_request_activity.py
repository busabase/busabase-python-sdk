from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.change_request import ChangeRequest


T = TypeVar("T", bound="ChangeRequestActivity")


@_attrs_define
class ChangeRequestActivity:
    """
    Attributes:
        kind (Literal['change_request']):
        timestamp (str):
        change_request (ChangeRequest):
    """

    kind: Literal["change_request"]
    timestamp: str
    change_request: ChangeRequest
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        timestamp = self.timestamp

        change_request = self.change_request.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "timestamp": timestamp,
                "changeRequest": change_request,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.change_request import ChangeRequest

        d = dict(src_dict)
        kind = cast(Literal["change_request"], d.pop("kind"))
        if kind != "change_request":
            raise ValueError(f"kind must match const 'change_request', got '{kind}'")

        timestamp = d.pop("timestamp")

        change_request = ChangeRequest.from_dict(d.pop("changeRequest"))

        change_request_activity = cls(
            kind=kind,
            timestamp=timestamp,
            change_request=change_request,
        )

        change_request_activity.additional_properties = d
        return change_request_activity

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
