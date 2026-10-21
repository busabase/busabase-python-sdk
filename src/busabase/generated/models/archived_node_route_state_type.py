from typing import Literal

ArchivedNodeRouteStateType = Literal[
    "airapp", "base", "doc", "drive", "file", "folder", "form", "html", "skill", "whiteboard", "workflow"
]

ARCHIVED_NODE_ROUTE_STATE_TYPE_VALUES: set[ArchivedNodeRouteStateType] = {
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


def check_archived_node_route_state_type(value: str) -> ArchivedNodeRouteStateType:
    if value in ARCHIVED_NODE_ROUTE_STATE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARCHIVED_NODE_ROUTE_STATE_TYPE_VALUES!r}")
