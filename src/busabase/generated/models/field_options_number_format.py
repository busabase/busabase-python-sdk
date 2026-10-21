from typing import Literal

FieldOptionsNumberFormat = Literal["currency", "plain"]

FIELD_OPTIONS_NUMBER_FORMAT_VALUES: set[FieldOptionsNumberFormat] = {
    "currency",
    "plain",
}


def check_field_options_number_format(value: str) -> FieldOptionsNumberFormat:
    if value in FIELD_OPTIONS_NUMBER_FORMAT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_NUMBER_FORMAT_VALUES!r}")
