from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewsChangeRequestBodyType2")


@_attrs_define
class ViewsChangeRequestBodyType2:
    """
    Attributes:
        operation (Literal['delete']):
        view_id (str):
        message (str | Unset):  Default: 'Delete view'.
        submitted_by (str | Unset):  Default: 'local-producer'.
        auto_merge (bool | Unset): Whether to approve and merge this view change immediately. Omitted defaults to
            merging immediately if the actor has write access on the Base's node, otherwise falling back to a pending Change
            Request; pass explicit false to force review even with write access.
    """

    operation: Literal["delete"]
    view_id: str
    message: str | Unset = "Delete view"
    submitted_by: str | Unset = "local-producer"
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation

        view_id = self.view_id

        message = self.message

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
        if message is not UNSET:
            field_dict["message"] = message
        if submitted_by is not UNSET:
            field_dict["submittedBy"] = submitted_by
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        operation = cast(Literal["delete"], d.pop("operation"))
        if operation != "delete":
            raise ValueError(f"operation must match const 'delete', got '{operation}'")

        view_id = d.pop("viewId")

        message = d.pop("message", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        views_change_request_body_type_2 = cls(
            operation=operation,
            view_id=view_id,
            message=message,
            submitted_by=submitted_by,
            auto_merge=auto_merge,
        )

        views_change_request_body_type_2.additional_properties = d
        return views_change_request_body_type_2

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
