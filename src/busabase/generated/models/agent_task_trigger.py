from typing import Literal

AgentTaskTrigger = Literal["ai_mention", "changes_requested"]

AGENT_TASK_TRIGGER_VALUES: set[AgentTaskTrigger] = {
    "ai_mention",
    "changes_requested",
}


def check_agent_task_trigger(value: str) -> AgentTaskTrigger:
    if value in AGENT_TASK_TRIGGER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_TASK_TRIGGER_VALUES!r}")
