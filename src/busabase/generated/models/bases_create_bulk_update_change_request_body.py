from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bases_create_bulk_update_change_request_body_updates_item import (
        BasesCreateBulkUpdateChangeRequestBodyUpdatesItem,
    )


T = TypeVar("T", bound="BasesCreateBulkUpdateChangeRequestBody")


@_attrs_define
class BasesCreateBulkUpdateChangeRequestBody:
    """
    Attributes:
        updates (list[BasesCreateBulkUpdateChangeRequestBodyUpdatesItem]):
        message (str | Unset):  Default: 'Bulk update records'.
        submitted_by (str | Unset):  Default: 'local-producer'.
        idempotency_key (str | Unset):
        auto_merge (bool | Unset):
    """

    updates: list[BasesCreateBulkUpdateChangeRequestBodyUpdatesItem]
    message: str | Unset = "Bulk update records"
    submitted_by: str | Unset = "local-producer"
    idempotency_key: str | Unset = UNSET
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updates = []
        for updates_item_data in self.updates:
            updates_item = updates_item_data.to_dict()
            updates.append(updates_item)

        message = self.message

        submitted_by = self.submitted_by

        idempotency_key = self.idempotency_key

        auto_merge = self.auto_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updates": updates,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if submitted_by is not UNSET:
            field_dict["submittedBy"] = submitted_by
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bases_create_bulk_update_change_request_body_updates_item import (
            BasesCreateBulkUpdateChangeRequestBodyUpdatesItem,
        )

        d = dict(src_dict)
        updates = []
        _updates = d.pop("updates")
        for updates_item_data in _updates:
            updates_item = BasesCreateBulkUpdateChangeRequestBodyUpdatesItem.from_dict(updates_item_data)

            updates.append(updates_item)

        message = d.pop("message", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        idempotency_key = d.pop("idempotencyKey", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        bases_create_bulk_update_change_request_body = cls(
            updates=updates,
            message=message,
            submitted_by=submitted_by,
            idempotency_key=idempotency_key,
            auto_merge=auto_merge,
        )

        bases_create_bulk_update_change_request_body.additional_properties = d
        return bases_create_bulk_update_change_request_body

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
