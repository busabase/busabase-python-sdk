from typing import Literal

WebhooksUpdateBodyEventType = Literal[
    "ai_mention", "asset.uploaded", "changes_requested", "record.created", "record.updated"
]

WEBHOOKS_UPDATE_BODY_EVENT_TYPE_VALUES: set[WebhooksUpdateBodyEventType] = {
    "ai_mention",
    "asset.uploaded",
    "changes_requested",
    "record.created",
    "record.updated",
}


def check_webhooks_update_body_event_type(value: str) -> WebhooksUpdateBodyEventType:
    if value in WEBHOOKS_UPDATE_BODY_EVENT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKS_UPDATE_BODY_EVENT_TYPE_VALUES!r}")
