from typing import Literal

AssetsPutTextResponse200TextStatus = Literal["missing", "none", "present", "stale"]

ASSETS_PUT_TEXT_RESPONSE_200_TEXT_STATUS_VALUES: set[AssetsPutTextResponse200TextStatus] = {
    "missing",
    "none",
    "present",
    "stale",
}


def check_assets_put_text_response_200_text_status(value: str) -> AssetsPutTextResponse200TextStatus:
    if value in ASSETS_PUT_TEXT_RESPONSE_200_TEXT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSETS_PUT_TEXT_RESPONSE_200_TEXT_STATUS_VALUES!r}")
