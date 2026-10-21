from typing import Literal

NodesListStatus = Literal["active", "archived"]

NODES_LIST_STATUS_VALUES: set[NodesListStatus] = {
    "active",
    "archived",
}


def check_nodes_list_status(value: str) -> NodesListStatus:
    if value in NODES_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODES_LIST_STATUS_VALUES!r}")
