from typing import Literal

RecordsCountValueFiltersItemType0Operator = Literal["eq", "gt", "gte", "lt", "lte", "ne"]

RECORDS_COUNT_VALUE_FILTERS_ITEM_TYPE_0_OPERATOR_VALUES: set[RecordsCountValueFiltersItemType0Operator] = {
    "eq",
    "gt",
    "gte",
    "lt",
    "lte",
    "ne",
}


def check_records_count_value_filters_item_type_0_operator(value: str) -> RecordsCountValueFiltersItemType0Operator:
    if value in RECORDS_COUNT_VALUE_FILTERS_ITEM_TYPE_0_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORDS_COUNT_VALUE_FILTERS_ITEM_TYPE_0_OPERATOR_VALUES!r}"
    )
