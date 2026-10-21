from typing import Literal

AgentTasksListStatus = Literal["cancelled", "completed", "failed", "in_progress", "pending"]

AGENT_TASKS_LIST_STATUS_VALUES: set[AgentTasksListStatus] = {
    "cancelled",
    "completed",
    "failed",
    "in_progress",
    "pending",
}


def check_agent_tasks_list_status(value: str) -> AgentTasksListStatus:
    if value in AGENT_TASKS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_TASKS_LIST_STATUS_VALUES!r}")
