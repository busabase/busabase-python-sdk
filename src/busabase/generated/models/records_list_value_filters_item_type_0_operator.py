from typing import Literal

RecordsListValueFiltersItemType0Operator = Literal["eq", "gt", "gte", "lt", "lte", "ne"]

RECORDS_LIST_VALUE_FILTERS_ITEM_TYPE_0_OPERATOR_VALUES: set[RecordsListValueFiltersItemType0Operator] = {
    "eq",
    "gt",
    "gte",
    "lt",
    "lte",
    "ne",
}


def check_records_list_value_filters_item_type_0_operator(value: str) -> RecordsListValueFiltersItemType0Operator:
    if value in RECORDS_LIST_VALUE_FILTERS_ITEM_TYPE_0_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORDS_LIST_VALUE_FILTERS_ITEM_TYPE_0_OPERATOR_VALUES!r}"
    )
