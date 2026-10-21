from typing import Literal

NodesResolveRouteStateType = Literal[
    "airapp", "base", "doc", "drive", "file", "folder", "form", "html", "skill", "whiteboard", "workflow"
]

NODES_RESOLVE_ROUTE_STATE_TYPE_VALUES: set[NodesResolveRouteStateType] = {
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


def check_nodes_resolve_route_state_type(value: str) -> NodesResolveRouteStateType:
    if value in NODES_RESOLVE_ROUTE_STATE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODES_RESOLVE_ROUTE_STATE_TYPE_VALUES!r}")
