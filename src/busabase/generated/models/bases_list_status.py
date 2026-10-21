from typing import Literal

BasesListStatus = Literal["active", "archived"]

BASES_LIST_STATUS_VALUES: set[BasesListStatus] = {
    "active",
    "archived",
}


def check_bases_list_status(value: str) -> BasesListStatus:
    if value in BASES_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BASES_LIST_STATUS_VALUES!r}")
