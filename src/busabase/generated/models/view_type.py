from typing import Literal

ViewType = Literal["calendar", "gallery", "gantt", "kanban", "table"]

VIEW_TYPE_VALUES: set[ViewType] = {
    "calendar",
    "gallery",
    "gantt",
    "kanban",
    "table",
}


def check_view_type(value: str) -> ViewType:
    if value in VIEW_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VIEW_TYPE_VALUES!r}")
