from typing import Literal

FormStatus = Literal["active", "archived"]

FORM_STATUS_VALUES: set[FormStatus] = {
    "active",
    "archived",
}


def check_form_status(value: str) -> FormStatus:
    if value in FORM_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORM_STATUS_VALUES!r}")
