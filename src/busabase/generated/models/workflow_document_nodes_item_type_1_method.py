from typing import Literal

WorkflowDocumentNodesItemType1Method = Literal["DELETE", "GET", "PATCH", "POST", "PUT"]

WORKFLOW_DOCUMENT_NODES_ITEM_TYPE_1_METHOD_VALUES: set[WorkflowDocumentNodesItemType1Method] = {
    "DELETE",
    "GET",
    "PATCH",
    "POST",
    "PUT",
}


def check_workflow_document_nodes_item_type_1_method(value: str) -> WorkflowDocumentNodesItemType1Method:
    if value in WORKFLOW_DOCUMENT_NODES_ITEM_TYPE_1_METHOD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKFLOW_DOCUMENT_NODES_ITEM_TYPE_1_METHOD_VALUES!r}"
    )
