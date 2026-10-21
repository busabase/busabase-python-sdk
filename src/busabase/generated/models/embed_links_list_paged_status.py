from typing import Literal

EmbedLinksListPagedStatus = Literal["active", "all", "expired", "revoked"]

EMBED_LINKS_LIST_PAGED_STATUS_VALUES: set[EmbedLinksListPagedStatus] = {
    "active",
    "all",
    "expired",
    "revoked",
}


def check_embed_links_list_paged_status(value: str) -> EmbedLinksListPagedStatus:
    if value in EMBED_LINKS_LIST_PAGED_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EMBED_LINKS_LIST_PAGED_STATUS_VALUES!r}")
