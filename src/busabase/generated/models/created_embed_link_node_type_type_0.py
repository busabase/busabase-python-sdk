from typing import Literal

CreatedEmbedLinkNodeTypeType0 = Literal["airapp", "base", "doc", "drive", "file", "folder", "skill"]

CREATED_EMBED_LINK_NODE_TYPE_TYPE_0_VALUES: set[CreatedEmbedLinkNodeTypeType0] = {
    "airapp",
    "base",
    "doc",
    "drive",
    "file",
    "folder",
    "skill",
}


def check_created_embed_link_node_type_type_0(value: str) -> CreatedEmbedLinkNodeTypeType0:
    if value in CREATED_EMBED_LINK_NODE_TYPE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATED_EMBED_LINK_NODE_TYPE_TYPE_0_VALUES!r}")
