from typing import Literal

CommentMentionDispatchStatus = Literal["failed", "linked", "not_applicable", "queued"]

COMMENT_MENTION_DISPATCH_STATUS_VALUES: set[CommentMentionDispatchStatus] = {
    "failed",
    "linked",
    "not_applicable",
    "queued",
}


def check_comment_mention_dispatch_status(value: str) -> CommentMentionDispatchStatus:
    if value in COMMENT_MENTION_DISPATCH_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMENT_MENTION_DISPATCH_STATUS_VALUES!r}")
