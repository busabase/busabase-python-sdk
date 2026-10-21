from typing import Literal

HttpWebhookRuleEventType = Literal[
    "ai_mention", "asset.uploaded", "changes_requested", "record.created", "record.updated"
]

HTTP_WEBHOOK_RULE_EVENT_TYPE_VALUES: set[HttpWebhookRuleEventType] = {
    "ai_mention",
    "asset.uploaded",
    "changes_requested",
    "record.created",
    "record.updated",
}


def check_http_webhook_rule_event_type(value: str) -> HttpWebhookRuleEventType:
    if value in HTTP_WEBHOOK_RULE_EVENT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HTTP_WEBHOOK_RULE_EVENT_TYPE_VALUES!r}")
