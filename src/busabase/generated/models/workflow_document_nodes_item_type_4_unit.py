from typing import Literal

WorkflowDocumentNodesItemType4Unit = Literal["days", "hours", "minutes"]

WORKFLOW_DOCUMENT_NODES_ITEM_TYPE_4_UNIT_VALUES: set[WorkflowDocumentNodesItemType4Unit] = {
    "days",
    "hours",
    "minutes",
}


def check_workflow_document_nodes_item_type_4_unit(value: str) -> WorkflowDocumentNodesItemType4Unit:
    if value in WORKFLOW_DOCUMENT_NODES_ITEM_TYPE_4_UNIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_DOCUMENT_NODES_ITEM_TYPE_4_UNIT_VALUES!r}")
