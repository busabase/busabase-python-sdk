from typing import Literal

HttpWebhookRuleInputEventType = Literal[
    "ai_mention", "asset.uploaded", "changes_requested", "record.created", "record.updated"
]

HTTP_WEBHOOK_RULE_INPUT_EVENT_TYPE_VALUES: set[HttpWebhookRuleInputEventType] = {
    "ai_mention",
    "asset.uploaded",
    "changes_requested",
    "record.created",
    "record.updated",
}


def check_http_webhook_rule_input_event_type(value: str) -> HttpWebhookRuleInputEventType:
    if value in HTTP_WEBHOOK_RULE_INPUT_EVENT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HTTP_WEBHOOK_RULE_INPUT_EVENT_TYPE_VALUES!r}")
