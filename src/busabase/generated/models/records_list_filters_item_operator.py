from typing import Literal

RecordsListFiltersItemOperator = Literal["contains", "equals", "is_empty", "is_false", "is_true", "not_empty"]

RECORDS_LIST_FILTERS_ITEM_OPERATOR_VALUES: set[RecordsListFiltersItemOperator] = {
    "contains",
    "equals",
    "is_empty",
    "is_false",
    "is_true",
    "not_empty",
}


def check_records_list_filters_item_operator(value: str) -> RecordsListFiltersItemOperator:
    if value in RECORDS_LIST_FILTERS_ITEM_OPERATOR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORDS_LIST_FILTERS_ITEM_OPERATOR_VALUES!r}")
