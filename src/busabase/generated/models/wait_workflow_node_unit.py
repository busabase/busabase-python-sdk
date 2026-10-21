from typing import Literal

WaitWorkflowNodeUnit = Literal["days", "hours", "minutes"]

WAIT_WORKFLOW_NODE_UNIT_VALUES: set[WaitWorkflowNodeUnit] = {
    "days",
    "hours",
    "minutes",
}


def check_wait_workflow_node_unit(value: str) -> WaitWorkflowNodeUnit:
    if value in WAIT_WORKFLOW_NODE_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WAIT_WORKFLOW_NODE_UNIT_VALUES!r}")
