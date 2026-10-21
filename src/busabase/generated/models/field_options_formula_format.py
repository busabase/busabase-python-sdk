from typing import Literal

FieldOptionsFormulaFormat = Literal["auto", "currency", "date", "number", "percent"]

FIELD_OPTIONS_FORMULA_FORMAT_VALUES: set[FieldOptionsFormulaFormat] = {
    "auto",
    "currency",
    "date",
    "number",
    "percent",
}


def check_field_options_formula_format(value: str) -> FieldOptionsFormulaFormat:
    if value in FIELD_OPTIONS_FORMULA_FORMAT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_FORMULA_FORMAT_VALUES!r}")
