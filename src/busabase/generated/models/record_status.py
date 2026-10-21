from typing import Literal

RecordStatus = Literal["active", "archived"]

RECORD_STATUS_VALUES: set[RecordStatus] = {
    "active",
    "archived",
}


def check_record_status(value: str) -> RecordStatus:
    if value in RECORD_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORD_STATUS_VALUES!r}")
