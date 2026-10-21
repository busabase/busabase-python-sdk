from typing import Literal

ChangeRequestsListPageStatusItem = Literal[
    "abandoned", "approved", "changes_requested", "conflict", "in_review", "merged", "rejected"
]

CHANGE_REQUESTS_LIST_PAGE_STATUS_ITEM_VALUES: set[ChangeRequestsListPageStatusItem] = {
    "abandoned",
    "approved",
    "changes_requested",
    "conflict",
    "in_review",
    "merged",
    "rejected",
}


def check_change_requests_list_page_status_item(value: str) -> ChangeRequestsListPageStatusItem:
    if value in CHANGE_REQUESTS_LIST_PAGE_STATUS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHANGE_REQUESTS_LIST_PAGE_STATUS_ITEM_VALUES!r}")
