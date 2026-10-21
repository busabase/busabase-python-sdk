from typing import Literal

NotifyAgentWebhookRuleLastStatusType0 = Literal["failed", "skipped", "success"]

NOTIFY_AGENT_WEBHOOK_RULE_LAST_STATUS_TYPE_0_VALUES: set[NotifyAgentWebhookRuleLastStatusType0] = {
    "failed",
    "skipped",
    "success",
}


def check_notify_agent_webhook_rule_last_status_type_0(value: str) -> NotifyAgentWebhookRuleLastStatusType0:
    if value in NOTIFY_AGENT_WEBHOOK_RULE_LAST_STATUS_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFY_AGENT_WEBHOOK_RULE_LAST_STATUS_TYPE_0_VALUES!r}"
    )
