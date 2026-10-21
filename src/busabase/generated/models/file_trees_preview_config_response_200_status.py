from typing import Literal

FileTreesPreviewConfigResponse200Status = Literal["invalid_configuration", "not_configured", "ready"]

FILE_TREES_PREVIEW_CONFIG_RESPONSE_200_STATUS_VALUES: set[FileTreesPreviewConfigResponse200Status] = {
    "invalid_configuration",
    "not_configured",
    "ready",
}


def check_file_trees_preview_config_response_200_status(value: str) -> FileTreesPreviewConfigResponse200Status:
    if value in FILE_TREES_PREVIEW_CONFIG_RESPONSE_200_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FILE_TREES_PREVIEW_CONFIG_RESPONSE_200_STATUS_VALUES!r}"
    )
