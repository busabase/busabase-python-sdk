from typing import Literal

SearchSort = Literal["created_asc", "created_desc", "relevance", "updated_asc", "updated_desc"]

SEARCH_SORT_VALUES: set[SearchSort] = {
    "created_asc",
    "created_desc",
    "relevance",
    "updated_asc",
    "updated_desc",
}


def check_search_sort(value: str) -> SearchSort:
    if value in SEARCH_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEARCH_SORT_VALUES!r}")
