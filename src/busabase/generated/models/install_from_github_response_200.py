from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.install_from_github_response_200_created import InstallFromGithubResponse200Created


T = TypeVar("T", bound="InstallFromGithubResponse200")


@_attrs_define
class InstallFromGithubResponse200:
    """
    Attributes:
        target_folder_slug (str):
        target_folder_node_id (str):
        created (InstallFromGithubResponse200Created):
        pending_change_requests (int):
        warnings (list[str] | Unset):
    """

    target_folder_slug: str
    target_folder_node_id: str
    created: InstallFromGithubResponse200Created
    pending_change_requests: int
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_folder_slug = self.target_folder_slug

        target_folder_node_id = self.target_folder_node_id

        created = self.created.to_dict()

        pending_change_requests = self.pending_change_requests

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetFolderSlug": target_folder_slug,
                "targetFolderNodeId": target_folder_node_id,
                "created": created,
                "pendingChangeRequests": pending_change_requests,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.install_from_github_response_200_created import InstallFromGithubResponse200Created

        d = dict(src_dict)
        target_folder_slug = d.pop("targetFolderSlug")

        target_folder_node_id = d.pop("targetFolderNodeId")

        created = InstallFromGithubResponse200Created.from_dict(d.pop("created"))

        pending_change_requests = d.pop("pendingChangeRequests")

        warnings = cast(list[str], d.pop("warnings", UNSET))

        install_from_github_response_200 = cls(
            target_folder_slug=target_folder_slug,
            target_folder_node_id=target_folder_node_id,
            created=created,
            pending_change_requests=pending_change_requests,
            warnings=warnings,
        )

        install_from_github_response_200.additional_properties = d
        return install_from_github_response_200

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
