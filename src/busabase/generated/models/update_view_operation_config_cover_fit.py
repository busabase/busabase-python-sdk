from typing import Literal

UpdateViewOperationConfigCoverFit = Literal["cover", "fit"]

UPDATE_VIEW_OPERATION_CONFIG_COVER_FIT_VALUES: set[UpdateViewOperationConfigCoverFit] = {
    "cover",
    "fit",
}


def check_update_view_operation_config_cover_fit(value: str) -> UpdateViewOperationConfigCoverFit:
    if value in UPDATE_VIEW_OPERATION_CONFIG_COVER_FIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_VIEW_OPERATION_CONFIG_COVER_FIT_VALUES!r}")
