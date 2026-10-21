from typing import Literal

AuditEventAction = Literal[
    "airapp.created",
    "asset.deleted",
    "asset.metadata_updated",
    "asset.text_marked_none",
    "asset.text_written",
    "base.created",
    "change_request.created",
    "change_request.deleted",
    "change_request.merged",
    "change_request.reviewed",
    "change_request.updated",
    "doc.created",
    "doc.updated",
    "drive.created",
    "field.created",
    "file.created",
    "node.agent_prompts_updated",
    "node.metadata_updated",
    "node.purged",
    "node.settings_updated",
    "record.viewed",
    "skill.created",
]

AUDIT_EVENT_ACTION_VALUES: set[AuditEventAction] = {
    "airapp.created",
    "asset.deleted",
    "asset.metadata_updated",
    "asset.text_marked_none",
    "asset.text_written",
    "base.created",
    "change_request.created",
    "change_request.deleted",
    "change_request.merged",
    "change_request.reviewed",
    "change_request.updated",
    "doc.created",
    "doc.updated",
    "drive.created",
    "field.created",
    "file.created",
    "node.agent_prompts_updated",
    "node.metadata_updated",
    "node.purged",
    "node.settings_updated",
    "record.viewed",
    "skill.created",
}


def check_audit_event_action(value: str) -> AuditEventAction:
    if value in AUDIT_EVENT_ACTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AUDIT_EVENT_ACTION_VALUES!r}")
