from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.materialized_record_status import MaterializedRecordStatus, check_materialized_record_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base import Base
    from ..models.commit import Commit
    from ..models.materialized_record_field_users import MaterializedRecordFieldUsers
    from ..models.user_ref import UserRef


T = TypeVar("T", bound="MaterializedRecord")


@_attrs_define
class MaterializedRecord:
    """
    Attributes:
        id (str):
        base_id (str):
        head_commit_id (str):
        parent_record_id (None | str):
        parent_commit_id (None | str):
        status (MaterializedRecordStatus):
        created_by (str):
        archived_at (None | str):
        created_at (str):
        updated_at (str):
        base (Base):
        head_commit (Commit):
        materialized (Literal[True]):
        created_by_user (None | Unset | UserRef):
        field_users (MaterializedRecordFieldUsers | Unset):
    """

    id: str
    base_id: str
    head_commit_id: str
    parent_record_id: None | str
    parent_commit_id: None | str
    status: MaterializedRecordStatus
    created_by: str
    archived_at: None | str
    created_at: str
    updated_at: str
    base: Base
    head_commit: Commit
    materialized: Literal[True]
    created_by_user: None | Unset | UserRef = UNSET
    field_users: MaterializedRecordFieldUsers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_ref import UserRef

        id = self.id

        base_id = self.base_id

        head_commit_id = self.head_commit_id

        parent_record_id: None | str
        parent_record_id = self.parent_record_id

        parent_commit_id: None | str
        parent_commit_id = self.parent_commit_id

        status: str = self.status

        created_by = self.created_by

        archived_at: None | str
        archived_at = self.archived_at

        created_at = self.created_at

        updated_at = self.updated_at

        base = self.base.to_dict()

        head_commit = self.head_commit.to_dict()

        materialized = self.materialized

        created_by_user: dict[str, Any] | None | Unset
        if isinstance(self.created_by_user, Unset):
            created_by_user = UNSET
        elif isinstance(self.created_by_user, UserRef):
            created_by_user = self.created_by_user.to_dict()
        else:
            created_by_user = self.created_by_user

        field_users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_users, Unset):
            field_users = self.field_users.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "baseId": base_id,
                "headCommitId": head_commit_id,
                "parentRecordId": parent_record_id,
                "parentCommitId": parent_commit_id,
                "status": status,
                "createdBy": created_by,
                "archivedAt": archived_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "base": base,
                "headCommit": head_commit,
                "materialized": materialized,
            }
        )
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if field_users is not UNSET:
            field_dict["fieldUsers"] = field_users

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.base import Base
        from ..models.commit import Commit
        from ..models.materialized_record_field_users import MaterializedRecordFieldUsers
        from ..models.user_ref import UserRef

        d = dict(src_dict)
        id = d.pop("id")

        base_id = d.pop("baseId")

        head_commit_id = d.pop("headCommitId")

        def _parse_parent_record_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_record_id = _parse_parent_record_id(d.pop("parentRecordId"))

        def _parse_parent_commit_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_commit_id = _parse_parent_commit_id(d.pop("parentCommitId"))

        status = check_materialized_record_status(d.pop("status"))

        created_by = d.pop("createdBy")

        def _parse_archived_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        archived_at = _parse_archived_at(d.pop("archivedAt"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        base = Base.from_dict(d.pop("base"))

        head_commit = Commit.from_dict(d.pop("headCommit"))

        materialized = cast(Literal[True], d.pop("materialized"))
        if materialized != True:
            raise ValueError(f"materialized must match const True, got '{materialized}'")

        def _parse_created_by_user(data: object) -> None | Unset | UserRef:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_user_type_0 = UserRef.from_dict(data)

                return created_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserRef, data)

        created_by_user = _parse_created_by_user(d.pop("createdByUser", UNSET))

        _field_users = d.pop("fieldUsers", UNSET)
        field_users: MaterializedRecordFieldUsers | Unset
        if isinstance(_field_users, Unset):
            field_users = UNSET
        else:
            field_users = MaterializedRecordFieldUsers.from_dict(_field_users)

        materialized_record = cls(
            id=id,
            base_id=base_id,
            head_commit_id=head_commit_id,
            parent_record_id=parent_record_id,
            parent_commit_id=parent_commit_id,
            status=status,
            created_by=created_by,
            archived_at=archived_at,
            created_at=created_at,
            updated_at=updated_at,
            base=base,
            head_commit=head_commit,
            materialized=materialized,
            created_by_user=created_by_user,
            field_users=field_users,
        )

        materialized_record.additional_properties = d
        return materialized_record

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
