from typing import Literal

ViewsChangeRequestBodyType1ConfigFiltersItemOperator = Literal[
    "contains", "equals", "is_empty", "is_false", "is_true", "not_empty"
]

VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_FILTERS_ITEM_OPERATOR_VALUES: set[
    ViewsChangeRequestBodyType1ConfigFiltersItemOperator
] = {
    "contains",
    "equals",
    "is_empty",
    "is_false",
    "is_true",
    "not_empty",
}


def check_views_change_request_body_type_1_config_filters_item_operator(
    value: str,
) -> ViewsChangeRequestBodyType1ConfigFiltersItemOperator:
    if value in VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_FILTERS_ITEM_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VIEWS_CHANGE_REQUEST_BODY_TYPE_1_CONFIG_FILTERS_ITEM_OPERATOR_VALUES!r}"
    )
