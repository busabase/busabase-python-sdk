from typing import Literal

NodesPrincipalsListResponse200ItemRole = Literal["changeRequest", "manage", "read", "write"]

NODES_PRINCIPALS_LIST_RESPONSE_200_ITEM_ROLE_VALUES: set[NodesPrincipalsListResponse200ItemRole] = {
    "changeRequest",
    "manage",
    "read",
    "write",
}


def check_nodes_principals_list_response_200_item_role(value: str) -> NodesPrincipalsListResponse200ItemRole:
    if value in NODES_PRINCIPALS_LIST_RESPONSE_200_ITEM_ROLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NODES_PRINCIPALS_LIST_RESPONSE_200_ITEM_ROLE_VALUES!r}"
    )
