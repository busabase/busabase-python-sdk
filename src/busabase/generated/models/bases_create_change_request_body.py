from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bases_create_change_request_body_fields import BasesCreateChangeRequestBodyFields


T = TypeVar("T", bound="BasesCreateChangeRequestBody")


@_attrs_define
class BasesCreateChangeRequestBody:
    """
    Attributes:
        fields (BasesCreateChangeRequestBodyFields): Record field values keyed by field slug. A field id or its exact
            display name (any language, unambiguous) is mapped to the slug; a write in which no key names a field of the
            Base is a 400 listing the valid slugs. The base's PRIMARY field (its first field) becomes the record's display
            name and the change request title everywhere — always give it a short, human-readable value, never an id or
            placeholder.
        message (str | Unset): Explanation shown to the human reviewer. Write a conventional-commit style subject —
            imperative verb + what + why, e.g. "Add Acme Corp — qualified lead from the June webinar". Default: 'Initial
            change request'.
        submitted_by (str | Unset):  Default: 'local-producer'.
        idempotency_key (str | Unset): Optional client-supplied key that dedupes retries. Scoped per base + submitter:
            calling this endpoint again with the SAME idempotencyKey (e.g. after a timeout or a 5xx where you couldn't tell
            if the first call succeeded) returns the change request created by the first call instead of creating a
            duplicate. Omit for normal one-shot calls; only set it when you might retry.
        auto_merge (bool | Unset):
    """

    fields: BasesCreateChangeRequestBodyFields
    message: str | Unset = "Initial change request"
    submitted_by: str | Unset = "local-producer"
    idempotency_key: str | Unset = UNSET
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = self.fields.to_dict()

        message = self.message

        submitted_by = self.submitted_by

        idempotency_key = self.idempotency_key

        auto_merge = self.auto_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
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
        from ..models.bases_create_change_request_body_fields import BasesCreateChangeRequestBodyFields

        d = dict(src_dict)
        fields = BasesCreateChangeRequestBodyFields.from_dict(d.pop("fields"))

        message = d.pop("message", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        idempotency_key = d.pop("idempotencyKey", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        bases_create_change_request_body = cls(
            fields=fields,
            message=message,
            submitted_by=submitted_by,
            idempotency_key=idempotency_key,
            auto_merge=auto_merge,
        )

        bases_create_change_request_body.additional_properties = d
        return bases_create_change_request_body

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
