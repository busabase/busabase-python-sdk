from typing import Literal

NodesUpdateVisibilityBodyVisibilityType0 = Literal["private", "public", "workspace"]

NODES_UPDATE_VISIBILITY_BODY_VISIBILITY_TYPE_0_VALUES: set[NodesUpdateVisibilityBodyVisibilityType0] = {
    "private",
    "public",
    "workspace",
}


def check_nodes_update_visibility_body_visibility_type_0(value: str) -> NodesUpdateVisibilityBodyVisibilityType0:
    if value in NODES_UPDATE_VISIBILITY_BODY_VISIBILITY_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NODES_UPDATE_VISIBILITY_BODY_VISIBILITY_TYPE_0_VALUES!r}"
    )
