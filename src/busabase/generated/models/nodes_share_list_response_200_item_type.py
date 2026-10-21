from typing import Literal

NodesShareListResponse200ItemType = Literal[
    "airapp", "base", "doc", "drive", "file", "folder", "form", "html", "skill", "whiteboard", "workflow"
]

NODES_SHARE_LIST_RESPONSE_200_ITEM_TYPE_VALUES: set[NodesShareListResponse200ItemType] = {
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


def check_nodes_share_list_response_200_item_type(value: str) -> NodesShareListResponse200ItemType:
    if value in NODES_SHARE_LIST_RESPONSE_200_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODES_SHARE_LIST_RESPONSE_200_ITEM_TYPE_VALUES!r}")
