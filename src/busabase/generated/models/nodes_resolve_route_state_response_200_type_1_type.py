from typing import Literal

NodesResolveRouteStateResponse200Type1Type = Literal[
    "airapp", "base", "doc", "drive", "file", "folder", "form", "html", "skill", "whiteboard", "workflow"
]

NODES_RESOLVE_ROUTE_STATE_RESPONSE_200_TYPE_1_TYPE_VALUES: set[NodesResolveRouteStateResponse200Type1Type] = {
    "airapp",
    "base",
    "doc",
    "drive",
    "file",
    "folder",
    "form",
    "html",
    "skill",
    "whiteboard",
    "workflow",
}


def check_nodes_resolve_route_state_response_200_type_1_type(value: str) -> NodesResolveRouteStateResponse200Type1Type:
    if value in NODES_RESOLVE_ROUTE_STATE_RESPONSE_200_TYPE_1_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NODES_RESOLVE_ROUTE_STATE_RESPONSE_200_TYPE_1_TYPE_VALUES!r}"
    )
