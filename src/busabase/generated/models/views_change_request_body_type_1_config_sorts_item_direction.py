from typing import Literal

ViewsChangeRequestBodyType1ConfigSortsItemDirection = Literal["asc", "desc"]

VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_SORTS_ITEM_DIRECTION_VALUES: set[
    ViewsChangeRequestBodyType1ConfigSortsItemDirection
] = {
    "asc",
    "desc",
}


def check_views_change_request_body_type_1_config_sorts_item_direction(
    value: str,
) -> ViewsChangeRequestBodyType1ConfigSortsItemDirection:
    if value in VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_SORTS_ITEM_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_SORTS_ITEM_DIRECTION_VALUES!r}"
    )
