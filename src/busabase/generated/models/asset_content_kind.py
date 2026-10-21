from typing import Literal

AssetContentKind = Literal["binary", "text"]

ASSET_CONTENT_KIND_VALUES: set[AssetContentKind] = {
    "binary",
    "text",
}


def check_asset_content_kind(value: str) -> AssetContentKind:
    if value in ASSET_CONTENT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSET_CONTENT_KIND_VALUES!r}")
