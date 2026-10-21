from typing import Literal

AssetTextStatus = Literal["missing", "none", "present", "stale"]

ASSET_TEXT_STATUS_VALUES: set[AssetTextStatus] = {
    "missing",
    "none",
    "present",
    "stale",
}


def check_asset_text_status(value: str) -> AssetTextStatus:
    if value in ASSET_TEXT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSET_TEXT_STATUS_VALUES!r}")
