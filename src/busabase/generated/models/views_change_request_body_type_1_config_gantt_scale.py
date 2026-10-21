from typing import Literal

ViewsChangeRequestBodyType1ConfigGanttScale = Literal["month", "week"]

VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_GANTT_SCALE_VALUES: set[ViewsChangeRequestBodyType1ConfigGanttScale] = {
    "month",
    "week",
}


def check_views_change_request_body_type_1_config_gantt_scale(
    value: str,
) -> ViewsChangeRequestBodyType1ConfigGanttScale:
    if value in VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_GANTT_SCALE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_GANTT_SCALE_VALUES!r}"
    )
