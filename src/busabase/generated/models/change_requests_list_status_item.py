from typing import Literal

ChangeRequestsListStatusItem = Literal[
    "abandoned", "approved", "changes_requested", "conflict", "in_review", "merged", "rejected"
]

CHANGE_REQUESTS_LIST_STATUS_ITEM_VALUES: set[ChangeRequestsListStatusItem] = {
    "abandoned",
    "approved",
    "changes_requested",
    "conflict",
    "in_review",
    "merged",
    "rejected",
}


def check_change_requests_list_status_item(value: str) -> ChangeRequestsListStatusItem:
    if value in CHANGE_REQUESTS_LIST_STATUS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHANGE_REQUESTS_LIST_STATUS_ITEM_VALUES!r}")
