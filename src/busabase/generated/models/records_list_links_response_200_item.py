from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecordsListLinksResponse200Item")


@_attrs_define
class RecordsListLinksResponse200Item:
    """
    Attributes:
        id (str):
        base_id (str):
        field_id (str):
        field_slug (str):
        source_record_id (str):
        target_base_id (str):
        target_record_id (str):
        commit_id (str):
        position (float):
        created_at (str):
        updated_at (str):
    """

    id: str
    base_id: str
    field_id: str
    field_slug: str
    source_record_id: str
    target_base_id: str
    target_record_id: str
    commit_id: str
    position: float
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        base_id = self.base_id

        field_id = self.field_id

        field_slug = self.field_slug

        source_record_id = self.source_record_id

        target_base_id = self.target_base_id

        target_record_id = self.target_record_id

        commit_id = self.commit_id

        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "baseId": base_id,
                "fieldId": field_id,
                "fieldSlug": field_slug,
                "sourceRecordId": source_record_id,
                "targetBaseId": target_base_id,
                "targetRecordId": target_record_id,
                "commitId": commit_id,
                "position": position,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        base_id = d.pop("baseId")

        field_id = d.pop("fieldId")

        field_slug = d.pop("fieldSlug")

        source_record_id = d.pop("sourceRecordId")

        target_base_id = d.pop("targetBaseId")

        target_record_id = d.pop("targetRecordId")

        commit_id = d.pop("commitId")

        position = d.pop("position")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        records_list_links_response_200_item = cls(
            id=id,
            base_id=base_id,
            field_id=field_id,
            field_slug=field_slug,
            source_record_id=source_record_id,
            target_base_id=target_base_id,
            target_record_id=target_record_id,
            commit_id=commit_id,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
        )

        records_list_links_response_200_item.additional_properties = d
        return records_list_links_response_200_item

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
