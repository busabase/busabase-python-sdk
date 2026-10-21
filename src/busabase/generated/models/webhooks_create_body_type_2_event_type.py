from typing import Literal

WebhooksCreateBodyType2EventType = Literal[
    "ai_mention", "asset.uploaded", "changes_requested", "record.created", "record.updated"
]

WEBHOOKS_CREATE_BODY_TYPE_2_EVENT_TYPE_VALUES: set[WebhooksCreateBodyType2EventType] = {
    "ai_mention",
    "asset.uploaded",
    "changes_requested",
    "record.created",
    "record.updated",
}


def check_webhooks_create_body_type_2_event_type(value: str) -> WebhooksCreateBodyType2EventType:
    if value in WEBHOOKS_CREATE_BODY_TYPE_2_EVENT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKS_CREATE_BODY_TYPE_2_EVENT_TYPE_VALUES!r}")
