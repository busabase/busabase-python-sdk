from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.install_plan_from_github_response_200_collisions_item import (
        InstallPlanFromGithubResponse200CollisionsItem,
    )
    from ..models.install_plan_from_github_response_200_counts import InstallPlanFromGithubResponse200Counts
    from ..models.install_plan_from_github_response_200_nodes_item import InstallPlanFromGithubResponse200NodesItem
    from ..models.install_plan_from_github_response_200_package import InstallPlanFromGithubResponse200Package
    from ..models.install_plan_from_github_response_200_source import InstallPlanFromGithubResponse200Source


T = TypeVar("T", bound="InstallPlanFromGithubResponse200")


@_attrs_define
class InstallPlanFromGithubResponse200:
    """
    Attributes:
        package (InstallPlanFromGithubResponse200Package):
        source (InstallPlanFromGithubResponse200Source):
        target_folder_slug (str):
        counts (InstallPlanFromGithubResponse200Counts):
        requires_auto_merge (bool):
        applicable (bool):
        nodes (list[InstallPlanFromGithubResponse200NodesItem] | Unset):
        collisions (list[InstallPlanFromGithubResponse200CollisionsItem] | Unset):
        warnings (list[str] | Unset):
    """

    package: InstallPlanFromGithubResponse200Package
    source: InstallPlanFromGithubResponse200Source
    target_folder_slug: str
    counts: InstallPlanFromGithubResponse200Counts
    requires_auto_merge: bool
    applicable: bool
    nodes: list[InstallPlanFromGithubResponse200NodesItem] | Unset = UNSET
    collisions: list[InstallPlanFromGithubResponse200CollisionsItem] | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package = self.package.to_dict()

        source = self.source.to_dict()

        target_folder_slug = self.target_folder_slug

        counts = self.counts.to_dict()

        requires_auto_merge = self.requires_auto_merge

        applicable = self.applicable

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        collisions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collisions, Unset):
            collisions = []
            for collisions_item_data in self.collisions:
                collisions_item = collisions_item_data.to_dict()
                collisions.append(collisions_item)

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package": package,
                "source": source,
                "targetFolderSlug": target_folder_slug,
                "counts": counts,
                "requiresAutoMerge": requires_auto_merge,
                "applicable": applicable,
            }
        )
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if collisions is not UNSET:
            field_dict["collisions"] = collisions
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.install_plan_from_github_response_200_collisions_item import (
            InstallPlanFromGithubResponse200CollisionsItem,
        )
        from ..models.install_plan_from_github_response_200_counts import InstallPlanFromGithubResponse200Counts
        from ..models.install_plan_from_github_response_200_nodes_item import InstallPlanFromGithubResponse200NodesItem
        from ..models.install_plan_from_github_response_200_package import InstallPlanFromGithubResponse200Package
        from ..models.install_plan_from_github_response_200_source import InstallPlanFromGithubResponse200Source

        d = dict(src_dict)
        package = InstallPlanFromGithubResponse200Package.from_dict(d.pop("package"))

        source = InstallPlanFromGithubResponse200Source.from_dict(d.pop("source"))

        target_folder_slug = d.pop("targetFolderSlug")

        counts = InstallPlanFromGithubResponse200Counts.from_dict(d.pop("counts"))

        requires_auto_merge = d.pop("requiresAutoMerge")

        applicable = d.pop("applicable")

        _nodes = d.pop("nodes", UNSET)
        nodes: list[InstallPlanFromGithubResponse200NodesItem] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = InstallPlanFromGithubResponse200NodesItem.from_dict(nodes_item_data)

                nodes.append(nodes_item)

        _collisions = d.pop("collisions", UNSET)
        collisions: list[InstallPlanFromGithubResponse200CollisionsItem] | Unset = UNSET
        if _collisions is not UNSET:
            collisions = []
            for collisions_item_data in _collisions:
                collisions_item = InstallPlanFromGithubResponse200CollisionsItem.from_dict(collisions_item_data)

                collisions.append(collisions_item)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        install_plan_from_github_response_200 = cls(
            package=package,
            source=source,
            target_folder_slug=target_folder_slug,
            counts=counts,
            requires_auto_merge=requires_auto_merge,
            applicable=applicable,
            nodes=nodes,
            collisions=collisions,
            warnings=warnings,
        )

        install_plan_from_github_response_200.additional_properties = d
        return install_plan_from_github_response_200

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
