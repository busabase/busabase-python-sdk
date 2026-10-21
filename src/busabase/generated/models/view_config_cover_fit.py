from typing import Literal

ViewConfigCoverFit = Literal["cover", "fit"]

VIEW_CONFIG_COVER_FIT_VALUES: set[ViewConfigCoverFit] = {
    "cover",
    "fit",
}


def check_view_config_cover_fit(value: str) -> ViewConfigCoverFit:
    if value in VIEW_CONFIG_COVER_FIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VIEW_CONFIG_COVER_FIT_VALUES!r}")
