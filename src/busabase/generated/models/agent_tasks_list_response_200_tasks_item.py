from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentTasksListResponse200TasksItem")


@_attrs_define
class AgentTasksListResponse200TasksItem:
    """
    Attributes:
        id (float | str):
        title (str):
        description (None | str):
        status (str):
        priority (str):
        created_at (str):
        completed_at (None | str):
    """

    id: float | str
    title: str
    description: None | str
    status: str
    priority: str
    created_at: str
    completed_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: float | str
        id = self.id

        title = self.title

        description: None | str
        description = self.description

        status = self.status

        priority = self.priority

        created_at = self.created_at

        completed_at: None | str
        completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "description": description,
                "status": status,
                "priority": priority,
                "createdAt": created_at,
                "completedAt": completed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_id(data: object) -> float | str:
            return cast(float | str, data)

        id = _parse_id(d.pop("id"))

        title = d.pop("title")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        status = d.pop("status")

        priority = d.pop("priority")

        created_at = d.pop("createdAt")

        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completedAt"))

        agent_tasks_list_response_200_tasks_item = cls(
            id=id,
            title=title,
            description=description,
            status=status,
            priority=priority,
            created_at=created_at,
            completed_at=completed_at,
        )

        agent_tasks_list_response_200_tasks_item.additional_properties = d
        return agent_tasks_list_response_200_tasks_item

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
