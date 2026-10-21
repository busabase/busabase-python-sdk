from typing import Literal

NodeAgentPromptsAgentPromptsType0ItemIntent = Literal["change", "read-only"]

NODE_AGENT_PROMPTS_AGENT_PROMPTS_TYPE_0_ITEM_INTENT_VALUES: set[NodeAgentPromptsAgentPromptsType0ItemIntent] = {
    "change",
    "read-only",
}


def check_node_agent_prompts_agent_prompts_type_0_item_intent(
    value: str,
) -> NodeAgentPromptsAgentPromptsType0ItemIntent:
    if value in NODE_AGENT_PROMPTS_AGENT_PROMPTS_TYPE_0_ITEM_INTENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NODE_AGENT_PROMPTS_AGENT_PROMPTS_TYPE_0_ITEM_INTENT_VALUES!r}"
    )
