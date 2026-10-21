from typing import Literal

PlaybookSearchItemKind = Literal["prompt", "skill"]

PLAYBOOK_SEARCH_ITEM_KIND_VALUES: set[PlaybookSearchItemKind] = {
    "prompt",
    "skill",
}


def check_playbook_search_item_kind(value: str) -> PlaybookSearchItemKind:
    if value in PLAYBOOK_SEARCH_ITEM_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOK_SEARCH_ITEM_KIND_VALUES!r}")
