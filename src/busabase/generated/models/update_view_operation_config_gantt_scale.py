from typing import Literal

UpdateViewOperationConfigGanttScale = Literal["month", "week"]

UPDATE_VIEW_OPERATION_CONFIG_GANTT_SCALE_VALUES: set[UpdateViewOperationConfigGanttScale] = {
    "month",
    "week",
}


def check_update_view_operation_config_gantt_scale(value: str) -> UpdateViewOperationConfigGanttScale:
    if value in UPDATE_VIEW_OPERATION_CONFIG_GANTT_SCALE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_VIEW_OPERATION_CONFIG_GANTT_SCALE_VALUES!r}")
