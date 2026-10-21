from typing import Literal

SearchResultKind = Literal["base", "change_request", "file", "node", "record"]

SEARCH_RESULT_KIND_VALUES: set[SearchResultKind] = {
    "base",
    "change_request",
    "file",
    "node",
    "record",
}


def check_search_result_kind(value: str) -> SearchResultKind:
    if value in SEARCH_RESULT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEARCH_RESULT_KIND_VALUES!r}")
