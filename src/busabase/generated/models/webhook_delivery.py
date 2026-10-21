from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_delivery_event_type import WebhookDeliveryEventType, check_webhook_delivery_event_type
from ..models.webhook_delivery_status import WebhookDeliveryStatus, check_webhook_delivery_status

T = TypeVar("T", bound="WebhookDelivery")


@_attrs_define
class WebhookDelivery:
    """
    Attributes:
        id (str):
        rule_id (str):
        event_type (WebhookDeliveryEventType):
        status (WebhookDeliveryStatus):
        http_status (float | None):
        detail (None | str):
        duration_ms (float | None):
        created_at (str):
    """

    id: str
    rule_id: str
    event_type: WebhookDeliveryEventType
    status: WebhookDeliveryStatus
    http_status: float | None
    detail: None | str
    duration_ms: float | None
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rule_id = self.rule_id

        event_type: str = self.event_type

        status: str = self.status

        http_status: float | None
        http_status = self.http_status

        detail: None | str
        detail = self.detail

        duration_ms: float | None
        duration_ms = self.duration_ms

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ruleId": rule_id,
                "eventType": event_type,
                "status": status,
                "httpStatus": http_status,
                "detail": detail,
                "durationMs": duration_ms,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        rule_id = d.pop("ruleId")

        event_type = check_webhook_delivery_event_type(d.pop("eventType"))

        status = check_webhook_delivery_status(d.pop("status"))

        def _parse_http_status(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        http_status = _parse_http_status(d.pop("httpStatus"))

        def _parse_detail(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        detail = _parse_detail(d.pop("detail"))

        def _parse_duration_ms(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        duration_ms = _parse_duration_ms(d.pop("durationMs"))

        created_at = d.pop("createdAt")

        webhook_delivery = cls(
            id=id,
            rule_id=rule_id,
            event_type=event_type,
            status=status,
            http_status=http_status,
            detail=detail,
            duration_ms=duration_ms,
            created_at=created_at,
        )

        webhook_delivery.additional_properties = d
        return webhook_delivery

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
