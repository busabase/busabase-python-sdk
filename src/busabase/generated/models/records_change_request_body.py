from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.records_change_request_body_delete_mode import (
    RecordsChangeRequestBodyDeleteMode,
    check_records_change_request_body_delete_mode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.records_change_request_body_fields import RecordsChangeRequestBodyFields


T = TypeVar("T", bound="RecordsChangeRequestBody")


@_attrs_define
class RecordsChangeRequestBody:
    """
    Attributes:
        operation (Literal['delete'] | Literal['restore'] | Literal['update']):
        fields (RecordsChangeRequestBodyFields | Unset): Updated field values keyed by field slug. A field id or its
            exact display name (any language, unambiguous) is mapped to the slug; a write in which no key names a field of
            the Base is a 400 listing the valid slugs. If you set the base's PRIMARY field (its first field), keep it a
            short human-readable name — it is the record's display title everywhere.
        message (str | Unset):
        author (str | Unset):  Default: 'local-producer'.
        base_commit_id (str | Unset):
        auto_merge (bool | Unset):
        submitted_by (str | Unset):
        delete_mode (RecordsChangeRequestBodyDeleteMode | Unset):  Default: 'archive'.
    """

    operation: Literal["delete", "restore", "update"]
    fields: RecordsChangeRequestBodyFields | Unset = UNSET
    message: str | Unset = UNSET
    author: str | Unset = "local-producer"
    base_commit_id: str | Unset = UNSET
    auto_merge: bool | Unset = UNSET
    submitted_by: str | Unset = UNSET
    delete_mode: RecordsChangeRequestBodyDeleteMode | Unset = "archive"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation: Literal["delete", "restore", "update"]
        operation = self.operation

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        message: str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        author = self.author

        base_commit_id = self.base_commit_id

        auto_merge: bool | Unset
        if isinstance(self.auto_merge, Unset):
            auto_merge = UNSET
        else:
            auto_merge = self.auto_merge

        submitted_by: str | Unset
        if isinstance(self.submitted_by, Unset):
            submitted_by = UNSET
        else:
            submitted_by = self.submitted_by

        delete_mode: str | Unset = UNSET
        if not isinstance(self.delete_mode, Unset):
            delete_mode = self.delete_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields
        if message is not UNSET:
            field_dict["message"] = message
        if author is not UNSET:
            field_dict["author"] = author
        if base_commit_id is not UNSET:
            field_dict["baseCommitId"] = base_commit_id
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge
        if submitted_by is not UNSET:
            field_dict["submittedBy"] = submitted_by
        if delete_mode is not UNSET:
            field_dict["deleteMode"] = delete_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.records_change_request_body_fields import RecordsChangeRequestBodyFields

        d = dict(src_dict)

        def _parse_operation(data: object) -> Literal["delete", "restore", "update"]:
            operation_type_0 = cast(Literal["update"], data)
            if operation_type_0 != "update":
                raise ValueError(f"operation_type_0 must match const 'update', got '{operation_type_0}'")
            return operation_type_0
            operation_type_1 = cast(Literal["delete"], data)
            if operation_type_1 != "delete":
                raise ValueError(f"operation_type_1 must match const 'delete', got '{operation_type_1}'")
            return operation_type_1
            operation_type_2 = cast(Literal["restore"], data)
            if operation_type_2 != "restore":
                raise ValueError(f"operation_type_2 must match const 'restore', got '{operation_type_2}'")
            return operation_type_2

        operation = _parse_operation(d.pop("operation"))

        _fields = d.pop("fields", UNSET)
        fields: RecordsChangeRequestBodyFields | Unset
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = RecordsChangeRequestBodyFields.from_dict(_fields)

        def _parse_message(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        author = d.pop("author", UNSET)

        base_commit_id = d.pop("baseCommitId", UNSET)

        def _parse_auto_merge(data: object) -> bool | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset, data)

        auto_merge = _parse_auto_merge(d.pop("autoMerge", UNSET))

        def _parse_submitted_by(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        submitted_by = _parse_submitted_by(d.pop("submittedBy", UNSET))

        _delete_mode = d.pop("deleteMode", UNSET)
        delete_mode: RecordsChangeRequestBodyDeleteMode | Unset
        if isinstance(_delete_mode, Unset):
            delete_mode = UNSET
        else:
            delete_mode = check_records_change_request_body_delete_mode(_delete_mode)

        records_change_request_body = cls(
            operation=operation,
            fields=fields,
            message=message,
            author=author,
            base_commit_id=base_commit_id,
            auto_merge=auto_merge,
            submitted_by=submitted_by,
            delete_mode=delete_mode,
        )

        records_change_request_body.additional_properties = d
        return records_change_request_body

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
