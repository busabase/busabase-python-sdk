from typing import Literal

RecordsGroupByFiltersItemOperator = Literal["contains", "equals", "is_empty", "is_false", "is_true", "not_empty"]

RECORDS_GROUP_BY_FILTERS_ITEM_OPERATOR_VALUES: set[RecordsGroupByFiltersItemOperator] = {
    "contains",
    "equals",
    "is_empty",
    "is_false",
    "is_true",
    "not_empty",
}


def check_records_group_by_filters_item_operator(value: str) -> RecordsGroupByFiltersItemOperator:
    if value in RECORDS_GROUP_BY_FILTERS_ITEM_OPERATOR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORDS_GROUP_BY_FILTERS_ITEM_OPERATOR_VALUES!r}")
