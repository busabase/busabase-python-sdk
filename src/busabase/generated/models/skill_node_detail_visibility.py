from typing import Literal

SkillNodeDetailVisibility = Literal["private", "public", "workspace"]

SKILL_NODE_DETAIL_VISIBILITY_VALUES: set[SkillNodeDetailVisibility] = {
    "private",
    "public",
    "workspace",
}


def check_skill_node_detail_visibility(value: str) -> SkillNodeDetailVisibility:
    if value in SKILL_NODE_DETAIL_VISIBILITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SKILL_NODE_DETAIL_VISIBILITY_VALUES!r}")
