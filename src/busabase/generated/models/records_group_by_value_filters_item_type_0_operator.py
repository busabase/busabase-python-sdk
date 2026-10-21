from typing import Literal

RecordsGroupByValueFiltersItemType0Operator = Literal["eq", "gt", "gte", "lt", "lte", "ne"]

RECORDS_GROUP_BY_VALUE_FILTERS_ITEM_TYPE_0_OPERATOR_VALUES: set[RecordsGroupByValueFiltersItemType0Operator] = {
    "eq",
    "gt",
    "gte",
    "lt",
    "lte",
    "ne",
}


def check_records_group_by_value_filters_item_type_0_operator(
    value: str,
) -> RecordsGroupByValueFiltersItemType0Operator:
    if value in RECORDS_GROUP_BY_VALUE_FILTERS_ITEM_TYPE_0_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORDS_GROUP_BY_VALUE_FILTERS_ITEM_TYPE_0_OPERATOR_VALUES!r}"
    )
