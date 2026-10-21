from typing import Literal

PlaybookSearchItemIntent = Literal["change", "read-only"]

PLAYBOOK_SEARCH_ITEM_INTENT_VALUES: set[PlaybookSearchItemIntent] = {
    "change",
    "read-only",
}


def check_playbook_search_item_intent(value: str) -> PlaybookSearchItemIntent:
    if value in PLAYBOOK_SEARCH_ITEM_INTENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOK_SEARCH_ITEM_INTENT_VALUES!r}")
