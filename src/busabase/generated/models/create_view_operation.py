from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_view_operation_type import CreateViewOperationType, check_create_view_operation_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.view_config import ViewConfig


T = TypeVar("T", bound="CreateViewOperation")


@_attrs_define
class CreateViewOperation:
    """
    Attributes:
        name (str):
        operation (Literal['create']):
        base_id (str): Base the new view belongs to.
        config (ViewConfig | Unset):
        description (str | Unset):  Default: ''.
        message (str | Unset):  Default: 'Create view'.
        type_ (CreateViewOperationType | Unset):  Default: 'table'.
        slug (str | Unset):
        submitted_by (str | Unset):  Default: 'local-producer'.
        auto_merge (bool | Unset): Whether to approve and merge this view change immediately. Omitted defaults to
            merging immediately if the actor has write access on the Base's node, otherwise falling back to a pending Change
            Request; pass explicit false to force review even with write access.
    """

    name: str
    operation: Literal["create"]
    base_id: str
    config: ViewConfig | Unset = UNSET
    description: str | Unset = ""
    message: str | Unset = "Create view"
    type_: CreateViewOperationType | Unset = "table"
    slug: str | Unset = UNSET
    submitted_by: str | Unset = "local-producer"
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        operation = self.operation

        base_id = self.base_id

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        description = self.description

        message = self.message

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        slug = self.slug

        submitted_by = self.submitted_by

        auto_merge = self.auto_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "operation": operation,
                "baseId": base_id,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if description is not UNSET:
            field_dict["description"] = description
        if message is not UNSET:
            field_dict["message"] = message
        if type_ is not UNSET:
            field_dict["type"] = type_
        if slug is not UNSET:
            field_dict["slug"] = slug
        if submitted_by is not UNSET:
            field_dict["submittedBy"] = submitted_by
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.view_config import ViewConfig

        d = dict(src_dict)
        name = d.pop("name")

        operation = cast(Literal["create"], d.pop("operation"))
        if operation != "create":
            raise ValueError(f"operation must match const 'create', got '{operation}'")

        base_id = d.pop("baseId")

        _config = d.pop("config", UNSET)
        config: ViewConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ViewConfig.from_dict(_config)

        description = d.pop("description", UNSET)

        message = d.pop("message", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CreateViewOperationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_create_view_operation_type(_type_)

        slug = d.pop("slug", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        create_view_operation = cls(
            name=name,
            operation=operation,
            base_id=base_id,
            config=config,
            description=description,
            message=message,
            type_=type_,
            slug=slug,
            submitted_by=submitted_by,
            auto_merge=auto_merge,
        )

        create_view_operation.additional_properties = d
        return create_view_operation

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
