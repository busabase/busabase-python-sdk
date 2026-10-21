from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.record import Record


T = TypeVar("T", bound="RecordActivity")


@_attrs_define
class RecordActivity:
    """
    Attributes:
        kind (Literal['record']):
        timestamp (str):
        record (Record):
    """

    kind: Literal["record"]
    timestamp: str
    record: Record
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        timestamp = self.timestamp

        record = self.record.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "timestamp": timestamp,
                "record": record,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.record import Record

        d = dict(src_dict)
        kind = cast(Literal["record"], d.pop("kind"))
        if kind != "record":
            raise ValueError(f"kind must match const 'record', got '{kind}'")

        timestamp = d.pop("timestamp")

        record = Record.from_dict(d.pop("record"))

        record_activity = cls(
            kind=kind,
            timestamp=timestamp,
            record=record,
        )

        record_activity.additional_properties = d
        return record_activity

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
