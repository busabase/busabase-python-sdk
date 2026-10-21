from typing import Literal

WebhookDeliveryEventType = Literal[
    "ai_mention", "asset.uploaded", "changes_requested", "record.created", "record.updated"
]

WEBHOOK_DELIVERY_EVENT_TYPE_VALUES: set[WebhookDeliveryEventType] = {
    "ai_mention",
    "asset.uploaded",
    "changes_requested",
    "record.created",
    "record.updated",
}


def check_webhook_delivery_event_type(value: str) -> WebhookDeliveryEventType:
    if value in WEBHOOK_DELIVERY_EVENT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_DELIVERY_EVENT_TYPE_VALUES!r}")
