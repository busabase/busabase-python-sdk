from typing import Literal

ViewSortDirection = Literal["asc", "desc"]

VIEW_SORT_DIRECTION_VALUES: set[ViewSortDirection] = {
    "asc",
    "desc",
}


def check_view_sort_direction(value: str) -> ViewSortDirection:
    if value in VIEW_SORT_DIRECTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VIEW_SORT_DIRECTION_VALUES!r}")
