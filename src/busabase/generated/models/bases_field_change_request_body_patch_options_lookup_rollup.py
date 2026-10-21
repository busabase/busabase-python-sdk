from typing import Literal

BasesFieldChangeRequestBodyPatchOptionsLookupRollup = Literal[
    "average", "concatenate", "count", "max", "min", "sum", "values"
]

BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_LOOKUP_ROLLUP_VALUES: set[
    BasesFieldChangeRequestBodyPatchOptionsLookupRollup
] = {
    "average",
    "concatenate",
    "count",
    "max",
    "min",
    "sum",
    "values",
}


def check_bases_field_change_request_body_patch_options_lookup_rollup(
    value: str,
) -> BasesFieldChangeRequestBodyPatchOptionsLookupRollup:
    if value in BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_LOOKUP_ROLLUP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_LOOKUP_ROLLUP_VALUES!r}"
    )
