from typing import Literal

FileTreesPreparePreviewResponse200Type2Reason = Literal[
    "authentication_failed",
    "file_too_large",
    "invalid_configuration",
    "invalid_response",
    "not_configured",
    "rate_limited",
    "service_unavailable",
    "timeout",
    "unsupported",
]

FILE_TREES_PREPARE_PREVIEW_RESPONSE_200_TYPE_2_REASON_VALUES: set[FileTreesPreparePreviewResponse200Type2Reason] = {
    "authentication_failed",
    "file_too_large",
    "invalid_configuration",
    "invalid_response",
    "not_configured",
    "rate_limited",
    "service_unavailable",
    "timeout",
    "unsupported",
}


def check_file_trees_prepare_preview_response_200_type_2_reason(
    value: str,
) -> FileTreesPreparePreviewResponse200Type2Reason:
    if value in FILE_TREES_PREPARE_PREVIEW_RESPONSE_200_TYPE_2_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FILE_TREES_PREPARE_PREVIEW_RESPONSE_200_TYPE_2_REASON_VALUES!r}"
    )
