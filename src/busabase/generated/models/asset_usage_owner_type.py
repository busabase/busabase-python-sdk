from typing import Literal

AssetUsageOwnerType = Literal["airapp", "base", "doc", "drive", "file_node", "skill"]

ASSET_USAGE_OWNER_TYPE_VALUES: set[AssetUsageOwnerType] = {
    "airapp",
    "base",
    "doc",
    "drive",
    "file_node",
    "skill",
}


def check_asset_usage_owner_type(value: str) -> AssetUsageOwnerType:
    if value in ASSET_USAGE_OWNER_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSET_USAGE_OWNER_TYPE_VALUES!r}")
