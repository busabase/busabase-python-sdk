from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.commit_operation import CommitOperation, check_commit_operation
from ..models.commit_target_type import CommitTargetType, check_commit_target_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_payload import CommitPayload
    from ..models.user_ref import UserRef


T = TypeVar("T", bound="Commit")


@_attrs_define
class Commit:
    """
    Attributes:
        id (str):
        base_id (None | str):
        target_type (CommitTargetType):
        node_id (None | str):
        operation_id (None | str):
        parent_commit_id (None | str):
        payload (CommitPayload):
        operation (CommitOperation):
        message (str):
        author (str):
        created_at (str):
        author_user (None | Unset | UserRef):
    """

    id: str
    base_id: None | str
    target_type: CommitTargetType
    node_id: None | str
    operation_id: None | str
    parent_commit_id: None | str
    payload: CommitPayload
    operation: CommitOperation
    message: str
    author: str
    created_at: str
    author_user: None | Unset | UserRef = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_ref import UserRef

        id = self.id

        base_id: None | str
        base_id = self.base_id

        target_type: str = self.target_type

        node_id: None | str
        node_id = self.node_id

        operation_id: None | str
        operation_id = self.operation_id

        parent_commit_id: None | str
        parent_commit_id = self.parent_commit_id

        payload = self.payload.to_dict()

        operation: str = self.operation

        message = self.message

        author = self.author

        created_at = self.created_at

        author_user: dict[str, Any] | None | Unset
        if isinstance(self.author_user, Unset):
            author_user = UNSET
        elif isinstance(self.author_user, UserRef):
            author_user = self.author_user.to_dict()
        else:
            author_user = self.author_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "baseId": base_id,
                "targetType": target_type,
                "nodeId": node_id,
                "operationId": operation_id,
                "parentCommitId": parent_commit_id,
                "payload": payload,
                "operation": operation,
                "message": message,
                "author": author,
                "createdAt": created_at,
            }
        )
        if author_user is not UNSET:
            field_dict["authorUser"] = author_user

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.commit_payload import CommitPayload
        from ..models.user_ref import UserRef

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_base_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        base_id = _parse_base_id(d.pop("baseId"))

        target_type = check_commit_target_type(d.pop("targetType"))

        def _parse_node_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        node_id = _parse_node_id(d.pop("nodeId"))

        def _parse_operation_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        operation_id = _parse_operation_id(d.pop("operationId"))

        def _parse_parent_commit_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_commit_id = _parse_parent_commit_id(d.pop("parentCommitId"))

        payload = CommitPayload.from_dict(d.pop("payload"))

        operation = check_commit_operation(d.pop("operation"))

        message = d.pop("message")

        author = d.pop("author")

        created_at = d.pop("createdAt")

        def _parse_author_user(data: object) -> None | Unset | UserRef:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_user_type_0 = UserRef.from_dict(data)

                return author_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserRef, data)

        author_user = _parse_author_user(d.pop("authorUser", UNSET))

        commit = cls(
            id=id,
            base_id=base_id,
            target_type=target_type,
            node_id=node_id,
            operation_id=operation_id,
            parent_commit_id=parent_commit_id,
            payload=payload,
            operation=operation,
            message=message,
            author=author,
            created_at=created_at,
            author_user=author_user,
        )

        commit.additional_properties = d
        return commit

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
