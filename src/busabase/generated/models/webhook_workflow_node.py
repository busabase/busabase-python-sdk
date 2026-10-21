from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_workflow_node_method import WebhookWorkflowNodeMethod, check_webhook_workflow_node_method
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_node_position import WorkflowNodePosition


T = TypeVar("T", bound="WebhookWorkflowNode")


@_attrs_define
class WebhookWorkflowNode:
    """
    Attributes:
        id (str):
        position (WorkflowNodePosition):
        label (str):
        kind (Literal['webhook']):
        description (str | Unset):  Default: ''.
        method (WebhookWorkflowNodeMethod | Unset):  Default: 'POST'.
        url (str | Unset):  Default: ''.
    """

    id: str
    position: WorkflowNodePosition
    label: str
    kind: Literal["webhook"]
    description: str | Unset = ""
    method: WebhookWorkflowNodeMethod | Unset = "POST"
    url: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position.to_dict()

        label = self.label

        kind = self.kind

        description = self.description

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "position": position,
                "label": label,
                "kind": kind,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if method is not UNSET:
            field_dict["method"] = method
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_node_position import WorkflowNodePosition

        d = dict(src_dict)
        id = d.pop("id")

        position = WorkflowNodePosition.from_dict(d.pop("position"))

        label = d.pop("label")

        kind = cast(Literal["webhook"], d.pop("kind"))
        if kind != "webhook":
            raise ValueError(f"kind must match const 'webhook', got '{kind}'")

        description = d.pop("description", UNSET)

        _method = d.pop("method", UNSET)
        method: WebhookWorkflowNodeMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = check_webhook_workflow_node_method(_method)

        url = d.pop("url", UNSET)

        webhook_workflow_node = cls(
            id=id,
            position=position,
            label=label,
            kind=kind,
            description=description,
            method=method,
            url=url,
        )

        webhook_workflow_node.additional_properties = d
        return webhook_workflow_node

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
