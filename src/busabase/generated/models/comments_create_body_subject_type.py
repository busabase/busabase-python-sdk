from typing import Literal

CommentsCreateBodySubjectType = Literal["change_request", "commit", "operation", "record"]

COMMENTS_CREATE_BODY_SUBJECT_TYPE_VALUES: set[CommentsCreateBodySubjectType] = {
    "change_request",
    "commit",
    "operation",
    "record",
}


def check_comments_create_body_subject_type(value: str) -> CommentsCreateBodySubjectType:
    if value in COMMENTS_CREATE_BODY_SUBJECT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMENTS_CREATE_BODY_SUBJECT_TYPE_VALUES!r}")
