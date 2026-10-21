from typing import Literal

OperationDeleteMode = Literal["archive"]

OPERATION_DELETE_MODE_VALUES: set[OperationDeleteMode] = {
    "archive",
}


def check_operation_delete_mode(value: str) -> OperationDeleteMode:
    if value in OPERATION_DELETE_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OPERATION_DELETE_MODE_VALUES!r}")
