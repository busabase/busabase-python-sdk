from typing import Literal

ViewConfigGanttScale = Literal["month", "week"]

VIEW_CONFIG_GANTT_SCALE_VALUES: set[ViewConfigGanttScale] = {
    "month",
    "week",
}


def check_view_config_gantt_scale(value: str) -> ViewConfigGanttScale:
    if value in VIEW_CONFIG_GANTT_SCALE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VIEW_CONFIG_GANTT_SCALE_VALUES!r}")
