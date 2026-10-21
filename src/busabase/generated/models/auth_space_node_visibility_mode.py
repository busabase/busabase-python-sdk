from typing import Literal

AuthSpaceNodeVisibilityMode = Literal["open", "restricted"]

AUTH_SPACE_NODE_VISIBILITY_MODE_VALUES: set[AuthSpaceNodeVisibilityMode] = {
    "open",
    "restricted",
}


def check_auth_space_node_visibility_mode(value: str) -> AuthSpaceNodeVisibilityMode:
    if value in AUTH_SPACE_NODE_VISIBILITY_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AUTH_SPACE_NODE_VISIBILITY_MODE_VALUES!r}")
