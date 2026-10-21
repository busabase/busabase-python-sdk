from typing import Literal

UnavailableFilePreviewReason = Literal[
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

UNAVAILABLE_FILE_PREVIEW_REASON_VALUES: set[UnavailableFilePreviewReason] = {
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


def check_unavailable_file_preview_reason(value: str) -> UnavailableFilePreviewReason:
    if value in UNAVAILABLE_FILE_PREVIEW_REASON_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNAVAILABLE_FILE_PREVIEW_REASON_VALUES!r}")
