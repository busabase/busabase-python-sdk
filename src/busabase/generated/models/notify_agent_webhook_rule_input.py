from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notify_agent_webhook_rule_input_event_type import (
    NotifyAgentWebhookRuleInputEventType,
    check_notify_agent_webhook_rule_input_event_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_http_config_input import WebhookHttpConfigInput


T = TypeVar("T", bound="NotifyAgentWebhookRuleInput")


@_attrs_define
class NotifyAgentWebhookRuleInput:
    """
    Attributes:
        name (str):
        event_type (NotifyAgentWebhookRuleInputEventType):
        action_kind (Literal['notify_agent']):
        config (WebhookHttpConfigInput):
        base_id (None | str | Unset):
        enabled (bool | Unset):  Default: True.
    """

    name: str
    event_type: NotifyAgentWebhookRuleInputEventType
    action_kind: Literal["notify_agent"]
    config: WebhookHttpConfigInput
    base_id: None | str | Unset = UNSET
    enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        event_type: str = self.event_type

        action_kind = self.action_kind

        config = self.config.to_dict()

        base_id: None | str | Unset
        if isinstance(self.base_id, Unset):
            base_id = UNSET
        else:
            base_id = self.base_id

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "eventType": event_type,
                "actionKind": action_kind,
                "config": config,
            }
        )
        if base_id is not UNSET:
            field_dict["baseId"] = base_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_http_config_input import WebhookHttpConfigInput

        d = dict(src_dict)
        name = d.pop("name")

        event_type = check_notify_agent_webhook_rule_input_event_type(d.pop("eventType"))

        action_kind = cast(Literal["notify_agent"], d.pop("actionKind"))
        if action_kind != "notify_agent":
            raise ValueError(f"actionKind must match const 'notify_agent', got '{action_kind}'")

        config = WebhookHttpConfigInput.from_dict(d.pop("config"))

        def _parse_base_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_id = _parse_base_id(d.pop("baseId", UNSET))

        enabled = d.pop("enabled", UNSET)

        notify_agent_webhook_rule_input = cls(
            name=name,
            event_type=event_type,
            action_kind=action_kind,
            config=config,
            base_id=base_id,
            enabled=enabled,
        )

        notify_agent_webhook_rule_input.additional_properties = d
        return notify_agent_webhook_rule_input

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
