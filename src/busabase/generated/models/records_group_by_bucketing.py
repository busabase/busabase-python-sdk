from typing import Literal

RecordsGroupByBucketing = Literal["grid", "sql"]

RECORDS_GROUP_BY_BUCKETING_VALUES: set[RecordsGroupByBucketing] = {
    "grid",
    "sql",
}


def check_records_group_by_bucketing(value: str) -> RecordsGroupByBucketing:
    if value in RECORDS_GROUP_BY_BUCKETING_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORDS_GROUP_BY_BUCKETING_VALUES!r}")
