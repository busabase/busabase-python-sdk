from typing import Literal

MaterializedViewType = Literal["calendar", "gallery", "gantt", "kanban", "table"]

MATERIALIZED_VIEW_TYPE_VALUES: set[MaterializedViewType] = {
    "calendar",
    "gallery",
    "gantt",
    "kanban",
    "table",
}


def check_materialized_view_type(value: str) -> MaterializedViewType:
    if value in MATERIALIZED_VIEW_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATERIALIZED_VIEW_TYPE_VALUES!r}")
