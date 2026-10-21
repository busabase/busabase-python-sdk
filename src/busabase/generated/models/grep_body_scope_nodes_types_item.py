from typing import Literal

GrepBodyScopeNodesTypesItem = Literal["doc", "html", "whiteboard", "workflow"]

GREP_BODY_SCOPE_NODES_TYPES_ITEM_VALUES: set[GrepBodyScopeNodesTypesItem] = {
    "doc",
    "html",
    "whiteboard",
    "workflow",
}


def check_grep_body_scope_nodes_types_item(value: str) -> GrepBodyScopeNodesTypesItem:
    if value in GREP_BODY_SCOPE_NODES_TYPES_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GREP_BODY_SCOPE_NODES_TYPES_ITEM_VALUES!r}")
