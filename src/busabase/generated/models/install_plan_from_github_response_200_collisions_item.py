from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.install_plan_from_github_response_200_collisions_item_kind import (
    InstallPlanFromGithubResponse200CollisionsItemKind,
    check_install_plan_from_github_response_200_collisions_item_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstallPlanFromGithubResponse200CollisionsItem")


@_attrs_define
class InstallPlanFromGithubResponse200CollisionsItem:
    """
    Attributes:
        kind (InstallPlanFromGithubResponse200CollisionsItemKind):
        slug (str):
        path (str):
        renamed_to (str | Unset):
    """

    kind: InstallPlanFromGithubResponse200CollisionsItemKind
    slug: str
    path: str
    renamed_to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        slug = self.slug

        path = self.path

        renamed_to = self.renamed_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "slug": slug,
                "path": path,
            }
        )
        if renamed_to is not UNSET:
            field_dict["renamedTo"] = renamed_to

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_install_plan_from_github_response_200_collisions_item_kind(d.pop("kind"))

        slug = d.pop("slug")

        path = d.pop("path")

        renamed_to = d.pop("renamedTo", UNSET)

        install_plan_from_github_response_200_collisions_item = cls(
            kind=kind,
            slug=slug,
            path=path,
            renamed_to=renamed_to,
        )

        install_plan_from_github_response_200_collisions_item.additional_properties = d
        return install_plan_from_github_response_200_collisions_item

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
