from typing import Literal

NodeShareScope = Literal["none", "public"]

NODE_SHARE_SCOPE_VALUES: set[NodeShareScope] = {
    "none",
    "public",
}


def check_node_share_scope(value: str) -> NodeShareScope:
    if value in NODE_SHARE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODE_SHARE_SCOPE_VALUES!r}")
