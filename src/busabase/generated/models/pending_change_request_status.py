from typing import Literal

PendingChangeRequestStatus = Literal[
    "abandoned", "approved", "changes_requested", "conflict", "in_review", "merged", "rejected"
]

PENDING_CHANGE_REQUEST_STATUS_VALUES: set[PendingChangeRequestStatus] = {
    "abandoned",
    "approved",
    "changes_requested",
    "conflict",
    "in_review",
    "merged",
    "rejected",
}


def check_pending_change_request_status(value: str) -> PendingChangeRequestStatus:
    if value in PENDING_CHANGE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PENDING_CHANGE_REQUEST_STATUS_VALUES!r}")
