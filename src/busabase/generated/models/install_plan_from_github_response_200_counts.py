from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InstallPlanFromGithubResponse200Counts")


@_attrs_define
class InstallPlanFromGithubResponse200Counts:
    """
    Attributes:
        folders (int):
        docs (int):
        bases (int):
        records (int):
        skills (int):
        airapps (int):
        drives (int):
        files (int):
    """

    folders: int
    docs: int
    bases: int
    records: int
    skills: int
    airapps: int
    drives: int
    files: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folders = self.folders

        docs = self.docs

        bases = self.bases

        records = self.records

        skills = self.skills

        airapps = self.airapps

        drives = self.drives

        files = self.files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folders": folders,
                "docs": docs,
                "bases": bases,
                "records": records,
                "skills": skills,
                "airapps": airapps,
                "drives": drives,
                "files": files,
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

        skills = d.pop("skills")

        airapps = d.pop("airapps")

        drives = d.pop("drives")

        files = d.pop("files")

        install_plan_from_github_response_200_counts = cls(
            folders=folders,
            docs=docs,
            bases=bases,
            records=records,
            skills=skills,
            airapps=airapps,
            drives=drives,
            files=files,
        )

        install_plan_from_github_response_200_counts.additional_properties = d
        return install_plan_from_github_response_200_counts

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
