from typing import Literal

EmbedLinksListType = Literal["change-request", "node", "record-detail"]

EMBED_LINKS_LIST_TYPE_VALUES: set[EmbedLinksListType] = {
    "change-request",
    "node",
    "record-detail",
}


def check_embed_links_list_type(value: str) -> EmbedLinksListType:
    if value in EMBED_LINKS_LIST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EMBED_LINKS_LIST_TYPE_VALUES!r}")
