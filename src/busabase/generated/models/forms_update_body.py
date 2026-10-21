from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.forms_update_body_bindings_item import FormsUpdateBodyBindingsItem
    from ..models.forms_update_body_page import FormsUpdateBodyPage
    from ..models.forms_update_body_share import FormsUpdateBodyShare


T = TypeVar("T", bound="FormsUpdateBody")


@_attrs_define
class FormsUpdateBody:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        bindings (list[FormsUpdateBodyBindingsItem] | Unset):
        page (FormsUpdateBodyPage | Unset):
        share (FormsUpdateBodyShare | Unset):
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    bindings: list[FormsUpdateBodyBindingsItem] | Unset = UNSET
    page: FormsUpdateBodyPage | Unset = UNSET
    share: FormsUpdateBodyShare | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        bindings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bindings, Unset):
            bindings = []
            for bindings_item_data in self.bindings:
                bindings_item = bindings_item_data.to_dict()
                bindings.append(bindings_item)

        page: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page, Unset):
            page = self.page.to_dict()

        share: dict[str, Any] | Unset = UNSET
        if not isinstance(self.share, Unset):
            share = self.share.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if bindings is not UNSET:
            field_dict["bindings"] = bindings
        if page is not UNSET:
            field_dict["page"] = page
        if share is not UNSET:
            field_dict["share"] = share

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.forms_update_body_bindings_item import FormsUpdateBodyBindingsItem
        from ..models.forms_update_body_page import FormsUpdateBodyPage
        from ..models.forms_update_body_share import FormsUpdateBodyShare

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _bindings = d.pop("bindings", UNSET)
        bindings: list[FormsUpdateBodyBindingsItem] | Unset = UNSET
        if _bindings is not UNSET:
            bindings = []
            for bindings_item_data in _bindings:
                bindings_item = FormsUpdateBodyBindingsItem.from_dict(bindings_item_data)

                bindings.append(bindings_item)

        _page = d.pop("page", UNSET)
        page: FormsUpdateBodyPage | Unset
        if isinstance(_page, Unset):
            page = UNSET
        else:
            page = FormsUpdateBodyPage.from_dict(_page)

        _share = d.pop("share", UNSET)
        share: FormsUpdateBodyShare | Unset
        if isinstance(_share, Unset):
            share = UNSET
        else:
            share = FormsUpdateBodyShare.from_dict(_share)

        forms_update_body = cls(
            name=name,
            description=description,
            bindings=bindings,
            page=page,
            share=share,
        )

        forms_update_body.additional_properties = d
        return forms_update_body

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
