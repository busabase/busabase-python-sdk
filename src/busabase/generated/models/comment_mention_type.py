from typing import Literal

CommentMentionType = Literal["agent", "member"]

COMMENT_MENTION_TYPE_VALUES: set[CommentMentionType] = {
    "agent",
    "member",
}


def check_comment_mention_type(value: str) -> CommentMentionType:
    if value in COMMENT_MENTION_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMENT_MENTION_TYPE_VALUES!r}")
