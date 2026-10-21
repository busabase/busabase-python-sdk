from typing import Literal

NodesPrincipalsRemoveBodyPrincipalType = Literal["space", "user"]

NODES_PRINCIPALS_REMOVE_BODY_PRINCIPAL_TYPE_VALUES: set[NodesPrincipalsRemoveBodyPrincipalType] = {
    "space",
    "user",
}


def check_nodes_principals_remove_body_principal_type(value: str) -> NodesPrincipalsRemoveBodyPrincipalType:
    if value in NODES_PRINCIPALS_REMOVE_BODY_PRINCIPAL_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NODES_PRINCIPALS_REMOVE_BODY_PRINCIPAL_TYPE_VALUES!r}"
    )
