from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_node_operation import CreateNodeOperation
    from ..models.delete_node_operation import DeleteNodeOperation
    from ..models.move_node_operation import MoveNodeOperation
    from ..models.rename_node_operation import RenameNodeOperation
    from ..models.restore_node_operation import RestoreNodeOperation


T = TypeVar("T", bound="NodesCreateChangeRequestBody")


@_attrs_define
class NodesCreateChangeRequestBody:
    """
    Attributes:
        operations (list[CreateNodeOperation | DeleteNodeOperation | MoveNodeOperation | RenameNodeOperation |
            RestoreNodeOperation]):
        message (str | Unset): Explanation shown to the human reviewer. Write a conventional-commit style subject —
            imperative verb + what + why, e.g. "Reorganize marketing docs under a Campaigns folder". Default: 'Update node
            tree'.
        submitted_by (str | Unset):  Default: 'local-producer'.
        auto_merge (bool | Unset): Whether to approve and merge this structural node change immediately. Omitted
            defaults to merging immediately if the actor has write access on every target node, otherwise falling back to a
            pending Change Request; pass explicit false to force review even with write access.
    """

    operations: list[
        CreateNodeOperation | DeleteNodeOperation | MoveNodeOperation | RenameNodeOperation | RestoreNodeOperation
    ]
    message: str | Unset = "Update node tree"
    submitted_by: str | Unset = "local-producer"
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_node_operation import CreateNodeOperation
        from ..models.delete_node_operation import DeleteNodeOperation
        from ..models.rename_node_operation import RenameNodeOperation
        from ..models.restore_node_operation import RestoreNodeOperation

        operations = []
        for operations_item_data in self.operations:
            operations_item: dict[str, Any]
            if (
                isinstance(operations_item_data, CreateNodeOperation)
                or isinstance(operations_item_data, RenameNodeOperation)
                or isinstance(operations_item_data, DeleteNodeOperation)
                or isinstance(operations_item_data, RestoreNodeOperation)
            ):
                operations_item = operations_item_data.to_dict()
            else:
                operations_item = operations_item_data.to_dict()

            operations.append(operations_item)

        message = self.message

        submitted_by = self.submitted_by

        auto_merge = self.auto_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operations": operations,
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
        from ..models.create_node_operation import CreateNodeOperation
        from ..models.delete_node_operation import DeleteNodeOperation
        from ..models.move_node_operation import MoveNodeOperation
        from ..models.rename_node_operation import RenameNodeOperation
        from ..models.restore_node_operation import RestoreNodeOperation

        d = dict(src_dict)
        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:

            def _parse_operations_item(
                data: object,
            ) -> (
                CreateNodeOperation
                | DeleteNodeOperation
                | MoveNodeOperation
                | RenameNodeOperation
                | RestoreNodeOperation
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_0 = CreateNodeOperation.from_dict(data)

                    return operations_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_1 = RenameNodeOperation.from_dict(data)

                    return operations_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_2 = DeleteNodeOperation.from_dict(data)

                    return operations_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_3 = RestoreNodeOperation.from_dict(data)

                    return operations_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                operations_item_type_4 = MoveNodeOperation.from_dict(data)

                return operations_item_type_4

            operations_item = _parse_operations_item(operations_item_data)

            operations.append(operations_item)

        message = d.pop("message", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        nodes_create_change_request_body = cls(
            operations=operations,
            message=message,
            submitted_by=submitted_by,
            auto_merge=auto_merge,
        )

        nodes_create_change_request_body.additional_properties = d
        return nodes_create_change_request_body

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
