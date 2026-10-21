from typing import Literal

AuthVerifyResponse200SpaceNodeVisibilityMode = Literal["open", "restricted"]

AUTH_VERIFY_RESPONSE_200_SPACE_NODE_VISIBILITY_MODE_VALUES: set[AuthVerifyResponse200SpaceNodeVisibilityMode] = {
    "open",
    "restricted",
}


def check_auth_verify_response_200_space_node_visibility_mode(
    value: str,
) -> AuthVerifyResponse200SpaceNodeVisibilityMode:
    if value in AUTH_VERIFY_RESPONSE_200_SPACE_NODE_VISIBILITY_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUTH_VERIFY_RESPONSE_200_SPACE_NODE_VISIBILITY_MODE_VALUES!r}"
    )
