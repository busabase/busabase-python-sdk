from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NodesUpdateAgentPromptsBodyAgentPromptsType0ItemLabelType1")


@_attrs_define
class NodesUpdateAgentPromptsBodyAgentPromptsType0ItemLabelType1:
    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        nodes_update_agent_prompts_body_agent_prompts_type_0_item_label_type_1 = cls()

        nodes_update_agent_prompts_body_agent_prompts_type_0_item_label_type_1.additional_properties = d
        return nodes_update_agent_prompts_body_agent_prompts_type_0_item_label_type_1

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
