from typing import Literal

ChangeRequestStatus = Literal[
    "abandoned", "approved", "changes_requested", "conflict", "in_review", "merged", "rejected"
]

CHANGE_REQUEST_STATUS_VALUES: set[ChangeRequestStatus] = {
    "abandoned",
    "approved",
    "changes_requested",
    "conflict",
    "in_review",
    "merged",
    "rejected",
}


def check_change_request_status(value: str) -> ChangeRequestStatus:
    if value in CHANGE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHANGE_REQUEST_STATUS_VALUES!r}")
