from typing import Literal

RecordsCountFiltersItemOperator = Literal["contains", "equals", "is_empty", "is_false", "is_true", "not_empty"]

RECORDS_COUNT_FILTERS_ITEM_OPERATOR_VALUES: set[RecordsCountFiltersItemOperator] = {
    "contains",
    "equals",
    "is_empty",
    "is_false",
    "is_true",
    "not_empty",
}


def check_records_count_filters_item_operator(value: str) -> RecordsCountFiltersItemOperator:
    if value in RECORDS_COUNT_FILTERS_ITEM_OPERATOR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORDS_COUNT_FILTERS_ITEM_OPERATOR_VALUES!r}")
