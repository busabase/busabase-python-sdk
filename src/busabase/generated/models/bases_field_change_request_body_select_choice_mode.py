from typing import Literal

BasesFieldChangeRequestBodySelectChoiceMode = Literal["auto_create", "null_on_missing"]

BASES_FIELD_CHANGE_REQUEST_BODY_SELECT_CHOICE_MODE_VALUES: set[BasesFieldChangeRequestBodySelectChoiceMode] = {
    "auto_create",
    "null_on_missing",
}


def check_bases_field_change_request_body_select_choice_mode(value: str) -> BasesFieldChangeRequestBodySelectChoiceMode:
    if value in BASES_FIELD_CHANGE_REQUEST_BODY_SELECT_CHOICE_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASES_FIELD_CHANGE_REQUEST_BODY_SELECT_CHOICE_MODE_VALUES!r}"
    )
