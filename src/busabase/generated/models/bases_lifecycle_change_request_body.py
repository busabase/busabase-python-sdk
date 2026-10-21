from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasesLifecycleChangeRequestBody")


@_attrs_define
class BasesLifecycleChangeRequestBody:
    """
    Attributes:
        operation (Literal['archive'] | Literal['restore']):
        message (str | Unset):
        submitted_by (str | Unset):  Default: 'local-editor'.
        auto_merge (bool | Unset):
    """

    operation: Literal["archive", "restore"]
    message: str | Unset = UNSET
    submitted_by: str | Unset = "local-editor"
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation: Literal["archive", "restore"]
        operation = self.operation

        message = self.message

        submitted_by = self.submitted_by

        auto_merge: bool | Unset
        if isinstance(self.auto_merge, Unset):
            auto_merge = UNSET
        else:
            auto_merge = self.auto_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
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

        def _parse_operation(data: object) -> Literal["archive", "restore"]:
            operation_type_0 = cast(Literal["archive"], data)
            if operation_type_0 != "archive":
                raise ValueError(f"operation_type_0 must match const 'archive', got '{operation_type_0}'")
            return operation_type_0
            operation_type_1 = cast(Literal["restore"], data)
            if operation_type_1 != "restore":
                raise ValueError(f"operation_type_1 must match const 'restore', got '{operation_type_1}'")
            return operation_type_1

        operation = _parse_operation(d.pop("operation"))

        message = d.pop("message", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        def _parse_auto_merge(data: object) -> bool | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset, data)

        auto_merge = _parse_auto_merge(d.pop("autoMerge", UNSET))

        bases_lifecycle_change_request_body = cls(
            operation=operation,
            message=message,
            submitted_by=submitted_by,
            auto_merge=auto_merge,
        )

        bases_lifecycle_change_request_body.additional_properties = d
        return bases_lifecycle_change_request_body

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
