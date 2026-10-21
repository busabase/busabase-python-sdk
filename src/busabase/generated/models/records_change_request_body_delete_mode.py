from typing import Literal

RecordsChangeRequestBodyDeleteMode = Literal["archive"]

RECORDS_CHANGE_REQUEST_BODY_DELETE_MODE_VALUES: set[RecordsChangeRequestBodyDeleteMode] = {
    "archive",
}


def check_records_change_request_body_delete_mode(value: str) -> RecordsChangeRequestBodyDeleteMode:
    if value in RECORDS_CHANGE_REQUEST_BODY_DELETE_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECORDS_CHANGE_REQUEST_BODY_DELETE_MODE_VALUES!r}")
