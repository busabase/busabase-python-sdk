from typing import Literal

AssetsUpdateMetadataBodyMode = Literal["merge", "replace"]

ASSETS_UPDATE_METADATA_BODY_MODE_VALUES: set[AssetsUpdateMetadataBodyMode] = {
    "merge",
    "replace",
}


def check_assets_update_metadata_body_mode(value: str) -> AssetsUpdateMetadataBodyMode:
    if value in ASSETS_UPDATE_METADATA_BODY_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSETS_UPDATE_METADATA_BODY_MODE_VALUES!r}")
