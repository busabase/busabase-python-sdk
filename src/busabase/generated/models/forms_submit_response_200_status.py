from typing import Literal

FormsSubmitResponse200Status = Literal["merged", "pending_review"]

FORMS_SUBMIT_RESPONSE_200_STATUS_VALUES: set[FormsSubmitResponse200Status] = {
    "merged",
    "pending_review",
}


def check_forms_submit_response_200_status(value: str) -> FormsSubmitResponse200Status:
    if value in FORMS_SUBMIT_RESPONSE_200_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FORMS_SUBMIT_RESPONSE_200_STATUS_VALUES!r}")
