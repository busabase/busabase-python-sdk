from typing import Literal

DriveNodeDetailVisibility = Literal["private", "public", "workspace"]

DRIVE_NODE_DETAIL_VISIBILITY_VALUES: set[DriveNodeDetailVisibility] = {
    "private",
    "public",
    "workspace",
}


def check_drive_node_detail_visibility(value: str) -> DriveNodeDetailVisibility:
    if value in DRIVE_NODE_DETAIL_VISIBILITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DRIVE_NODE_DETAIL_VISIBILITY_VALUES!r}")
