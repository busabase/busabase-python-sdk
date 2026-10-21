from typing import Literal

NodesShareSetBodyScope = Literal["none", "public"]

NODES_SHARE_SET_BODY_SCOPE_VALUES: set[NodesShareSetBodyScope] = {
    "none",
    "public",
}


def check_nodes_share_set_body_scope(value: str) -> NodesShareSetBodyScope:
    if value in NODES_SHARE_SET_BODY_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODES_SHARE_SET_BODY_SCOPE_VALUES!r}")
