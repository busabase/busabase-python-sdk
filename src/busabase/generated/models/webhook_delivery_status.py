from typing import Literal

WebhookDeliveryStatus = Literal["failed", "skipped", "success"]

WEBHOOK_DELIVERY_STATUS_VALUES: set[WebhookDeliveryStatus] = {
    "failed",
    "skipped",
    "success",
}


def check_webhook_delivery_status(value: str) -> WebhookDeliveryStatus:
    if value in WEBHOOK_DELIVERY_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_DELIVERY_STATUS_VALUES!r}")
