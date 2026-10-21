from typing import Literal

RunFunctionWebhookRuleLastStatusType0 = Literal["failed", "skipped", "success"]

RUN_FUNCTION_WEBHOOK_RULE_LAST_STATUS_TYPE_0_VALUES: set[RunFunctionWebhookRuleLastStatusType0] = {
    "failed",
    "skipped",
    "success",
}


def check_run_function_webhook_rule_last_status_type_0(value: str) -> RunFunctionWebhookRuleLastStatusType0:
    if value in RUN_FUNCTION_WEBHOOK_RULE_LAST_STATUS_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RUN_FUNCTION_WEBHOOK_RULE_LAST_STATUS_TYPE_0_VALUES!r}"
    )
