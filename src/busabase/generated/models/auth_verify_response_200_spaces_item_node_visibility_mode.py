from typing import Literal

AuthVerifyResponse200SpacesItemNodeVisibilityMode = Literal["open", "restricted"]

AUTH_VERIFY_RESPONSE_200_SPACES_ITEM_NODE_VISIBILITY_MODE_VALUES: set[
    AuthVerifyResponse200SpacesItemNodeVisibilityMode
] = {
    "open",
    "restricted",
}


def check_auth_verify_response_200_spaces_item_node_visibility_mode(
    value: str,
) -> AuthVerifyResponse200SpacesItemNodeVisibilityMode:
    if value in AUTH_VERIFY_RESPONSE_200_SPACES_ITEM_NODE_VISIBILITY_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUTH_VERIFY_RESPONSE_200_SPACES_ITEM_NODE_VISIBILITY_MODE_VALUES!r}"
    )
