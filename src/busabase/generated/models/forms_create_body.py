from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_field_binding import FormFieldBinding
    from ..models.form_page import FormPage
    from ..models.form_share import FormShare


T = TypeVar("T", bound="FormsCreateBody")


@_attrs_define
class FormsCreateBody:
    """
    Attributes:
        node_id (str):
        target_base_id (str):
        name (str):
        description (str | Unset):  Default: ''.
        bindings (list[FormFieldBinding] | Unset):
        page (FormPage | Unset):
        share (FormShare | Unset):
    """

    node_id: str
    target_base_id: str
    name: str
    description: str | Unset = ""
    bindings: list[FormFieldBinding] | Unset = UNSET
    page: FormPage | Unset = UNSET
    share: FormShare | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        target_base_id = self.target_base_id

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
        field_dict.update(
            {
                "nodeId": node_id,
                "targetBaseId": target_base_id,
                "name": name,
            }
        )
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
        from ..models.form_field_binding import FormFieldBinding
        from ..models.form_page import FormPage
        from ..models.form_share import FormShare

        d = dict(src_dict)
        node_id = d.pop("nodeId")

        target_base_id = d.pop("targetBaseId")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        _bindings = d.pop("bindings", UNSET)
        bindings: list[FormFieldBinding] | Unset = UNSET
        if _bindings is not UNSET:
            bindings = []
            for bindings_item_data in _bindings:
                bindings_item = FormFieldBinding.from_dict(bindings_item_data)

                bindings.append(bindings_item)

        _page = d.pop("page", UNSET)
        page: FormPage | Unset
        if isinstance(_page, Unset):
            page = UNSET
        else:
            page = FormPage.from_dict(_page)

        _share = d.pop("share", UNSET)
        share: FormShare | Unset
        if isinstance(_share, Unset):
            share = UNSET
        else:
            share = FormShare.from_dict(_share)

        forms_create_body = cls(
            node_id=node_id,
            target_base_id=target_base_id,
            name=name,
            description=description,
            bindings=bindings,
            page=page,
            share=share,
        )

        forms_create_body.additional_properties = d
        return forms_create_body

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
