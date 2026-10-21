from typing import Literal

SearchSourcesType0Item = Literal["files", "names", "nodes", "records"]

SEARCH_SOURCES_TYPE_0_ITEM_VALUES: set[SearchSourcesType0Item] = {
    "files",
    "names",
    "nodes",
    "records",
}


def check_search_sources_type_0_item(value: str) -> SearchSourcesType0Item:
    if value in SEARCH_SOURCES_TYPE_0_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEARCH_SOURCES_TYPE_0_ITEM_VALUES!r}")
