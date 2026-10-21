from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_update_body_event_type import WebhooksUpdateBodyEventType, check_webhooks_update_body_event_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_function_config import WebhookFunctionConfig
    from ..models.webhooks_update_body_config_type_0 import WebhooksUpdateBodyConfigType0


T = TypeVar("T", bound="WebhooksUpdateBody")


@_attrs_define
class WebhooksUpdateBody:
    """
    Attributes:
        name (str):
        event_type (WebhooksUpdateBodyEventType):
        action_kind (Literal['notify_agent'] | Literal['run_function'] | Literal['webhook']):
        config (WebhookFunctionConfig | WebhooksUpdateBodyConfigType0):
        base_id (None | str | Unset):
        enabled (bool | Unset):  Default: True.
    """

    name: str
    event_type: WebhooksUpdateBodyEventType
    action_kind: Literal["notify_agent", "run_function", "webhook"]
    config: WebhookFunctionConfig | WebhooksUpdateBodyConfigType0
    base_id: None | str | Unset = UNSET
    enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhooks_update_body_config_type_0 import WebhooksUpdateBodyConfigType0

        name = self.name

        event_type: str = self.event_type

        action_kind: Literal["notify_agent", "run_function", "webhook"]
        action_kind = self.action_kind

        config: dict[str, Any]
        if isinstance(self.config, WebhooksUpdateBodyConfigType0):
            config = self.config.to_dict()
        else:
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
        from ..models.webhook_function_config import WebhookFunctionConfig
        from ..models.webhooks_update_body_config_type_0 import WebhooksUpdateBodyConfigType0

        d = dict(src_dict)
        name = d.pop("name")

        event_type = check_webhooks_update_body_event_type(d.pop("eventType"))

        def _parse_action_kind(data: object) -> Literal["notify_agent", "run_function", "webhook"]:
            action_kind_type_0 = cast(Literal["webhook"], data)
            if action_kind_type_0 != "webhook":
                raise ValueError(f"actionKind_type_0 must match const 'webhook', got '{action_kind_type_0}'")
            return action_kind_type_0
            action_kind_type_1 = cast(Literal["notify_agent"], data)
            if action_kind_type_1 != "notify_agent":
                raise ValueError(f"actionKind_type_1 must match const 'notify_agent', got '{action_kind_type_1}'")
            return action_kind_type_1
            action_kind_type_2 = cast(Literal["run_function"], data)
            if action_kind_type_2 != "run_function":
                raise ValueError(f"actionKind_type_2 must match const 'run_function', got '{action_kind_type_2}'")
            return action_kind_type_2

        action_kind = _parse_action_kind(d.pop("actionKind"))

        def _parse_config(data: object) -> WebhookFunctionConfig | WebhooksUpdateBodyConfigType0:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = WebhooksUpdateBodyConfigType0.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            config_type_1 = WebhookFunctionConfig.from_dict(data)

            return config_type_1

        config = _parse_config(d.pop("config"))

        def _parse_base_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_id = _parse_base_id(d.pop("baseId", UNSET))

        enabled = d.pop("enabled", UNSET)

        webhooks_update_body = cls(
            name=name,
            event_type=event_type,
            action_kind=action_kind,
            config=config,
            base_id=base_id,
            enabled=enabled,
        )

        webhooks_update_body.additional_properties = d
        return webhooks_update_body

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
