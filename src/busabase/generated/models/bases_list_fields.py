from typing import Literal

BasesListFields = Literal["all", "links"]

BASES_LIST_FIELDS_VALUES: set[BasesListFields] = {
    "all",
    "links",
}


def check_bases_list_fields(value: str) -> BasesListFields:
    if value in BASES_LIST_FIELDS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BASES_LIST_FIELDS_VALUES!r}")
