from typing import Literal

ViewStatus = Literal["active", "archived"]

VIEW_STATUS_VALUES: set[ViewStatus] = {
    "active",
    "archived",
}


def check_view_status(value: str) -> ViewStatus:
    if value in VIEW_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VIEW_STATUS_VALUES!r}")
