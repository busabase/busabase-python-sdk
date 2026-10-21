from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_bound_fields_item_type import FormBoundFieldsItemType, check_form_bound_fields_item_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_bound_fields_item_choices_item import FormBoundFieldsItemChoicesItem
    from ..models.form_bound_fields_item_date import FormBoundFieldsItemDate
    from ..models.form_bound_fields_item_help import FormBoundFieldsItemHelp
    from ..models.form_bound_fields_item_name_type_1 import FormBoundFieldsItemNameType1


T = TypeVar("T", bound="FormBoundFieldsItem")


@_attrs_define
class FormBoundFieldsItem:
    """
    Attributes:
        slug (str):
        name (FormBoundFieldsItemNameType1 | str):
        type_ (FormBoundFieldsItemType):
        help_ (FormBoundFieldsItemHelp | Unset):
        choices (list[FormBoundFieldsItemChoicesItem] | Unset):
        date (FormBoundFieldsItemDate | Unset):
    """

    slug: str
    name: FormBoundFieldsItemNameType1 | str
    type_: FormBoundFieldsItemType
    help_: FormBoundFieldsItemHelp | Unset = UNSET
    choices: list[FormBoundFieldsItemChoicesItem] | Unset = UNSET
    date: FormBoundFieldsItemDate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.form_bound_fields_item_name_type_1 import FormBoundFieldsItemNameType1

        slug = self.slug

        name: dict[str, Any] | str
        if isinstance(self.name, FormBoundFieldsItemNameType1):
            name = self.name.to_dict()
        else:
            name = self.name

        type_: str = self.type_

        help_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.help_, Unset):
            help_ = self.help_.to_dict()

        choices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.choices, Unset):
            choices = []
            for choices_item_data in self.choices:
                choices_item = choices_item_data.to_dict()
                choices.append(choices_item)

        date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "name": name,
                "type": type_,
            }
        )
        if help_ is not UNSET:
            field_dict["help"] = help_
        if choices is not UNSET:
            field_dict["choices"] = choices
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.form_bound_fields_item_choices_item import FormBoundFieldsItemChoicesItem
        from ..models.form_bound_fields_item_date import FormBoundFieldsItemDate
        from ..models.form_bound_fields_item_help import FormBoundFieldsItemHelp
        from ..models.form_bound_fields_item_name_type_1 import FormBoundFieldsItemNameType1

        d = dict(src_dict)
        slug = d.pop("slug")

        def _parse_name(data: object) -> FormBoundFieldsItemNameType1 | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_type_1 = FormBoundFieldsItemNameType1.from_dict(data)

                return name_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormBoundFieldsItemNameType1 | str, data)

        name = _parse_name(d.pop("name"))

        type_ = check_form_bound_fields_item_type(d.pop("type"))

        _help_ = d.pop("help", UNSET)
        help_: FormBoundFieldsItemHelp | Unset
        if isinstance(_help_, Unset):
            help_ = UNSET
        else:
            help_ = FormBoundFieldsItemHelp.from_dict(_help_)

        _choices = d.pop("choices", UNSET)
        choices: list[FormBoundFieldsItemChoicesItem] | Unset = UNSET
        if _choices is not UNSET:
            choices = []
            for choices_item_data in _choices:
                choices_item = FormBoundFieldsItemChoicesItem.from_dict(choices_item_data)

                choices.append(choices_item)

        _date = d.pop("date", UNSET)
        date: FormBoundFieldsItemDate | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = FormBoundFieldsItemDate.from_dict(_date)

        form_bound_fields_item = cls(
            slug=slug,
            name=name,
            type_=type_,
            help_=help_,
            choices=choices,
            date=date,
        )

        form_bound_fields_item.additional_properties = d
        return form_bound_fields_item

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
