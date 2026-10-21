from typing import Literal

RecordsListStatus = Literal["active", "archived"]

RECORDS_LIST_STATUS_VALUES: set[RecordsListStatus] = {
    "active",
    "archived",
}


def check_records_list_status(value: str) -> RecordsListStatus:
    if value in RECORDS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORDS_LIST_STATUS_VALUES!r}")
