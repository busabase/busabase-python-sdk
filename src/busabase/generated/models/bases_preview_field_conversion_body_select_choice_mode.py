from typing import Literal

BasesPreviewFieldConversionBodySelectChoiceMode = Literal["auto_create", "null_on_missing"]

BASES_PREVIEW_FIELD_CONVERSION_BODY_SELECT_CHOICE_MODE_VALUES: set[BasesPreviewFieldConversionBodySelectChoiceMode] = {
    "auto_create",
    "null_on_missing",
}


def check_bases_preview_field_conversion_body_select_choice_mode(
    value: str,
) -> BasesPreviewFieldConversionBodySelectChoiceMode:
    if value in BASES_PREVIEW_FIELD_CONVERSION_BODY_SELECT_CHOICE_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASES_PREVIEW_FIELD_CONVERSION_BODY_SELECT_CHOICE_MODE_VALUES!r}"
    )
