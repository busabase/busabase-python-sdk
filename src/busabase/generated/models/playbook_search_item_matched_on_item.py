from typing import Literal

PlaybookSearchItemMatchedOnItem = Literal["body", "description", "label", "name", "slug"]

PLAYBOOK_SEARCH_ITEM_MATCHED_ON_ITEM_VALUES: set[PlaybookSearchItemMatchedOnItem] = {
    "body",
    "description",
    "label",
    "name",
    "slug",
}


def check_playbook_search_item_matched_on_item(value: str) -> PlaybookSearchItemMatchedOnItem:
    if value in PLAYBOOK_SEARCH_ITEM_MATCHED_ON_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOK_SEARCH_ITEM_MATCHED_ON_ITEM_VALUES!r}")
