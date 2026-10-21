from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstallFromGithubBody")


@_attrs_define
class InstallFromGithubBody:
    """
    Attributes:
        repo_url (str): GitHub repo URL: https://github.com/<owner>/<repo>[/tree/<ref>[/<subdir>]]. Only GitHub hosts
            are accepted.
        into_folder (str | Unset): Slug of the folder to install into. Defaults to the package manifest's name.
        rename (bool | Unset): Resolve slug collisions by suffixing (-2, -3, …) instead of refusing. Never overwrites
            anything.
        auto_merge (bool | Unset): Whether the package's content change requests merge on the spot. Omitted defaults to
            merging immediately when the caller holds write access (installing is already a space owner/admin operation, so
            normally they do), otherwise leaving them for review; pass explicit false to force review even with write
            access. Either way, installing trusts the package author: a package can carry skills and AirApps, i.e. code this
            space's agents will execute.
    """

    repo_url: str
    into_folder: str | Unset = UNSET
    rename: bool | Unset = UNSET
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_url = self.repo_url

        into_folder = self.into_folder

        rename = self.rename

        auto_merge = self.auto_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repoUrl": repo_url,
            }
        )
        if into_folder is not UNSET:
            field_dict["intoFolder"] = into_folder
        if rename is not UNSET:
            field_dict["rename"] = rename
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        repo_url = d.pop("repoUrl")

        into_folder = d.pop("intoFolder", UNSET)

        rename = d.pop("rename", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        install_from_github_body = cls(
            repo_url=repo_url,
            into_folder=into_folder,
            rename=rename,
            auto_merge=auto_merge,
        )

        install_from_github_body.additional_properties = d
        return install_from_github_body

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
