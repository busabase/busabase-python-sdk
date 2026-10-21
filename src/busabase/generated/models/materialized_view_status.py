from typing import Literal

MaterializedViewStatus = Literal["active", "archived"]

MATERIALIZED_VIEW_STATUS_VALUES: set[MaterializedViewStatus] = {
    "active",
    "archived",
}


def check_materialized_view_status(value: str) -> MaterializedViewStatus:
    if value in MATERIALIZED_VIEW_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATERIALIZED_VIEW_STATUS_VALUES!r}")
