from typing import Literal

NodesPrincipalsAddBodyPrincipalType = Literal["space", "user"]

NODES_PRINCIPALS_ADD_BODY_PRINCIPAL_TYPE_VALUES: set[NodesPrincipalsAddBodyPrincipalType] = {
    "space",
    "user",
}


def check_nodes_principals_add_body_principal_type(value: str) -> NodesPrincipalsAddBodyPrincipalType:
    if value in NODES_PRINCIPALS_ADD_BODY_PRINCIPAL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODES_PRINCIPALS_ADD_BODY_PRINCIPAL_TYPE_VALUES!r}")
