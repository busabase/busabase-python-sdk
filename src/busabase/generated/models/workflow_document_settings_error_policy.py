from typing import Literal

WorkflowDocumentSettingsErrorPolicy = Literal["continue", "stop"]

WORKFLOW_DOCUMENT_SETTINGS_ERROR_POLICY_VALUES: set[WorkflowDocumentSettingsErrorPolicy] = {
    "continue",
    "stop",
}


def check_workflow_document_settings_error_policy(value: str) -> WorkflowDocumentSettingsErrorPolicy:
    if value in WORKFLOW_DOCUMENT_SETTINGS_ERROR_POLICY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_DOCUMENT_SETTINGS_ERROR_POLICY_VALUES!r}")
