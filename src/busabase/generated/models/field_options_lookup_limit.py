from typing import Literal

FieldOptionsLookupLimit = Literal["all", "first"]

FIELD_OPTIONS_LOOKUP_LIMIT_VALUES: set[FieldOptionsLookupLimit] = {
    "all",
    "first",
}


def check_field_options_lookup_limit(value: str) -> FieldOptionsLookupLimit:
    if value in FIELD_OPTIONS_LOOKUP_LIMIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_LOOKUP_LIMIT_VALUES!r}")
