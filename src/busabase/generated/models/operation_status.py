from typing import Literal

OperationStatus = Literal["archived", "failed", "merged", "pending"]

OPERATION_STATUS_VALUES: set[OperationStatus] = {
    "archived",
    "failed",
    "merged",
    "pending",
}


def check_operation_status(value: str) -> OperationStatus:
    if value in OPERATION_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OPERATION_STATUS_VALUES!r}")
