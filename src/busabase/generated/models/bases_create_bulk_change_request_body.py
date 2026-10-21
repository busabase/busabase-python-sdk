from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bases_create_bulk_change_request_body_records_item import BasesCreateBulkChangeRequestBodyRecordsItem


T = TypeVar("T", bound="BasesCreateBulkChangeRequestBody")


@_attrs_define
class BasesCreateBulkChangeRequestBody:
    """
    Attributes:
        records (list[BasesCreateBulkChangeRequestBodyRecordsItem]): Field-value maps, one per record to create, each
            keyed by field slug. A field id or its exact display name (any language, unambiguous) is mapped to the slug; a
            write in which no key names a field of the Base is a 400 listing the valid slugs. All records are proposed as a
            SINGLE change request (one review, one merge) — use this to import/seed many rows at once instead of one change
            request per record. Capped at 1000; for very large loads prefer a dedicated import job. Always give each
            record's PRIMARY field a short human-readable value.
        message (str | Unset): Explanation shown to the human reviewer for the whole batch — e.g. "Import 240 June
            webinar leads". Default: 'Bulk create records'.
        submitted_by (str | Unset):  Default: 'local-producer'.
        idempotency_key (str | Unset): Optional client-supplied key that dedupes retries. Scoped per base + submitter:
            calling this endpoint again with the SAME idempotencyKey returns the bulk change request created by the first
            call instead of creating a duplicate. Omit for normal one-shot calls; only set it when you might retry.
        auto_merge (bool | Unset):
    """

    records: list[BasesCreateBulkChangeRequestBodyRecordsItem]
    message: str | Unset = "Bulk create records"
    submitted_by: str | Unset = "local-producer"
    idempotency_key: str | Unset = UNSET
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        message = self.message

        submitted_by = self.submitted_by

        idempotency_key = self.idempotency_key

        auto_merge = self.auto_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "records": records,
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
        from ..models.bases_create_bulk_change_request_body_records_item import (
            BasesCreateBulkChangeRequestBodyRecordsItem,
        )

        d = dict(src_dict)
        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = BasesCreateBulkChangeRequestBodyRecordsItem.from_dict(records_item_data)

            records.append(records_item)

        message = d.pop("message", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        idempotency_key = d.pop("idempotencyKey", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        bases_create_bulk_change_request_body = cls(
            records=records,
            message=message,
            submitted_by=submitted_by,
            idempotency_key=idempotency_key,
            auto_merge=auto_merge,
        )

        bases_create_bulk_change_request_body.additional_properties = d
        return bases_create_bulk_change_request_body

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
