from typing import Literal

GrepNodeMatchType = Literal["doc", "html", "whiteboard", "workflow"]

GREP_NODE_MATCH_TYPE_VALUES: set[GrepNodeMatchType] = {
    "doc",
    "html",
    "whiteboard",
    "workflow",
}


def check_grep_node_match_type(value: str) -> GrepNodeMatchType:
    if value in GREP_NODE_MATCH_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GREP_NODE_MATCH_TYPE_VALUES!r}")
