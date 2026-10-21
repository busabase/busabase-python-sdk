from typing import Literal

BasesFieldChangeRequestBodyPatchOptionsNumberFormat = Literal["currency", "plain"]

BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_NUMBER_FORMAT_VALUES: set[
    BasesFieldChangeRequestBodyPatchOptionsNumberFormat
] = {
    "currency",
    "plain",
}


def check_bases_field_change_request_body_patch_options_number_format(
    value: str,
) -> BasesFieldChangeRequestBodyPatchOptionsNumberFormat:
    if value in BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_NUMBER_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_NUMBER_FORMAT_VALUES!r}"
    )
