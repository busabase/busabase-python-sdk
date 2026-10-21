from typing import Literal

CommentsListSubjectType = Literal["change_request", "commit", "operation", "record"]

COMMENTS_LIST_SUBJECT_TYPE_VALUES: set[CommentsListSubjectType] = {
    "change_request",
    "commit",
    "operation",
    "record",
}


def check_comments_list_subject_type(value: str) -> CommentsListSubjectType:
    if value in COMMENTS_LIST_SUBJECT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMENTS_LIST_SUBJECT_TYPE_VALUES!r}")
