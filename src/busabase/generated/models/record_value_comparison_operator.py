from typing import Literal

RecordValueComparisonOperator = Literal["eq", "gt", "gte", "lt", "lte", "ne"]

RECORD_VALUE_COMPARISON_OPERATOR_VALUES: set[RecordValueComparisonOperator] = {
    "eq",
    "gt",
    "gte",
    "lt",
    "lte",
    "ne",
}


def check_record_value_comparison_operator(value: str) -> RecordValueComparisonOperator:
    if value in RECORD_VALUE_COMPARISON_OPERATOR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORD_VALUE_COMPARISON_OPERATOR_VALUES!r}")
