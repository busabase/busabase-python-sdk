from typing import Literal

NodeShareCapability = Literal["read", "submit"]

NODE_SHARE_CAPABILITY_VALUES: set[NodeShareCapability] = {
    "read",
    "submit",
}


def check_node_share_capability(value: str) -> NodeShareCapability:
    if value in NODE_SHARE_CAPABILITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODE_SHARE_CAPABILITY_VALUES!r}")
