from typing import Literal

NodesPrincipalsListResponse200ItemPrincipalType = Literal["space", "team", "user"]

NODES_PRINCIPALS_LIST_RESPONSE_200_ITEM_PRINCIPAL_TYPE_VALUES: set[NodesPrincipalsListResponse200ItemPrincipalType] = {
    "space",
    "team",
    "user",
}


def check_nodes_principals_list_response_200_item_principal_type(
    value: str,
) -> NodesPrincipalsListResponse200ItemPrincipalType:
    if value in NODES_PRINCIPALS_LIST_RESPONSE_200_ITEM_PRINCIPAL_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NODES_PRINCIPALS_LIST_RESPONSE_200_ITEM_PRINCIPAL_TYPE_VALUES!r}"
    )
