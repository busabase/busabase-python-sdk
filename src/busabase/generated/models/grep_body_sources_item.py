from typing import Literal

GrepBodySourcesItem = Literal["files", "nodes", "prompts", "records"]

GREP_BODY_SOURCES_ITEM_VALUES: set[GrepBodySourcesItem] = {
    "files",
    "nodes",
    "prompts",
    "records",
}


def check_grep_body_sources_item(value: str) -> GrepBodySourcesItem:
    if value in GREP_BODY_SOURCES_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GREP_BODY_SOURCES_ITEM_VALUES!r}")
