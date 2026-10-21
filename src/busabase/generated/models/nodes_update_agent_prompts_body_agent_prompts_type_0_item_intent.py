from typing import Literal

NodesUpdateAgentPromptsBodyAgentPromptsType0ItemIntent = Literal["change", "read-only"]

NODES_UPDATE_AGENT_PROMPTS_BODY_AGENT_PROMPTS_TYPE_0_ITEM_INTENT_VALUES: set[
    NodesUpdateAgentPromptsBodyAgentPromptsType0ItemIntent
] = {
    "change",
    "read-only",
}


def check_nodes_update_agent_prompts_body_agent_prompts_type_0_item_intent(
    value: str,
) -> NodesUpdateAgentPromptsBodyAgentPromptsType0ItemIntent:
    if value in NODES_UPDATE_AGENT_PROMPTS_BODY_AGENT_PROMPTS_TYPE_0_ITEM_INTENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NODES_UPDATE_AGENT_PROMPTS_BODY_AGENT_PROMPTS_TYPE_0_ITEM_INTENT_VALUES!r}"
    )
