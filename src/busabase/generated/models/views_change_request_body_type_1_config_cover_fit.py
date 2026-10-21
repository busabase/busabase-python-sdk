from typing import Literal

ViewsChangeRequestBodyType1ConfigCoverFit = Literal["cover", "fit"]

VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_COVER_FIT_VALUES: set[ViewsChangeRequestBodyType1ConfigCoverFit] = {
    "cover",
    "fit",
}


def check_views_change_request_body_type_1_config_cover_fit(value: str) -> ViewsChangeRequestBodyType1ConfigCoverFit:
    if value in VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_COVER_FIT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_COVER_FIT_VALUES!r}"
    )
