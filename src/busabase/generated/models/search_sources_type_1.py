from typing import Literal

SearchSourcesType1 = Literal["files", "names", "nodes", "records"]

SEARCH_SOURCES_TYPE_1_VALUES: set[SearchSourcesType1] = {
    "files",
    "names",
    "nodes",
    "records",
}


def check_search_sources_type_1(value: str) -> SearchSourcesType1:
    if value in SEARCH_SOURCES_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEARCH_SOURCES_TYPE_1_VALUES!r}")
