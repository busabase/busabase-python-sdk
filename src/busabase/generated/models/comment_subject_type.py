from typing import Literal

CommentSubjectType = Literal["change_request", "commit", "operation", "record"]

COMMENT_SUBJECT_TYPE_VALUES: set[CommentSubjectType] = {
    "change_request",
    "commit",
    "operation",
    "record",
}


def check_comment_subject_type(value: str) -> CommentSubjectType:
    if value in COMMENT_SUBJECT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMENT_SUBJECT_TYPE_VALUES!r}")
