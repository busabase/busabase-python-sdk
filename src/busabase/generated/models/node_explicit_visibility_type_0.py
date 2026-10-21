from typing import Literal

NodeExplicitVisibilityType0 = Literal["private", "public", "workspace"]

NODE_EXPLICIT_VISIBILITY_TYPE_0_VALUES: set[NodeExplicitVisibilityType0] = {
    "private",
    "public",
    "workspace",
}


def check_node_explicit_visibility_type_0(value: str) -> NodeExplicitVisibilityType0:
    if value in NODE_EXPLICIT_VISIBILITY_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODE_EXPLICIT_VISIBILITY_TYPE_0_VALUES!r}")
