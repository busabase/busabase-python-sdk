from typing import Literal

NodesCreateChangeRequestBodyOperationsItemType0NodeType = Literal[
    "airapp", "base", "doc", "drive", "file", "folder", "form", "html", "skill", "whiteboard", "workflow"
]

NODES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_0_NODE_TYPE_VALUES: set[
    NodesCreateChangeRequestBodyOperationsItemType0NodeType
] = {
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


def check_nodes_create_change_request_body_operations_item_type_0_node_type(
    value: str,
) -> NodesCreateChangeRequestBodyOperationsItemType0NodeType:
    if value in NODES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_0_NODE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NODES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_0_NODE_TYPE_VALUES!r}"
    )
