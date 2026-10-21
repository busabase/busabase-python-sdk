from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_node_operation_fields_item_type import (
    CreateNodeOperationFieldsItemType,
    check_create_node_operation_fields_item_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_options import FieldOptions
    from ..models.localized_field_name import LocalizedFieldName


T = TypeVar("T", bound="CreateNodeOperationFieldsItem")


@_attrs_define
class CreateNodeOperationFieldsItem:
    """
    Attributes:
        slug (str):
        name (LocalizedFieldName | str):
        type_ (CreateNodeOperationFieldsItemType | Unset):  Default: 'text'.
        required (bool | Unset):  Default: False.
        options (FieldOptions | Unset):
    """

    slug: str
    name: LocalizedFieldName | str
    type_: CreateNodeOperationFieldsItemType | Unset = "text"
    required: bool | Unset = False
    options: FieldOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_field_name import LocalizedFieldName

        slug = self.slug

        name: dict[str, Any] | str
        if isinstance(self.name, LocalizedFieldName):
            name = self.name.to_dict()
        else:
            name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        required = self.required

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if required is not UNSET:
            field_dict["required"] = required
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.field_options import FieldOptions
        from ..models.localized_field_name import LocalizedFieldName

        d = dict(src_dict)
        slug = d.pop("slug")

        def _parse_name(data: object) -> LocalizedFieldName | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_type_1 = LocalizedFieldName.from_dict(data)

                return name_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedFieldName | str, data)

        name = _parse_name(d.pop("name"))

        _type_ = d.pop("type", UNSET)
        type_: CreateNodeOperationFieldsItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_create_node_operation_fields_item_type(_type_)

        required = d.pop("required", UNSET)

        _options = d.pop("options", UNSET)
        options: FieldOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = FieldOptions.from_dict(_options)

        create_node_operation_fields_item = cls(
            slug=slug,
            name=name,
            type_=type_,
            required=required,
            options=options,
        )

        create_node_operation_fields_item.additional_properties = d
        return create_node_operation_fields_item

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
