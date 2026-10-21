from typing import Literal

FileTreesPreviewConfigResponse200Provider = Literal["builtin", "previewfile"]

FILE_TREES_PREVIEW_CONFIG_RESPONSE_200_PROVIDER_VALUES: set[FileTreesPreviewConfigResponse200Provider] = {
    "builtin",
    "previewfile",
}


def check_file_trees_preview_config_response_200_provider(value: str) -> FileTreesPreviewConfigResponse200Provider:
    if value in FILE_TREES_PREVIEW_CONFIG_RESPONSE_200_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FILE_TREES_PREVIEW_CONFIG_RESPONSE_200_PROVIDER_VALUES!r}"
    )
