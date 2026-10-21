from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_events_create_body_action import AuditEventsCreateBodyAction, check_audit_events_create_body_action
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_events_create_body_metadata import AuditEventsCreateBodyMetadata


T = TypeVar("T", bound="AuditEventsCreateBody")


@_attrs_define
class AuditEventsCreateBody:
    """
    Attributes:
        action (AuditEventsCreateBodyAction):
        actor_id (str | Unset):  Default: 'local-viewer'.
        base_id (None | str | Unset):
        record_id (None | str | Unset):
        change_request_id (None | str | Unset):
        operation_id (None | str | Unset):
        commit_id (None | str | Unset):
        metadata (AuditEventsCreateBodyMetadata | Unset):
    """

    action: AuditEventsCreateBodyAction
    actor_id: str | Unset = "local-viewer"
    base_id: None | str | Unset = UNSET
    record_id: None | str | Unset = UNSET
    change_request_id: None | str | Unset = UNSET
    operation_id: None | str | Unset = UNSET
    commit_id: None | str | Unset = UNSET
    metadata: AuditEventsCreateBodyMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        actor_id = self.actor_id

        base_id: None | str | Unset
        if isinstance(self.base_id, Unset):
            base_id = UNSET
        else:
            base_id = self.base_id

        record_id: None | str | Unset
        if isinstance(self.record_id, Unset):
            record_id = UNSET
        else:
            record_id = self.record_id

        change_request_id: None | str | Unset
        if isinstance(self.change_request_id, Unset):
            change_request_id = UNSET
        else:
            change_request_id = self.change_request_id

        operation_id: None | str | Unset
        if isinstance(self.operation_id, Unset):
            operation_id = UNSET
        else:
            operation_id = self.operation_id

        commit_id: None | str | Unset
        if isinstance(self.commit_id, Unset):
            commit_id = UNSET
        else:
            commit_id = self.commit_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if actor_id is not UNSET:
            field_dict["actorId"] = actor_id
        if base_id is not UNSET:
            field_dict["baseId"] = base_id
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if change_request_id is not UNSET:
            field_dict["changeRequestId"] = change_request_id
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_events_create_body_metadata import AuditEventsCreateBodyMetadata

        d = dict(src_dict)
        action = check_audit_events_create_body_action(d.pop("action"))

        actor_id = d.pop("actorId", UNSET)

        def _parse_base_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_id = _parse_base_id(d.pop("baseId", UNSET))

        def _parse_record_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        record_id = _parse_record_id(d.pop("recordId", UNSET))

        def _parse_change_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        change_request_id = _parse_change_request_id(d.pop("changeRequestId", UNSET))

        def _parse_operation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operation_id = _parse_operation_id(d.pop("operationId", UNSET))

        def _parse_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_id = _parse_commit_id(d.pop("commitId", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: AuditEventsCreateBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AuditEventsCreateBodyMetadata.from_dict(_metadata)

        audit_events_create_body = cls(
            action=action,
            actor_id=actor_id,
            base_id=base_id,
            record_id=record_id,
            change_request_id=change_request_id,
            operation_id=operation_id,
            commit_id=commit_id,
            metadata=metadata,
        )

        audit_events_create_body.additional_properties = d
        return audit_events_create_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
