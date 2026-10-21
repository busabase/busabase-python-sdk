from typing import Literal

ViewConfigFiltersItemOperator = Literal["contains", "equals", "is_empty", "is_false", "is_true", "not_empty"]

VIEW_CONFIG_FILTERS_ITEM_OPERATOR_VALUES: set[ViewConfigFiltersItemOperator] = {
    "contains",
    "equals",
    "is_empty",
    "is_false",
    "is_true",
    "not_empty",
}


def check_view_config_filters_item_operator(value: str) -> ViewConfigFiltersItemOperator:
    if value in VIEW_CONFIG_FILTERS_ITEM_OPERATOR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VIEW_CONFIG_FILTERS_ITEM_OPERATOR_VALUES!r}")
