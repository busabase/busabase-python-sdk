from typing import Literal

BasesFieldChangeRequestBodyPatchOptionsLookupLimit = Literal["all", "first"]

BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_LOOKUP_LIMIT_VALUES: set[
    BasesFieldChangeRequestBodyPatchOptionsLookupLimit
] = {
    "all",
    "first",
}


def check_bases_field_change_request_body_patch_options_lookup_limit(
    value: str,
) -> BasesFieldChangeRequestBodyPatchOptionsLookupLimit:
    if value in BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_LOOKUP_LIMIT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_LOOKUP_LIMIT_VALUES!r}"
    )
