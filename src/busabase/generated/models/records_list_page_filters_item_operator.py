from typing import Literal

RecordsListPageFiltersItemOperator = Literal["contains", "equals", "is_empty", "is_false", "is_true", "not_empty"]

RECORDS_LIST_PAGE_FILTERS_ITEM_OPERATOR_VALUES: set[RecordsListPageFiltersItemOperator] = {
    "contains",
    "equals",
    "is_empty",
    "is_false",
    "is_true",
    "not_empty",
}


def check_records_list_page_filters_item_operator(value: str) -> RecordsListPageFiltersItemOperator:
    if value in RECORDS_LIST_PAGE_FILTERS_ITEM_OPERATOR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORDS_LIST_PAGE_FILTERS_ITEM_OPERATOR_VALUES!r}")
