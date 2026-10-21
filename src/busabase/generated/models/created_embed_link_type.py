from typing import Literal

CreatedEmbedLinkType = Literal["change-request", "node", "record-detail"]

CREATED_EMBED_LINK_TYPE_VALUES: set[CreatedEmbedLinkType] = {
    "change-request",
    "node",
    "record-detail",
}


def check_created_embed_link_type(value: str) -> CreatedEmbedLinkType:
    if value in CREATED_EMBED_LINK_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATED_EMBED_LINK_TYPE_VALUES!r}")
