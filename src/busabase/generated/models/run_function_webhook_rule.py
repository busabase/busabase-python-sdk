from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.run_function_webhook_rule_event_type import (
    RunFunctionWebhookRuleEventType,
    check_run_function_webhook_rule_event_type,
)
from ..models.run_function_webhook_rule_last_status_type_0 import (
    RunFunctionWebhookRuleLastStatusType0,
    check_run_function_webhook_rule_last_status_type_0,
)

if TYPE_CHECKING:
    from ..models.webhook_function_config import WebhookFunctionConfig


T = TypeVar("T", bound="RunFunctionWebhookRule")


@_attrs_define
class RunFunctionWebhookRule:
    """
    Attributes:
        id (str):
        space_id (str):
        base_id (None | str):
        name (str):
        event_type (RunFunctionWebhookRuleEventType):
        enabled (bool):
        created_by (str):
        created_at (str):
        updated_at (str):
        last_triggered_at (None | str):
        last_status (None | RunFunctionWebhookRuleLastStatusType0):
        action_kind (Literal['run_function']):
        config (WebhookFunctionConfig):
    """

    id: str
    space_id: str
    base_id: None | str
    name: str
    event_type: RunFunctionWebhookRuleEventType
    enabled: bool
    created_by: str
    created_at: str
    updated_at: str
    last_triggered_at: None | str
    last_status: None | RunFunctionWebhookRuleLastStatusType0
    action_kind: Literal["run_function"]
    config: WebhookFunctionConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        space_id = self.space_id

        base_id: None | str
        base_id = self.base_id

        name = self.name

        event_type: str = self.event_type

        enabled = self.enabled

        created_by = self.created_by

        created_at = self.created_at

        updated_at = self.updated_at

        last_triggered_at: None | str
        last_triggered_at = self.last_triggered_at

        last_status: None | str
        if isinstance(self.last_status, str):
            last_status = self.last_status
        else:
            last_status = self.last_status

        action_kind = self.action_kind

        config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "spaceId": space_id,
                "baseId": base_id,
                "name": name,
                "eventType": event_type,
                "enabled": enabled,
                "createdBy": created_by,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "lastTriggeredAt": last_triggered_at,
                "lastStatus": last_status,
                "actionKind": action_kind,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_function_config import WebhookFunctionConfig

        d = dict(src_dict)
        id = d.pop("id")

        space_id = d.pop("spaceId")

        def _parse_base_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        base_id = _parse_base_id(d.pop("baseId"))

        name = d.pop("name")

        event_type = check_run_function_webhook_rule_event_type(d.pop("eventType"))

        enabled = d.pop("enabled")

        created_by = d.pop("createdBy")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_last_triggered_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_triggered_at = _parse_last_triggered_at(d.pop("lastTriggeredAt"))

        def _parse_last_status(data: object) -> None | RunFunctionWebhookRuleLastStatusType0:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_status_type_0 = check_run_function_webhook_rule_last_status_type_0(data)

                return last_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunFunctionWebhookRuleLastStatusType0, data)

        last_status = _parse_last_status(d.pop("lastStatus"))

        action_kind = cast(Literal["run_function"], d.pop("actionKind"))
        if action_kind != "run_function":
            raise ValueError(f"actionKind must match const 'run_function', got '{action_kind}'")

        config = WebhookFunctionConfig.from_dict(d.pop("config"))

        run_function_webhook_rule = cls(
            id=id,
            space_id=space_id,
            base_id=base_id,
            name=name,
            event_type=event_type,
            enabled=enabled,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            last_triggered_at=last_triggered_at,
            last_status=last_status,
            action_kind=action_kind,
            config=config,
        )

        run_function_webhook_rule.additional_properties = d
        return run_function_webhook_rule

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
