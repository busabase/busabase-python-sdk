from typing import Literal

MaterializedRecordStatus = Literal["active", "archived"]

MATERIALIZED_RECORD_STATUS_VALUES: set[MaterializedRecordStatus] = {
    "active",
    "archived",
}


def check_materialized_record_status(value: str) -> MaterializedRecordStatus:
    if value in MATERIALIZED_RECORD_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATERIALIZED_RECORD_STATUS_VALUES!r}")
