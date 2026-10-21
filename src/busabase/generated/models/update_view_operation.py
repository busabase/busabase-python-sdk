from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_view_operation_type import UpdateViewOperationType, check_update_view_operation_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_view_operation_config import UpdateViewOperationConfig


T = TypeVar("T", bound="UpdateViewOperation")


@_attrs_define
class UpdateViewOperation:
    """
    Attributes:
        operation (Literal['update']):
        view_id (str):
        config (UpdateViewOperationConfig | Unset): Only supplied config keys change; empty arrays and null clear
            supported settings.
        description (str | Unset):
        message (str | Unset):  Default: 'Update view'.
        name (str | Unset):
        type_ (UpdateViewOperationType | Unset):
        position (int | Unset): Move the view to this 0-based index among the Base's active views; the others shift to
            make room. The order is shared by everyone, and the leftmost view (0) is the one the Base opens on. Out-of-range
            values clamp to the end.
        submitted_by (str | Unset):  Default: 'local-producer'.
        auto_merge (bool | Unset): Whether to approve and merge this view change immediately. Omitted defaults to
            merging immediately if the actor has write access on the Base's node, otherwise falling back to a pending Change
            Request; pass explicit false to force review even with write access.
    """

    operation: Literal["update"]
    view_id: str
    config: UpdateViewOperationConfig | Unset = UNSET
    description: str | Unset = UNSET
    message: str | Unset = "Update view"
    name: str | Unset = UNSET
    type_: UpdateViewOperationType | Unset = UNSET
    position: int | Unset = UNSET
    submitted_by: str | Unset = "local-producer"
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation

        view_id = self.view_id

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        description = self.description

        message = self.message

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        position = self.position

        submitted_by = self.submitted_by

        auto_merge = self.auto_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
                "viewId": view_id,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if description is not UNSET:
            field_dict["description"] = description
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if position is not UNSET:
            field_dict["position"] = position
        if submitted_by is not UNSET:
            field_dict["submittedBy"] = submitted_by
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_view_operation_config import UpdateViewOperationConfig

        d = dict(src_dict)
        operation = cast(Literal["update"], d.pop("operation"))
        if operation != "update":
            raise ValueError(f"operation must match const 'update', got '{operation}'")

        view_id = d.pop("viewId")

        _config = d.pop("config", UNSET)
        config: UpdateViewOperationConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = UpdateViewOperationConfig.from_dict(_config)

        description = d.pop("description", UNSET)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: UpdateViewOperationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_update_view_operation_type(_type_)

        position = d.pop("position", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        update_view_operation = cls(
            operation=operation,
            view_id=view_id,
            config=config,
            description=description,
            message=message,
            name=name,
            type_=type_,
            position=position,
            submitted_by=submitted_by,
            auto_merge=auto_merge,
        )

        update_view_operation.additional_properties = d
        return update_view_operation

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
