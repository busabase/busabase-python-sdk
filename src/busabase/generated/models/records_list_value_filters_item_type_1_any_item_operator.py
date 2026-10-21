from typing import Literal

RecordsListValueFiltersItemType1AnyItemOperator = Literal["eq", "gt", "gte", "lt", "lte", "ne"]

RECORDS_LIST_VALUE_FILTERS_ITEM_TYPE_1_ANY_ITEM_OPERATOR_VALUES: set[
    RecordsListValueFiltersItemType1AnyItemOperator
] = {
    "eq",
    "gt",
    "gte",
    "lt",
    "lte",
    "ne",
}


def check_records_list_value_filters_item_type_1_any_item_operator(
    value: str,
) -> RecordsListValueFiltersItemType1AnyItemOperator:
    if value in RECORDS_LIST_VALUE_FILTERS_ITEM_TYPE_1_ANY_ITEM_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORDS_LIST_VALUE_FILTERS_ITEM_TYPE_1_ANY_ITEM_OPERATOR_VALUES!r}"
    )
