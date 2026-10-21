from typing import Literal

NodesListTypesType1 = Literal[
    "airapp", "base", "doc", "drive", "file", "folder", "form", "html", "skill", "whiteboard", "workflow"
]

NODES_LIST_TYPES_TYPE_1_VALUES: set[NodesListTypesType1] = {
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


def check_nodes_list_types_type_1(value: str) -> NodesListTypesType1:
    if value in NODES_LIST_TYPES_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODES_LIST_TYPES_TYPE_1_VALUES!r}")
