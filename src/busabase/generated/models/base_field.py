from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.base_field_type import BaseFieldType, check_base_field_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_field_name_type_1 import BaseFieldNameType1
    from ..models.field_options import FieldOptions


T = TypeVar("T", bound="BaseField")


@_attrs_define
class BaseField:
    """
    Attributes:
        id (str):
        base_id (str):
        slug (str):
        name (BaseFieldNameType1 | str):
        type_ (BaseFieldType):
        required (bool):
        position (float):
        options (FieldOptions | Unset):
    """

    id: str
    base_id: str
    slug: str
    name: BaseFieldNameType1 | str
    type_: BaseFieldType
    required: bool
    position: float
    options: FieldOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_field_name_type_1 import BaseFieldNameType1

        id = self.id

        base_id = self.base_id

        slug = self.slug

        name: dict[str, Any] | str
        if isinstance(self.name, BaseFieldNameType1):
            name = self.name.to_dict()
        else:
            name = self.name

        type_: str = self.type_

        required = self.required

        position = self.position

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "baseId": base_id,
                "slug": slug,
                "name": name,
                "type": type_,
                "required": required,
                "position": position,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.base_field_name_type_1 import BaseFieldNameType1
        from ..models.field_options import FieldOptions

        d = dict(src_dict)
        id = d.pop("id")

        base_id = d.pop("baseId")

        slug = d.pop("slug")

        def _parse_name(data: object) -> BaseFieldNameType1 | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_type_1 = BaseFieldNameType1.from_dict(data)

                return name_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseFieldNameType1 | str, data)

        name = _parse_name(d.pop("name"))

        type_ = check_base_field_type(d.pop("type"))

        required = d.pop("required")

        position = d.pop("position")

        _options = d.pop("options", UNSET)
        options: FieldOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = FieldOptions.from_dict(_options)

        base_field = cls(
            id=id,
            base_id=base_id,
            slug=slug,
            name=name,
            type_=type_,
            required=required,
            position=position,
            options=options,
        )

        base_field.additional_properties = d
        return base_field

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
