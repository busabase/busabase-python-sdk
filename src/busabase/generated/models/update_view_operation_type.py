from typing import Literal

UpdateViewOperationType = Literal["calendar", "gallery", "gantt", "kanban", "table"]

UPDATE_VIEW_OPERATION_TYPE_VALUES: set[UpdateViewOperationType] = {
    "calendar",
    "gallery",
    "gantt",
    "kanban",
    "table",
}


def check_update_view_operation_type(value: str) -> UpdateViewOperationType:
    if value in UPDATE_VIEW_OPERATION_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_VIEW_OPERATION_TYPE_VALUES!r}")
