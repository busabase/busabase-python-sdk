from typing import Literal

EmbedLinkNodeTypeType0 = Literal["airapp", "base", "doc", "drive", "file", "folder", "skill"]

EMBED_LINK_NODE_TYPE_TYPE_0_VALUES: set[EmbedLinkNodeTypeType0] = {
    "airapp",
    "base",
    "doc",
    "drive",
    "file",
    "folder",
    "skill",
}


def check_embed_link_node_type_type_0(value: str) -> EmbedLinkNodeTypeType0:
    if value in EMBED_LINK_NODE_TYPE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EMBED_LINK_NODE_TYPE_TYPE_0_VALUES!r}")
