from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bases_create_field_body_type import BasesCreateFieldBodyType, check_bases_create_field_body_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_options import FieldOptions
    from ..models.localized_field_name import LocalizedFieldName


T = TypeVar("T", bound="BasesCreateFieldBody")


@_attrs_define
class BasesCreateFieldBody:
    """
    Attributes:
        name (LocalizedFieldName | str):
        slug (str):
        type_ (BasesCreateFieldBodyType | Unset):  Default: 'text'.
        required (bool | Unset):  Default: False.
        options (FieldOptions | Unset):
    """

    name: LocalizedFieldName | str
    slug: str
    type_: BasesCreateFieldBodyType | Unset = "text"
    required: bool | Unset = False
    options: FieldOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_field_name import LocalizedFieldName

        name: dict[str, Any] | str
        if isinstance(self.name, LocalizedFieldName):
            name = self.name.to_dict()
        else:
            name = self.name

        slug = self.slug

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
                "name": name,
                "slug": slug,
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

        slug = d.pop("slug")

        _type_ = d.pop("type", UNSET)
        type_: BasesCreateFieldBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_bases_create_field_body_type(_type_)

        required = d.pop("required", UNSET)

        _options = d.pop("options", UNSET)
        options: FieldOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = FieldOptions.from_dict(_options)

        bases_create_field_body = cls(
            name=name,
            slug=slug,
            type_=type_,
            required=required,
            options=options,
        )

        bases_create_field_body.additional_properties = d
        return bases_create_field_body

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
