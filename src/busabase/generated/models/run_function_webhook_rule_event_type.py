from typing import Literal

RunFunctionWebhookRuleEventType = Literal[
    "ai_mention", "asset.uploaded", "changes_requested", "record.created", "record.updated"
]

RUN_FUNCTION_WEBHOOK_RULE_EVENT_TYPE_VALUES: set[RunFunctionWebhookRuleEventType] = {
    "ai_mention",
    "asset.uploaded",
    "changes_requested",
    "record.created",
    "record.updated",
}


def check_run_function_webhook_rule_event_type(value: str) -> RunFunctionWebhookRuleEventType:
    if value in RUN_FUNCTION_WEBHOOK_RULE_EVENT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RUN_FUNCTION_WEBHOOK_RULE_EVENT_TYPE_VALUES!r}")
