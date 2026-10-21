from typing import Literal

OperationTargetType = Literal["base", "node"]

OPERATION_TARGET_TYPE_VALUES: set[OperationTargetType] = {
    "base",
    "node",
}


def check_operation_target_type(value: str) -> OperationTargetType:
    if value in OPERATION_TARGET_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OPERATION_TARGET_TYPE_VALUES!r}")
