from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_status import FormStatus, check_form_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_bound_fields_item import FormBoundFieldsItem
    from ..models.form_field_binding import FormFieldBinding
    from ..models.form_page import FormPage
    from ..models.form_share import FormShare


T = TypeVar("T", bound="Form")


@_attrs_define
class Form:
    """
    Attributes:
        id (str):
        node_id (str):
        space_id (str):
        target_base_id (str):
        name (str):
        description (str):
        bindings (list[FormFieldBinding]):
        page (FormPage):
        share (FormShare):
        status (FormStatus):
        created_by (str):
        created_at (str):
        updated_at (str):
        bound_fields (list[FormBoundFieldsItem] | Unset):
        submission_count (int | Unset):  Default: 0.
    """

    id: str
    node_id: str
    space_id: str
    target_base_id: str
    name: str
    description: str
    bindings: list[FormFieldBinding]
    page: FormPage
    share: FormShare
    status: FormStatus
    created_by: str
    created_at: str
    updated_at: str
    bound_fields: list[FormBoundFieldsItem] | Unset = UNSET
    submission_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        node_id = self.node_id

        space_id = self.space_id

        target_base_id = self.target_base_id

        name = self.name

        description = self.description

        bindings = []
        for bindings_item_data in self.bindings:
            bindings_item = bindings_item_data.to_dict()
            bindings.append(bindings_item)

        page = self.page.to_dict()

        share = self.share.to_dict()

        status: str = self.status

        created_by = self.created_by

        created_at = self.created_at

        updated_at = self.updated_at

        bound_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bound_fields, Unset):
            bound_fields = []
            for bound_fields_item_data in self.bound_fields:
                bound_fields_item = bound_fields_item_data.to_dict()
                bound_fields.append(bound_fields_item)

        submission_count = self.submission_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nodeId": node_id,
                "spaceId": space_id,
                "targetBaseId": target_base_id,
                "name": name,
                "description": description,
                "bindings": bindings,
                "page": page,
                "share": share,
                "status": status,
                "createdBy": created_by,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if bound_fields is not UNSET:
            field_dict["boundFields"] = bound_fields
        if submission_count is not UNSET:
            field_dict["submissionCount"] = submission_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.form_bound_fields_item import FormBoundFieldsItem
        from ..models.form_field_binding import FormFieldBinding
        from ..models.form_page import FormPage
        from ..models.form_share import FormShare

        d = dict(src_dict)
        id = d.pop("id")

        node_id = d.pop("nodeId")

        space_id = d.pop("spaceId")

        target_base_id = d.pop("targetBaseId")

        name = d.pop("name")

        description = d.pop("description")

        bindings = []
        _bindings = d.pop("bindings")
        for bindings_item_data in _bindings:
            bindings_item = FormFieldBinding.from_dict(bindings_item_data)

            bindings.append(bindings_item)

        page = FormPage.from_dict(d.pop("page"))

        share = FormShare.from_dict(d.pop("share"))

        status = check_form_status(d.pop("status"))

        created_by = d.pop("createdBy")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        _bound_fields = d.pop("boundFields", UNSET)
        bound_fields: list[FormBoundFieldsItem] | Unset = UNSET
        if _bound_fields is not UNSET:
            bound_fields = []
            for bound_fields_item_data in _bound_fields:
                bound_fields_item = FormBoundFieldsItem.from_dict(bound_fields_item_data)

                bound_fields.append(bound_fields_item)

        submission_count = d.pop("submissionCount", UNSET)

        form = cls(
            id=id,
            node_id=node_id,
            space_id=space_id,
            target_base_id=target_base_id,
            name=name,
            description=description,
            bindings=bindings,
            page=page,
            share=share,
            status=status,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            bound_fields=bound_fields,
            submission_count=submission_count,
        )

        form.additional_properties = d
        return form

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
