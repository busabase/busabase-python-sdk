from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bases_create_bulk_update_change_request_body_updates_item_fields import (
        BasesCreateBulkUpdateChangeRequestBodyUpdatesItemFields,
    )


T = TypeVar("T", bound="BasesCreateBulkUpdateChangeRequestBodyUpdatesItem")


@_attrs_define
class BasesCreateBulkUpdateChangeRequestBodyUpdatesItem:
    """
    Attributes:
        record_id (str):
        fields (BasesCreateBulkUpdateChangeRequestBodyUpdatesItemFields): The fields to change, keyed by field slug. A
            field id or its exact display name (any language, unambiguous) is mapped to the slug; an update in which no key
            names a field of the Base is a 400 listing the valid slugs.
        base_commit_id (str | Unset):
        message (str | Unset):
    """

    record_id: str
    fields: BasesCreateBulkUpdateChangeRequestBodyUpdatesItemFields
    base_commit_id: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        fields = self.fields.to_dict()

        base_commit_id = self.base_commit_id

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recordId": record_id,
                "fields": fields,
            }
        )
        if base_commit_id is not UNSET:
            field_dict["baseCommitId"] = base_commit_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bases_create_bulk_update_change_request_body_updates_item_fields import (
            BasesCreateBulkUpdateChangeRequestBodyUpdatesItemFields,
        )

        d = dict(src_dict)
        record_id = d.pop("recordId")

        fields = BasesCreateBulkUpdateChangeRequestBodyUpdatesItemFields.from_dict(d.pop("fields"))

        base_commit_id = d.pop("baseCommitId", UNSET)

        message = d.pop("message", UNSET)

        bases_create_bulk_update_change_request_body_updates_item = cls(
            record_id=record_id,
            fields=fields,
            base_commit_id=base_commit_id,
            message=message,
        )

        bases_create_bulk_update_change_request_body_updates_item.additional_properties = d
        return bases_create_bulk_update_change_request_body_updates_item

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
