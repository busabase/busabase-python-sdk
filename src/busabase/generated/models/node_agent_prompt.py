from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_agent_prompt_intent import NodeAgentPromptIntent, check_node_agent_prompt_intent
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="NodeAgentPrompt")


@_attrs_define
class NodeAgentPrompt:
    """
    Attributes:
        key (str):
        label (LocalizedText | str): i18n string
        body (LocalizedText | str): i18n string
        intent (NodeAgentPromptIntent | Unset):
    """

    key: str
    label: LocalizedText | str
    body: LocalizedText | str
    intent: NodeAgentPromptIntent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_text import LocalizedText

        key = self.key

        label: dict[str, Any] | str
        if isinstance(self.label, LocalizedText):
            label = self.label.to_dict()
        else:
            label = self.label

        body: dict[str, Any] | str
        if isinstance(self.body, LocalizedText):
            body = self.body.to_dict()
        else:
            body = self.body

        intent: str | Unset = UNSET
        if not isinstance(self.intent, Unset):
            intent = self.intent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "body": body,
            }
        )
        if intent is not UNSET:
            field_dict["intent"] = intent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.localized_text import LocalizedText

        d = dict(src_dict)
        key = d.pop("key")

        def _parse_label(data: object) -> LocalizedText | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                label_type_1 = LocalizedText.from_dict(data)

                return label_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedText | str, data)

        label = _parse_label(d.pop("label"))

        def _parse_body(data: object) -> LocalizedText | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                body_type_1 = LocalizedText.from_dict(data)

                return body_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedText | str, data)

        body = _parse_body(d.pop("body"))

        _intent = d.pop("intent", UNSET)
        intent: NodeAgentPromptIntent | Unset
        if isinstance(_intent, Unset):
            intent = UNSET
        else:
            intent = check_node_agent_prompt_intent(_intent)

        node_agent_prompt = cls(
            key=key,
            label=label,
            body=body,
            intent=intent,
        )

        node_agent_prompt.additional_properties = d
        return node_agent_prompt

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
