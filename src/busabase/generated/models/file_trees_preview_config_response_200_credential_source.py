from typing import Literal

FileTreesPreviewConfigResponse200CredentialSource = Literal["environment", "none", "vault"]

FILE_TREES_PREVIEW_CONFIG_RESPONSE_200_CREDENTIAL_SOURCE_VALUES: set[
    FileTreesPreviewConfigResponse200CredentialSource
] = {
    "environment",
    "none",
    "vault",
}


def check_file_trees_preview_config_response_200_credential_source(
    value: str,
) -> FileTreesPreviewConfigResponse200CredentialSource:
    if value in FILE_TREES_PREVIEW_CONFIG_RESPONSE_200_CREDENTIAL_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FILE_TREES_PREVIEW_CONFIG_RESPONSE_200_CREDENTIAL_SOURCE_VALUES!r}"
    )
