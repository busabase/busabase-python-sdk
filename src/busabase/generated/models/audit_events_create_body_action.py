from typing import Literal

AuditEventsCreateBodyAction = Literal[
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

AUDIT_EVENTS_CREATE_BODY_ACTION_VALUES: set[AuditEventsCreateBodyAction] = {
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


def check_audit_events_create_body_action(value: str) -> AuditEventsCreateBodyAction:
    if value in AUDIT_EVENTS_CREATE_BODY_ACTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AUDIT_EVENTS_CREATE_BODY_ACTION_VALUES!r}")
