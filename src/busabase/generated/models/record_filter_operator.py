from typing import Literal

RecordFilterOperator = Literal["contains", "equals", "is_empty", "is_false", "is_true", "not_empty"]

RECORD_FILTER_OPERATOR_VALUES: set[RecordFilterOperator] = {
    "contains",
    "equals",
    "is_empty",
    "is_false",
    "is_true",
    "not_empty",
}


def check_record_filter_operator(value: str) -> RecordFilterOperator:
    if value in RECORD_FILTER_OPERATOR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORD_FILTER_OPERATOR_VALUES!r}")
