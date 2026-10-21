from typing import Literal

RecordsGroupByAggregatesItemFn = Literal["avg", "count", "max", "min", "sum"]

RECORDS_GROUP_BY_AGGREGATES_ITEM_FN_VALUES: set[RecordsGroupByAggregatesItemFn] = {
    "avg",
    "count",
    "max",
    "min",
    "sum",
}


def check_records_group_by_aggregates_item_fn(value: str) -> RecordsGroupByAggregatesItemFn:
    if value in RECORDS_GROUP_BY_AGGREGATES_ITEM_FN_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORDS_GROUP_BY_AGGREGATES_ITEM_FN_VALUES!r}")
