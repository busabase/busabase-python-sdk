from typing import Literal

RecordsGroupByValueFiltersItemType1AnyItemOperator = Literal["eq", "gt", "gte", "lt", "lte", "ne"]

RECORDS_GROUP_BY_VALUE_FILTERS_ITEM_TYPE_1_ANY_ITEM_OPERATOR_VALUES: set[
    RecordsGroupByValueFiltersItemType1AnyItemOperator
] = {
    "eq",
    "gt",
    "gte",
    "lt",
    "lte",
    "ne",
}


def check_records_group_by_value_filters_item_type_1_any_item_operator(
    value: str,
) -> RecordsGroupByValueFiltersItemType1AnyItemOperator:
    if value in RECORDS_GROUP_BY_VALUE_FILTERS_ITEM_TYPE_1_ANY_ITEM_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORDS_GROUP_BY_VALUE_FILTERS_ITEM_TYPE_1_ANY_ITEM_OPERATOR_VALUES!r}"
    )
