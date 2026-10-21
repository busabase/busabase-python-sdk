from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_trees_create_change_request_body_type import (
    FileTreesCreateChangeRequestBodyType,
    check_file_trees_create_change_request_body_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_trees_create_change_request_body_operations_item_type_0 import (
        FileTreesCreateChangeRequestBodyOperationsItemType0,
    )
    from ..models.file_trees_create_change_request_body_operations_item_type_1 import (
        FileTreesCreateChangeRequestBodyOperationsItemType1,
    )
    from ..models.file_trees_create_change_request_body_operations_item_type_2 import (
        FileTreesCreateChangeRequestBodyOperationsItemType2,
    )
    from ..models.file_trees_create_change_request_body_operations_item_type_3 import (
        FileTreesCreateChangeRequestBodyOperationsItemType3,
    )


T = TypeVar("T", bound="FileTreesCreateChangeRequestBody")


@_attrs_define
class FileTreesCreateChangeRequestBody:
    """
    Attributes:
        operations (list[FileTreesCreateChangeRequestBodyOperationsItemType0 |
            FileTreesCreateChangeRequestBodyOperationsItemType1 | FileTreesCreateChangeRequestBodyOperationsItemType2 |
            FileTreesCreateChangeRequestBodyOperationsItemType3]):
        message (str | Unset): Explanation shown to the human reviewer. Write a conventional-commit style subject —
            imperative verb + what + why, e.g. "Rewrite README.md quickstart for the new auth flow". Default: 'Update file
            tree'.
        submitted_by (str | Unset): Producer label for hosts with no authentication (the open-source single-user build).
            A host that authenticates the caller — Busabase Cloud — attributes the proposal to that account and ignores this
            value. Default: 'local-producer'.
        auto_merge (bool | Unset): Whether to approve and merge these file changes immediately. Omitted defaults to
            merging immediately if the actor has write access on the node, otherwise falling back to a pending Change
            Request; pass explicit false to force review even with write access. Applies to every operation kind, deletes
            included.
        type_ (FileTreesCreateChangeRequestBodyType | Unset): Disambiguates a slug. Unnecessary — and ignored — when
            `nodeId` is an id.
    """

    operations: list[
        FileTreesCreateChangeRequestBodyOperationsItemType0
        | FileTreesCreateChangeRequestBodyOperationsItemType1
        | FileTreesCreateChangeRequestBodyOperationsItemType2
        | FileTreesCreateChangeRequestBodyOperationsItemType3
    ]
    message: str | Unset = "Update file tree"
    submitted_by: str | Unset = "local-producer"
    auto_merge: bool | Unset = UNSET
    type_: FileTreesCreateChangeRequestBodyType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_trees_create_change_request_body_operations_item_type_0 import (
            FileTreesCreateChangeRequestBodyOperationsItemType0,
        )
        from ..models.file_trees_create_change_request_body_operations_item_type_1 import (
            FileTreesCreateChangeRequestBodyOperationsItemType1,
        )
        from ..models.file_trees_create_change_request_body_operations_item_type_2 import (
            FileTreesCreateChangeRequestBodyOperationsItemType2,
        )

        operations = []
        for operations_item_data in self.operations:
            operations_item: dict[str, Any]
            if (
                isinstance(operations_item_data, FileTreesCreateChangeRequestBodyOperationsItemType0)
                or isinstance(operations_item_data, FileTreesCreateChangeRequestBodyOperationsItemType1)
                or isinstance(operations_item_data, FileTreesCreateChangeRequestBodyOperationsItemType2)
            ):
                operations_item = operations_item_data.to_dict()
            else:
                operations_item = operations_item_data.to_dict()

            operations.append(operations_item)

        message = self.message

        submitted_by = self.submitted_by

        auto_merge = self.auto_merge

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

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
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.file_trees_create_change_request_body_operations_item_type_0 import (
            FileTreesCreateChangeRequestBodyOperationsItemType0,
        )
        from ..models.file_trees_create_change_request_body_operations_item_type_1 import (
            FileTreesCreateChangeRequestBodyOperationsItemType1,
        )
        from ..models.file_trees_create_change_request_body_operations_item_type_2 import (
            FileTreesCreateChangeRequestBodyOperationsItemType2,
        )
        from ..models.file_trees_create_change_request_body_operations_item_type_3 import (
            FileTreesCreateChangeRequestBodyOperationsItemType3,
        )

        d = dict(src_dict)
        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:

            def _parse_operations_item(
                data: object,
            ) -> (
                FileTreesCreateChangeRequestBodyOperationsItemType0
                | FileTreesCreateChangeRequestBodyOperationsItemType1
                | FileTreesCreateChangeRequestBodyOperationsItemType2
                | FileTreesCreateChangeRequestBodyOperationsItemType3
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_0 = FileTreesCreateChangeRequestBodyOperationsItemType0.from_dict(data)

                    return operations_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_1 = FileTreesCreateChangeRequestBodyOperationsItemType1.from_dict(data)

                    return operations_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_2 = FileTreesCreateChangeRequestBodyOperationsItemType2.from_dict(data)

                    return operations_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                operations_item_type_3 = FileTreesCreateChangeRequestBodyOperationsItemType3.from_dict(data)

                return operations_item_type_3

            operations_item = _parse_operations_item(operations_item_data)

            operations.append(operations_item)

        message = d.pop("message", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: FileTreesCreateChangeRequestBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_file_trees_create_change_request_body_type(_type_)

        file_trees_create_change_request_body = cls(
            operations=operations,
            message=message,
            submitted_by=submitted_by,
            auto_merge=auto_merge,
            type_=type_,
        )

        file_trees_create_change_request_body.additional_properties = d
        return file_trees_create_change_request_body

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
