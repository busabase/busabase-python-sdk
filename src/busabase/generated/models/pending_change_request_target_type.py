from typing import Literal

PendingChangeRequestTargetType = Literal["base", "node"]

PENDING_CHANGE_REQUEST_TARGET_TYPE_VALUES: set[PendingChangeRequestTargetType] = {
    "base",
    "node",
}


def check_pending_change_request_target_type(value: str) -> PendingChangeRequestTargetType:
    if value in PENDING_CHANGE_REQUEST_TARGET_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PENDING_CHANGE_REQUEST_TARGET_TYPE_VALUES!r}")
