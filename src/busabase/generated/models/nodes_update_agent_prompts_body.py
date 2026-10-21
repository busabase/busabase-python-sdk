from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node_agent_prompt import NodeAgentPrompt


T = TypeVar("T", bound="NodesUpdateAgentPromptsBody")


@_attrs_define
class NodesUpdateAgentPromptsBody:
    """
    Attributes:
        agent_prompts (list[NodeAgentPrompt] | None):
    """

    agent_prompts: list[NodeAgentPrompt] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_prompts: list[dict[str, Any]] | None
        if isinstance(self.agent_prompts, list):
            agent_prompts = []
            for agent_prompts_type_0_item_data in self.agent_prompts:
                agent_prompts_type_0_item = agent_prompts_type_0_item_data.to_dict()
                agent_prompts.append(agent_prompts_type_0_item)

        else:
            agent_prompts = self.agent_prompts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agentPrompts": agent_prompts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.node_agent_prompt import NodeAgentPrompt

        d = dict(src_dict)

        def _parse_agent_prompts(data: object) -> list[NodeAgentPrompt] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                agent_prompts_type_0 = []
                _agent_prompts_type_0 = data
                for agent_prompts_type_0_item_data in _agent_prompts_type_0:
                    agent_prompts_type_0_item = NodeAgentPrompt.from_dict(agent_prompts_type_0_item_data)

                    agent_prompts_type_0.append(agent_prompts_type_0_item)

                return agent_prompts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NodeAgentPrompt] | None, data)

        agent_prompts = _parse_agent_prompts(d.pop("agentPrompts"))

        nodes_update_agent_prompts_body = cls(
            agent_prompts=agent_prompts,
        )

        nodes_update_agent_prompts_body.additional_properties = d
        return nodes_update_agent_prompts_body

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
