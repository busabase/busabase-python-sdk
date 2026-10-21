from typing import Literal

RecordsListPageSortDirection = Literal["asc", "desc"]

RECORDS_LIST_PAGE_SORT_DIRECTION_VALUES: set[RecordsListPageSortDirection] = {
    "asc",
    "desc",
}


def check_records_list_page_sort_direction(value: str) -> RecordsListPageSortDirection:
    if value in RECORDS_LIST_PAGE_SORT_DIRECTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORDS_LIST_PAGE_SORT_DIRECTION_VALUES!r}")
