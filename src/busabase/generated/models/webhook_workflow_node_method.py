from typing import Literal

WebhookWorkflowNodeMethod = Literal["DELETE", "GET", "PATCH", "POST", "PUT"]

WEBHOOK_WORKFLOW_NODE_METHOD_VALUES: set[WebhookWorkflowNodeMethod] = {
    "DELETE",
    "GET",
    "PATCH",
    "POST",
    "PUT",
}


def check_webhook_workflow_node_method(value: str) -> WebhookWorkflowNodeMethod:
    if value in WEBHOOK_WORKFLOW_NODE_METHOD_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_WORKFLOW_NODE_METHOD_VALUES!r}")
