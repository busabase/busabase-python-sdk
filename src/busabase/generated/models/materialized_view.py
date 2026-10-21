from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.materialized_view_status import MaterializedViewStatus, check_materialized_view_status
from ..models.materialized_view_type import MaterializedViewType, check_materialized_view_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_ref import UserRef
    from ..models.view_config import ViewConfig


T = TypeVar("T", bound="MaterializedView")


@_attrs_define
class MaterializedView:
    """
    Attributes:
        id (str):
        base_id (str):
        slug (str):
        name (str):
        description (str):
        type_ (MaterializedViewType):
        config (ViewConfig):
        status (MaterializedViewStatus):
        position (int):
        created_by (str):
        archived_at (None | str):
        created_at (str):
        updated_at (str):
        materialized (Literal[True]):
        created_by_user (None | Unset | UserRef):
    """

    id: str
    base_id: str
    slug: str
    name: str
    description: str
    type_: MaterializedViewType
    config: ViewConfig
    status: MaterializedViewStatus
    position: int
    created_by: str
    archived_at: None | str
    created_at: str
    updated_at: str
    materialized: Literal[True]
    created_by_user: None | Unset | UserRef = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_ref import UserRef

        id = self.id

        base_id = self.base_id

        slug = self.slug

        name = self.name

        description = self.description

        type_: str = self.type_

        config = self.config.to_dict()

        status: str = self.status

        position = self.position

        created_by = self.created_by

        archived_at: None | str
        archived_at = self.archived_at

        created_at = self.created_at

        updated_at = self.updated_at

        materialized = self.materialized

        created_by_user: dict[str, Any] | None | Unset
        if isinstance(self.created_by_user, Unset):
            created_by_user = UNSET
        elif isinstance(self.created_by_user, UserRef):
            created_by_user = self.created_by_user.to_dict()
        else:
            created_by_user = self.created_by_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "baseId": base_id,
                "slug": slug,
                "name": name,
                "description": description,
                "type": type_,
                "config": config,
                "status": status,
                "position": position,
                "createdBy": created_by,
                "archivedAt": archived_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "materialized": materialized,
            }
        )
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.user_ref import UserRef
        from ..models.view_config import ViewConfig

        d = dict(src_dict)
        id = d.pop("id")

        base_id = d.pop("baseId")

        slug = d.pop("slug")

        name = d.pop("name")

        description = d.pop("description")

        type_ = check_materialized_view_type(d.pop("type"))

        config = ViewConfig.from_dict(d.pop("config"))

        status = check_materialized_view_status(d.pop("status"))

        position = d.pop("position")

        created_by = d.pop("createdBy")

        def _parse_archived_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        archived_at = _parse_archived_at(d.pop("archivedAt"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

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

        materialized_view = cls(
            id=id,
            base_id=base_id,
            slug=slug,
            name=name,
            description=description,
            type_=type_,
            config=config,
            status=status,
            position=position,
            created_by=created_by,
            archived_at=archived_at,
            created_at=created_at,
            updated_at=updated_at,
            materialized=materialized,
            created_by_user=created_by_user,
        )

        materialized_view.additional_properties = d
        return materialized_view

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
