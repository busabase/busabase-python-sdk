from typing import Literal

FieldOptionsLookupRollup = Literal["average", "concatenate", "count", "max", "min", "sum", "values"]

FIELD_OPTIONS_LOOKUP_ROLLUP_VALUES: set[FieldOptionsLookupRollup] = {
    "average",
    "concatenate",
    "count",
    "max",
    "min",
    "sum",
    "values",
}


def check_field_options_lookup_rollup(value: str) -> FieldOptionsLookupRollup:
    if value in FIELD_OPTIONS_LOOKUP_ROLLUP_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_LOOKUP_ROLLUP_VALUES!r}")
