from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstallPlanFromGithubResponse200Source")


@_attrs_define
class InstallPlanFromGithubResponse200Source:
    """
    Attributes:
        owner (str):
        repo (str):
        ref (str | Unset):
        subdir (str | Unset):
    """

    owner: str
    repo: str
    ref: str | Unset = UNSET
    subdir: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner = self.owner

        repo = self.repo

        ref = self.ref

        subdir = self.subdir

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "repo": repo,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref
        if subdir is not UNSET:
            field_dict["subdir"] = subdir

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        owner = d.pop("owner")

        repo = d.pop("repo")

        ref = d.pop("ref", UNSET)

        subdir = d.pop("subdir", UNSET)

        install_plan_from_github_response_200_source = cls(
            owner=owner,
            repo=repo,
            ref=ref,
            subdir=subdir,
        )

        install_plan_from_github_response_200_source.additional_properties = d
        return install_plan_from_github_response_200_source

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
