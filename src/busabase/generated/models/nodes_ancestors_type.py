from typing import Literal

NodesAncestorsType = Literal[
    "airapp", "base", "doc", "drive", "file", "folder", "form", "html", "skill", "whiteboard", "workflow"
]

NODES_ANCESTORS_TYPE_VALUES: set[NodesAncestorsType] = {
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


def check_nodes_ancestors_type(value: str) -> NodesAncestorsType:
    if value in NODES_ANCESTORS_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODES_ANCESTORS_TYPE_VALUES!r}")
