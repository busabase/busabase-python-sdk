from typing import Literal

NodesShareSetBodyCapability = Literal["read", "submit"]

NODES_SHARE_SET_BODY_CAPABILITY_VALUES: set[NodesShareSetBodyCapability] = {
    "read",
    "submit",
}


def check_nodes_share_set_body_capability(value: str) -> NodesShareSetBodyCapability:
    if value in NODES_SHARE_SET_BODY_CAPABILITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODES_SHARE_SET_BODY_CAPABILITY_VALUES!r}")
