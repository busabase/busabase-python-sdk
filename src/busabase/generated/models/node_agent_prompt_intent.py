from typing import Literal

NodeAgentPromptIntent = Literal["change", "read-only"]

NODE_AGENT_PROMPT_INTENT_VALUES: set[NodeAgentPromptIntent] = {
    "change",
    "read-only",
}


def check_node_agent_prompt_intent(value: str) -> NodeAgentPromptIntent:
    if value in NODE_AGENT_PROMPT_INTENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODE_AGENT_PROMPT_INTENT_VALUES!r}")
