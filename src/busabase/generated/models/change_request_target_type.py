from typing import Literal

ChangeRequestTargetType = Literal["base", "node"]

CHANGE_REQUEST_TARGET_TYPE_VALUES: set[ChangeRequestTargetType] = {
    "base",
    "node",
}


def check_change_request_target_type(value: str) -> ChangeRequestTargetType:
    if value in CHANGE_REQUEST_TARGET_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHANGE_REQUEST_TARGET_TYPE_VALUES!r}")
