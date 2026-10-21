from typing import Literal

ViewsChangeRequestBodyType0Type = Literal["calendar", "gallery", "gantt", "kanban", "table"]

VIEWS_CHANGE_REQUEST_BODY_TYPE_0_TYPE_VALUES: set[ViewsChangeRequestBodyType0Type] = {
    "calendar",
    "gallery",
    "gantt",
    "kanban",
    "table",
}


def check_views_change_request_body_type_0_type(value: str) -> ViewsChangeRequestBodyType0Type:
    if value in VIEWS_CHANGE_REQUEST_BODY_TYPE_0_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VIEWS_CHANGE_REQUEST_BODY_TYPE_0_TYPE_VALUES!r}")
