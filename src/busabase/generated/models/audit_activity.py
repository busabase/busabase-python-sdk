from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_event import AuditEvent
    from ..models.record import Record


T = TypeVar("T", bound="AuditActivity")


@_attrs_define
class AuditActivity:
    """
    Attributes:
        kind (Literal['audit']):
        timestamp (str):
        audit_event (AuditEvent):
        record (None | Record):
    """

    kind: Literal["audit"]
    timestamp: str
    audit_event: AuditEvent
    record: None | Record
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.record import Record

        kind = self.kind

        timestamp = self.timestamp

        audit_event = self.audit_event.to_dict()

        record: dict[str, Any] | None
        if isinstance(self.record, Record):
            record = self.record.to_dict()
        else:
            record = self.record

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "timestamp": timestamp,
                "auditEvent": audit_event,
                "record": record,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_event import AuditEvent
        from ..models.record import Record

        d = dict(src_dict)
        kind = cast(Literal["audit"], d.pop("kind"))
        if kind != "audit":
            raise ValueError(f"kind must match const 'audit', got '{kind}'")

        timestamp = d.pop("timestamp")

        audit_event = AuditEvent.from_dict(d.pop("auditEvent"))

        def _parse_record(data: object) -> None | Record:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                record_type_0 = Record.from_dict(data)

                return record_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Record, data)

        record = _parse_record(d.pop("record"))

        audit_activity = cls(
            kind=kind,
            timestamp=timestamp,
            audit_event=audit_event,
            record=record,
        )

        audit_activity.additional_properties = d
        return audit_activity

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
