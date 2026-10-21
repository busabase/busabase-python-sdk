from typing import Literal

NotifyAgentWebhookRuleInputEventType = Literal[
    "ai_mention", "asset.uploaded", "changes_requested", "record.created", "record.updated"
]

NOTIFY_AGENT_WEBHOOK_RULE_INPUT_EVENT_TYPE_VALUES: set[NotifyAgentWebhookRuleInputEventType] = {
    "ai_mention",
    "asset.uploaded",
    "changes_requested",
    "record.created",
    "record.updated",
}


def check_notify_agent_webhook_rule_input_event_type(value: str) -> NotifyAgentWebhookRuleInputEventType:
    if value in NOTIFY_AGENT_WEBHOOK_RULE_INPUT_EVENT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFY_AGENT_WEBHOOK_RULE_INPUT_EVENT_TYPE_VALUES!r}"
    )
