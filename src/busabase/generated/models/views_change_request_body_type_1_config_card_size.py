from typing import Literal

ViewsChangeRequestBodyType1ConfigCardSize = Literal["large", "medium", "small"]

VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_CARD_SIZE_VALUES: set[ViewsChangeRequestBodyType1ConfigCardSize] = {
    "large",
    "medium",
    "small",
}


def check_views_change_request_body_type_1_config_card_size(value: str) -> ViewsChangeRequestBodyType1ConfigCardSize:
    if value in VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_CARD_SIZE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_CARD_SIZE_VALUES!r}"
    )
