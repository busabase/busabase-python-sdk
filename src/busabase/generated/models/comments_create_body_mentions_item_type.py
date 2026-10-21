from typing import Literal

CommentsCreateBodyMentionsItemType = Literal["agent", "member"]

COMMENTS_CREATE_BODY_MENTIONS_ITEM_TYPE_VALUES: set[CommentsCreateBodyMentionsItemType] = {
    "agent",
    "member",
}


def check_comments_create_body_mentions_item_type(value: str) -> CommentsCreateBodyMentionsItemType:
    if value in COMMENTS_CREATE_BODY_MENTIONS_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMENTS_CREATE_BODY_MENTIONS_ITEM_TYPE_VALUES!r}")
