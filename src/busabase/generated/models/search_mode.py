from typing import Literal

SearchMode = Literal["full", "quick"]

SEARCH_MODE_VALUES: set[SearchMode] = {
    "full",
    "quick",
}


def check_search_mode(value: str) -> SearchMode:
    if value in SEARCH_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEARCH_MODE_VALUES!r}")
