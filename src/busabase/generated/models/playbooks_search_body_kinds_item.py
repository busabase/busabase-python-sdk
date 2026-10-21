from typing import Literal

PlaybooksSearchBodyKindsItem = Literal["prompt", "skill"]

PLAYBOOKS_SEARCH_BODY_KINDS_ITEM_VALUES: set[PlaybooksSearchBodyKindsItem] = {
    "prompt",
    "skill",
}


def check_playbooks_search_body_kinds_item(value: str) -> PlaybooksSearchBodyKindsItem:
    if value in PLAYBOOKS_SEARCH_BODY_KINDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOKS_SEARCH_BODY_KINDS_ITEM_VALUES!r}")
