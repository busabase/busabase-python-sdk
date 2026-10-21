from typing import Literal

BasesFieldChangeRequestBodyPatchOptionsFormulaFormat = Literal["auto", "currency", "date", "number", "percent"]

BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_FORMULA_FORMAT_VALUES: set[
    BasesFieldChangeRequestBodyPatchOptionsFormulaFormat
] = {
    "auto",
    "currency",
    "date",
    "number",
    "percent",
}


def check_bases_field_change_request_body_patch_options_formula_format(
    value: str,
) -> BasesFieldChangeRequestBodyPatchOptionsFormulaFormat:
    if value in BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_FORMULA_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_FORMULA_FORMAT_VALUES!r}"
    )
