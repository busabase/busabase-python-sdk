from typing import Literal

CreateNodeOperationNodeType = Literal[
    "airapp", "base", "doc", "drive", "file", "folder", "form", "html", "skill", "whiteboard", "workflow"
]

CREATE_NODE_OPERATION_NODE_TYPE_VALUES: set[CreateNodeOperationNodeType] = {
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


def check_create_node_operation_node_type(value: str) -> CreateNodeOperationNodeType:
    if value in CREATE_NODE_OPERATION_NODE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_NODE_OPERATION_NODE_TYPE_VALUES!r}")
