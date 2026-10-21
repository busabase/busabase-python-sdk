from typing import Literal

CreateViewOperationType = Literal["calendar", "gallery", "gantt", "kanban", "table"]

CREATE_VIEW_OPERATION_TYPE_VALUES: set[CreateViewOperationType] = {
    "calendar",
    "gallery",
    "gantt",
    "kanban",
    "table",
}


def check_create_view_operation_type(value: str) -> CreateViewOperationType:
    if value in CREATE_VIEW_OPERATION_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_VIEW_OPERATION_TYPE_VALUES!r}")
