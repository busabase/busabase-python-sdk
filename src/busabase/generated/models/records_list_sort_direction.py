from typing import Literal

RecordsListSortDirection = Literal["asc", "desc"]

RECORDS_LIST_SORT_DIRECTION_VALUES: set[RecordsListSortDirection] = {
    "asc",
    "desc",
}


def check_records_list_sort_direction(value: str) -> RecordsListSortDirection:
    if value in RECORDS_LIST_SORT_DIRECTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORDS_LIST_SORT_DIRECTION_VALUES!r}")
