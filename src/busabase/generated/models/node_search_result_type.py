from typing import Literal

NodeSearchResultType = Literal[
    "airapp", "base", "doc", "drive", "file", "folder", "form", "html", "skill", "whiteboard", "workflow"
]

NODE_SEARCH_RESULT_TYPE_VALUES: set[NodeSearchResultType] = {
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


def check_node_search_result_type(value: str) -> NodeSearchResultType:
    if value in NODE_SEARCH_RESULT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODE_SEARCH_RESULT_TYPE_VALUES!r}")
