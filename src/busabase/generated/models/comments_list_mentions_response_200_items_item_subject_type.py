from typing import Literal

CommentsListMentionsResponse200ItemsItemSubjectType = Literal["change_request", "commit", "operation", "record"]

COMMENTS_LIST_MENTIONS_RESPONSE_200_ITEMS_ITEM_SUBJECT_TYPE_VALUES: set[
    CommentsListMentionsResponse200ItemsItemSubjectType
] = {
    "change_request",
    "commit",
    "operation",
    "record",
}


def check_comments_list_mentions_response_200_items_item_subject_type(
    value: str,
) -> CommentsListMentionsResponse200ItemsItemSubjectType:
    if value in COMMENTS_LIST_MENTIONS_RESPONSE_200_ITEMS_ITEM_SUBJECT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMENTS_LIST_MENTIONS_RESPONSE_200_ITEMS_ITEM_SUBJECT_TYPE_VALUES!r}"
    )
