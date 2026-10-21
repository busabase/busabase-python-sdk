from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operations_revise_body_fields import OperationsReviseBodyFields


T = TypeVar("T", bound="OperationsReviseBody")


@_attrs_define
class OperationsReviseBody:
    """
    Attributes:
        fields (OperationsReviseBodyFields): Updated field values keyed by field slug. A field id or its exact display
            name (any language, unambiguous) is mapped to the slug; a write in which no key names a field of the Base is a
            400 listing the valid slugs. If you set the base's PRIMARY field (its first field), keep it a short human-
            readable name — it is the record's display title everywhere.
        message (str | Unset): Explanation shown to the human reviewer. Write a conventional-commit style subject —
            imperative verb + what + why, e.g. "Update deal stage to qualified — demo booked for July 8". Default: 'Revise
            operation'.
        author (str | Unset):  Default: 'local-producer'.
        base_commit_id (str | Unset):
    """

    fields: OperationsReviseBodyFields
    message: str | Unset = "Revise operation"
    author: str | Unset = "local-producer"
    base_commit_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = self.fields.to_dict()

        message = self.message

        author = self.author

        base_commit_id = self.base_commit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if author is not UNSET:
            field_dict["author"] = author
        if base_commit_id is not UNSET:
            field_dict["baseCommitId"] = base_commit_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.operations_revise_body_fields import OperationsReviseBodyFields

        d = dict(src_dict)
        fields = OperationsReviseBodyFields.from_dict(d.pop("fields"))

        message = d.pop("message", UNSET)

        author = d.pop("author", UNSET)

        base_commit_id = d.pop("baseCommitId", UNSET)

        operations_revise_body = cls(
            fields=fields,
            message=message,
            author=author,
            base_commit_id=base_commit_id,
        )

        operations_revise_body.additional_properties = d
        return operations_revise_body

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
