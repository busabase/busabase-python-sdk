from typing import Literal

EmbedLinksCreateBodyType = Literal["change-request", "node", "record-detail"]

EMBED_LINKS_CREATE_BODY_TYPE_VALUES: set[EmbedLinksCreateBodyType] = {
    "change-request",
    "node",
    "record-detail",
}


def check_embed_links_create_body_type(value: str) -> EmbedLinksCreateBodyType:
    if value in EMBED_LINKS_CREATE_BODY_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EMBED_LINKS_CREATE_BODY_TYPE_VALUES!r}")
