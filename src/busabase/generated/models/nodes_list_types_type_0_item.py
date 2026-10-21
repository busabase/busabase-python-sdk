from typing import Literal

NodesListTypesType0Item = Literal[
    "airapp", "base", "doc", "drive", "file", "folder", "form", "html", "skill", "whiteboard", "workflow"
]

NODES_LIST_TYPES_TYPE_0_ITEM_VALUES: set[NodesListTypesType0Item] = {
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


def check_nodes_list_types_type_0_item(value: str) -> NodesListTypesType0Item:
    if value in NODES_LIST_TYPES_TYPE_0_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODES_LIST_TYPES_TYPE_0_ITEM_VALUES!r}")
