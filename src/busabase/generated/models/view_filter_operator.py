from typing import Literal

ViewFilterOperator = Literal["contains", "equals", "is_empty", "is_false", "is_true", "not_empty"]

VIEW_FILTER_OPERATOR_VALUES: set[ViewFilterOperator] = {
    "contains",
    "equals",
    "is_empty",
    "is_false",
    "is_true",
    "not_empty",
}


def check_view_filter_operator(value: str) -> ViewFilterOperator:
    if value in VIEW_FILTER_OPERATOR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VIEW_FILTER_OPERATOR_VALUES!r}")
