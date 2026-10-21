from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operation_delete_mode import OperationDeleteMode, check_operation_delete_mode
from ..models.operation_operation import OperationOperation, check_operation_operation
from ..models.operation_status import OperationStatus, check_operation_status
from ..models.operation_target_type import OperationTargetType, check_operation_target_type

if TYPE_CHECKING:
    from ..models.commit import Commit
    from ..models.operation_base_fields_type_0 import OperationBaseFieldsType0


T = TypeVar("T", bound="Operation")


@_attrs_define
class Operation:
    """
    Attributes:
        id (str):
        change_request_id (str):
        base_id (None | str):
        target_type (OperationTargetType):
        node_id (None | str):
        operation (OperationOperation):
        status (OperationStatus):
        target_record_id (None | str):
        target_view_id (None | str):
        file_path (None | str):
        source_record_id (None | str):
        source_commit_id (None | str):
        base_commit_id (None | str):
        head_commit_id (str):
        delete_mode (OperationDeleteMode):
        merged_record_id (None | str):
        merged_view_id (None | str):
        position (float):
        created_at (str):
        updated_at (str):
        head_commit (Commit):
        base_fields (None | OperationBaseFieldsType0):
    """

    id: str
    change_request_id: str
    base_id: None | str
    target_type: OperationTargetType
    node_id: None | str
    operation: OperationOperation
    status: OperationStatus
    target_record_id: None | str
    target_view_id: None | str
    file_path: None | str
    source_record_id: None | str
    source_commit_id: None | str
    base_commit_id: None | str
    head_commit_id: str
    delete_mode: OperationDeleteMode
    merged_record_id: None | str
    merged_view_id: None | str
    position: float
    created_at: str
    updated_at: str
    head_commit: Commit
    base_fields: None | OperationBaseFieldsType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.operation_base_fields_type_0 import OperationBaseFieldsType0

        id = self.id

        change_request_id = self.change_request_id

        base_id: None | str
        base_id = self.base_id

        target_type: str = self.target_type

        node_id: None | str
        node_id = self.node_id

        operation: str = self.operation

        status: str = self.status

        target_record_id: None | str
        target_record_id = self.target_record_id

        target_view_id: None | str
        target_view_id = self.target_view_id

        file_path: None | str
        file_path = self.file_path

        source_record_id: None | str
        source_record_id = self.source_record_id

        source_commit_id: None | str
        source_commit_id = self.source_commit_id

        base_commit_id: None | str
        base_commit_id = self.base_commit_id

        head_commit_id = self.head_commit_id

        delete_mode: str = self.delete_mode

        merged_record_id: None | str
        merged_record_id = self.merged_record_id

        merged_view_id: None | str
        merged_view_id = self.merged_view_id

        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        head_commit = self.head_commit.to_dict()

        base_fields: dict[str, Any] | None
        if isinstance(self.base_fields, OperationBaseFieldsType0):
            base_fields = self.base_fields.to_dict()
        else:
            base_fields = self.base_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "changeRequestId": change_request_id,
                "baseId": base_id,
                "targetType": target_type,
                "nodeId": node_id,
                "operation": operation,
                "status": status,
                "targetRecordId": target_record_id,
                "targetViewId": target_view_id,
                "filePath": file_path,
                "sourceRecordId": source_record_id,
                "sourceCommitId": source_commit_id,
                "baseCommitId": base_commit_id,
                "headCommitId": head_commit_id,
                "deleteMode": delete_mode,
                "mergedRecordId": merged_record_id,
                "mergedViewId": merged_view_id,
                "position": position,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "headCommit": head_commit,
                "baseFields": base_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.commit import Commit
        from ..models.operation_base_fields_type_0 import OperationBaseFieldsType0

        d = dict(src_dict)
        id = d.pop("id")

        change_request_id = d.pop("changeRequestId")

        def _parse_base_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        base_id = _parse_base_id(d.pop("baseId"))

        target_type = check_operation_target_type(d.pop("targetType"))

        def _parse_node_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        node_id = _parse_node_id(d.pop("nodeId"))

        operation = check_operation_operation(d.pop("operation"))

        status = check_operation_status(d.pop("status"))

        def _parse_target_record_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_record_id = _parse_target_record_id(d.pop("targetRecordId"))

        def _parse_target_view_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_view_id = _parse_target_view_id(d.pop("targetViewId"))

        def _parse_file_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_path = _parse_file_path(d.pop("filePath"))

        def _parse_source_record_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_record_id = _parse_source_record_id(d.pop("sourceRecordId"))

        def _parse_source_commit_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_commit_id = _parse_source_commit_id(d.pop("sourceCommitId"))

        def _parse_base_commit_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        base_commit_id = _parse_base_commit_id(d.pop("baseCommitId"))

        head_commit_id = d.pop("headCommitId")

        delete_mode = check_operation_delete_mode(d.pop("deleteMode"))

        def _parse_merged_record_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        merged_record_id = _parse_merged_record_id(d.pop("mergedRecordId"))

        def _parse_merged_view_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        merged_view_id = _parse_merged_view_id(d.pop("mergedViewId"))

        position = d.pop("position")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        head_commit = Commit.from_dict(d.pop("headCommit"))

        def _parse_base_fields(data: object) -> None | OperationBaseFieldsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                base_fields_type_0 = OperationBaseFieldsType0.from_dict(data)

                return base_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperationBaseFieldsType0, data)

        base_fields = _parse_base_fields(d.pop("baseFields"))

        operation = cls(
            id=id,
            change_request_id=change_request_id,
            base_id=base_id,
            target_type=target_type,
            node_id=node_id,
            operation=operation,
            status=status,
            target_record_id=target_record_id,
            target_view_id=target_view_id,
            file_path=file_path,
            source_record_id=source_record_id,
            source_commit_id=source_commit_id,
            base_commit_id=base_commit_id,
            head_commit_id=head_commit_id,
            delete_mode=delete_mode,
            merged_record_id=merged_record_id,
            merged_view_id=merged_view_id,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            head_commit=head_commit,
            base_fields=base_fields,
        )

        operation.additional_properties = d
        return operation

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
