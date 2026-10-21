from typing import Literal

NodesShareListResponse200ItemCapability = Literal["read", "submit"]

NODES_SHARE_LIST_RESPONSE_200_ITEM_CAPABILITY_VALUES: set[NodesShareListResponse200ItemCapability] = {
    "read",
    "submit",
}


def check_nodes_share_list_response_200_item_capability(value: str) -> NodesShareListResponse200ItemCapability:
    if value in NODES_SHARE_LIST_RESPONSE_200_ITEM_CAPABILITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NODES_SHARE_LIST_RESPONSE_200_ITEM_CAPABILITY_VALUES!r}"
    )
