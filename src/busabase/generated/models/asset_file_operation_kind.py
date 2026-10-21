from typing import Literal

AssetFileOperationKind = Literal["create", "update"]

ASSET_FILE_OPERATION_KIND_VALUES: set[AssetFileOperationKind] = {
    "create",
    "update",
}


def check_asset_file_operation_kind(value: str) -> AssetFileOperationKind:
    if value in ASSET_FILE_OPERATION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSET_FILE_OPERATION_KIND_VALUES!r}")
