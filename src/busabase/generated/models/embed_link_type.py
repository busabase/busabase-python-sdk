from typing import Literal

EmbedLinkType = Literal["change-request", "node", "record-detail"]

EMBED_LINK_TYPE_VALUES: set[EmbedLinkType] = {
    "change-request",
    "node",
    "record-detail",
}


def check_embed_link_type(value: str) -> EmbedLinkType:
    if value in EMBED_LINK_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EMBED_LINK_TYPE_VALUES!r}")
