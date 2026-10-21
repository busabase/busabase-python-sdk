from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_event_action import AuditEventAction, check_audit_event_action
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_event_metadata import AuditEventMetadata
    from ..models.source_attribution import SourceAttribution
    from ..models.user_ref import UserRef


T = TypeVar("T", bound="AuditEvent")


@_attrs_define
class AuditEvent:
    """
    Attributes:
        id (str):
        action (AuditEventAction):
        actor_id (str):
        base_id (None | str):
        record_id (None | str):
        change_request_id (None | str):
        operation_id (None | str):
        commit_id (None | str):
        metadata (AuditEventMetadata):
        created_at (str):
        actor (None | Unset | UserRef):
        source_attribution (None | SourceAttribution | Unset):
    """

    id: str
    action: AuditEventAction
    actor_id: str
    base_id: None | str
    record_id: None | str
    change_request_id: None | str
    operation_id: None | str
    commit_id: None | str
    metadata: AuditEventMetadata
    created_at: str
    actor: None | Unset | UserRef = UNSET
    source_attribution: None | SourceAttribution | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.source_attribution import SourceAttribution
        from ..models.user_ref import UserRef

        id = self.id

        action: str = self.action

        actor_id = self.actor_id

        base_id: None | str
        base_id = self.base_id

        record_id: None | str
        record_id = self.record_id

        change_request_id: None | str
        change_request_id = self.change_request_id

        operation_id: None | str
        operation_id = self.operation_id

        commit_id: None | str
        commit_id = self.commit_id

        metadata = self.metadata.to_dict()

        created_at = self.created_at

        actor: dict[str, Any] | None | Unset
        if isinstance(self.actor, Unset):
            actor = UNSET
        elif isinstance(self.actor, UserRef):
            actor = self.actor.to_dict()
        else:
            actor = self.actor

        source_attribution: dict[str, Any] | None | Unset
        if isinstance(self.source_attribution, Unset):
            source_attribution = UNSET
        elif isinstance(self.source_attribution, SourceAttribution):
            source_attribution = self.source_attribution.to_dict()
        else:
            source_attribution = self.source_attribution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "action": action,
                "actorId": actor_id,
                "baseId": base_id,
                "recordId": record_id,
                "changeRequestId": change_request_id,
                "operationId": operation_id,
                "commitId": commit_id,
                "metadata": metadata,
                "createdAt": created_at,
            }
        )
        if actor is not UNSET:
            field_dict["actor"] = actor
        if source_attribution is not UNSET:
            field_dict["sourceAttribution"] = source_attribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_event_metadata import AuditEventMetadata
        from ..models.source_attribution import SourceAttribution
        from ..models.user_ref import UserRef

        d = dict(src_dict)
        id = d.pop("id")

        action = check_audit_event_action(d.pop("action"))

        actor_id = d.pop("actorId")

        def _parse_base_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        base_id = _parse_base_id(d.pop("baseId"))

        def _parse_record_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        record_id = _parse_record_id(d.pop("recordId"))

        def _parse_change_request_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        change_request_id = _parse_change_request_id(d.pop("changeRequestId"))

        def _parse_operation_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        operation_id = _parse_operation_id(d.pop("operationId"))

        def _parse_commit_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        commit_id = _parse_commit_id(d.pop("commitId"))

        metadata = AuditEventMetadata.from_dict(d.pop("metadata"))

        created_at = d.pop("createdAt")

        def _parse_actor(data: object) -> None | Unset | UserRef:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_0 = UserRef.from_dict(data)

                return actor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserRef, data)

        actor = _parse_actor(d.pop("actor", UNSET))

        def _parse_source_attribution(data: object) -> None | SourceAttribution | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_attribution_type_0 = SourceAttribution.from_dict(data)

                return source_attribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceAttribution | Unset, data)

        source_attribution = _parse_source_attribution(d.pop("sourceAttribution", UNSET))

        audit_event = cls(
            id=id,
            action=action,
            actor_id=actor_id,
            base_id=base_id,
            record_id=record_id,
            change_request_id=change_request_id,
            operation_id=operation_id,
            commit_id=commit_id,
            metadata=metadata,
            created_at=created_at,
            actor=actor,
            source_attribution=source_attribution,
        )

        audit_event.additional_properties = d
        return audit_event

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
