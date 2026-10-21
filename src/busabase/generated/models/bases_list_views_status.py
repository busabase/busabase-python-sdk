from typing import Literal

BasesListViewsStatus = Literal["active", "archived"]

BASES_LIST_VIEWS_STATUS_VALUES: set[BasesListViewsStatus] = {
    "active",
    "archived",
}


def check_bases_list_views_status(value: str) -> BasesListViewsStatus:
    if value in BASES_LIST_VIEWS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BASES_LIST_VIEWS_STATUS_VALUES!r}")
