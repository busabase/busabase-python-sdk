from typing import Literal

HttpWebhookRuleLastStatusType0 = Literal["failed", "skipped", "success"]

HTTP_WEBHOOK_RULE_LAST_STATUS_TYPE_0_VALUES: set[HttpWebhookRuleLastStatusType0] = {
    "failed",
    "skipped",
    "success",
}


def check_http_webhook_rule_last_status_type_0(value: str) -> HttpWebhookRuleLastStatusType0:
    if value in HTTP_WEBHOOK_RULE_LAST_STATUS_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HTTP_WEBHOOK_RULE_LAST_STATUS_TYPE_0_VALUES!r}")
