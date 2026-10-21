from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nodes_create_change_request_body_operations_item_type_0_fields_item_type import (
    NodesCreateChangeRequestBodyOperationsItemType0FieldsItemType,
    check_nodes_create_change_request_body_operations_item_type_0_fields_item_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_options import FieldOptions
    from ..models.nodes_create_change_request_body_operations_item_type_0_fields_item_name_type_1 import (
        NodesCreateChangeRequestBodyOperationsItemType0FieldsItemNameType1,
    )


T = TypeVar("T", bound="NodesCreateChangeRequestBodyOperationsItemType0FieldsItem")


@_attrs_define
class NodesCreateChangeRequestBodyOperationsItemType0FieldsItem:
    """
    Attributes:
        slug (str):
        name (NodesCreateChangeRequestBodyOperationsItemType0FieldsItemNameType1 | str):
        type_ (NodesCreateChangeRequestBodyOperationsItemType0FieldsItemType | Unset):  Default: 'text'.
        required (bool | Unset):  Default: False.
        options (FieldOptions | Unset):
    """

    slug: str
    name: NodesCreateChangeRequestBodyOperationsItemType0FieldsItemNameType1 | str
    type_: NodesCreateChangeRequestBodyOperationsItemType0FieldsItemType | Unset = "text"
    required: bool | Unset = False
    options: FieldOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nodes_create_change_request_body_operations_item_type_0_fields_item_name_type_1 import (
            NodesCreateChangeRequestBodyOperationsItemType0FieldsItemNameType1,
        )

        slug = self.slug

        name: dict[str, Any] | str
        if isinstance(self.name, NodesCreateChangeRequestBodyOperationsItemType0FieldsItemNameType1):
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
        from ..models.nodes_create_change_request_body_operations_item_type_0_fields_item_name_type_1 import (
            NodesCreateChangeRequestBodyOperationsItemType0FieldsItemNameType1,
        )

        d = dict(src_dict)
        slug = d.pop("slug")

        def _parse_name(data: object) -> NodesCreateChangeRequestBodyOperationsItemType0FieldsItemNameType1 | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_type_1 = NodesCreateChangeRequestBodyOperationsItemType0FieldsItemNameType1.from_dict(data)

                return name_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NodesCreateChangeRequestBodyOperationsItemType0FieldsItemNameType1 | str, data)

        name = _parse_name(d.pop("name"))

        _type_ = d.pop("type", UNSET)
        type_: NodesCreateChangeRequestBodyOperationsItemType0FieldsItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_nodes_create_change_request_body_operations_item_type_0_fields_item_type(_type_)

        required = d.pop("required", UNSET)

        _options = d.pop("options", UNSET)
        options: FieldOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = FieldOptions.from_dict(_options)

        nodes_create_change_request_body_operations_item_type_0_fields_item = cls(
            slug=slug,
            name=name,
            type_=type_,
            required=required,
            options=options,
        )

        nodes_create_change_request_body_operations_item_type_0_fields_item.additional_properties = d
        return nodes_create_change_request_body_operations_item_type_0_fields_item

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
