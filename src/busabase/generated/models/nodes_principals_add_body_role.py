from typing import Literal

NodesPrincipalsAddBodyRole = Literal["changeRequest", "manage", "read", "write"]

NODES_PRINCIPALS_ADD_BODY_ROLE_VALUES: set[NodesPrincipalsAddBodyRole] = {
    "changeRequest",
    "manage",
    "read",
    "write",
}


def check_nodes_principals_add_body_role(value: str) -> NodesPrincipalsAddBodyRole:
    if value in NODES_PRINCIPALS_ADD_BODY_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODES_PRINCIPALS_ADD_BODY_ROLE_VALUES!r}")
