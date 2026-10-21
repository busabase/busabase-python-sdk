from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TemplatesListResponse200TemplatesItemStats")


@_attrs_define
class TemplatesListResponse200TemplatesItemStats:
    """
    Attributes:
        folders (int):
        docs (int):
        bases (int):
        records (int):
        files (int):
        airapps (int):
        skill (bool):
    """

    folders: int
    docs: int
    bases: int
    records: int
    files: int
    airapps: int
    skill: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folders = self.folders

        docs = self.docs

        bases = self.bases

        records = self.records

        files = self.files

        airapps = self.airapps

        skill = self.skill

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folders": folders,
                "docs": docs,
                "bases": bases,
                "records": records,
                "files": files,
                "airapps": airapps,
                "skill": skill,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        folders = d.pop("folders")

        docs = d.pop("docs")

        bases = d.pop("bases")

        records = d.pop("records")

        files = d.pop("files")

        airapps = d.pop("airapps")

        skill = d.pop("skill")

        templates_list_response_200_templates_item_stats = cls(
            folders=folders,
            docs=docs,
            bases=bases,
            records=records,
            files=files,
            airapps=airapps,
            skill=skill,
        )

        templates_list_response_200_templates_item_stats.additional_properties = d
        return templates_list_response_200_templates_item_stats

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
