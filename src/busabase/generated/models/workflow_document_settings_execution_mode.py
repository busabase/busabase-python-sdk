from typing import Literal

WorkflowDocumentSettingsExecutionMode = Literal["event", "manual"]

WORKFLOW_DOCUMENT_SETTINGS_EXECUTION_MODE_VALUES: set[WorkflowDocumentSettingsExecutionMode] = {
    "event",
    "manual",
}


def check_workflow_document_settings_execution_mode(value: str) -> WorkflowDocumentSettingsExecutionMode:
    if value in WORKFLOW_DOCUMENT_SETTINGS_EXECUTION_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_DOCUMENT_SETTINGS_EXECUTION_MODE_VALUES!r}")
