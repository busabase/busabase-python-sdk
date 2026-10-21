from typing import Literal

RecordSortDirection = Literal["asc", "desc"]

RECORD_SORT_DIRECTION_VALUES: set[RecordSortDirection] = {
    "asc",
    "desc",
}


def check_record_sort_direction(value: str) -> RecordSortDirection:
    if value in RECORD_SORT_DIRECTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORD_SORT_DIRECTION_VALUES!r}")
