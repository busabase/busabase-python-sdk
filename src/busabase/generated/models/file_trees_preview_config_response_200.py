from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_trees_preview_config_response_200_credential_source import (
    FileTreesPreviewConfigResponse200CredentialSource,
    check_file_trees_preview_config_response_200_credential_source,
)
from ..models.file_trees_preview_config_response_200_provider import (
    FileTreesPreviewConfigResponse200Provider,
    check_file_trees_preview_config_response_200_provider,
)
from ..models.file_trees_preview_config_response_200_status import (
    FileTreesPreviewConfigResponse200Status,
    check_file_trees_preview_config_response_200_status,
)

T = TypeVar("T", bound="FileTreesPreviewConfigResponse200")


@_attrs_define
class FileTreesPreviewConfigResponse200:
    """
    Attributes:
        provider (FileTreesPreviewConfigResponse200Provider):
        status (FileTreesPreviewConfigResponse200Status):
        credential_source (FileTreesPreviewConfigResponse200CredentialSource):
        credential_configured (bool):
        max_file_size_bytes (int):
        session_ttl_minutes (int):
        vault_encryption_configured (bool | None):
    """

    provider: FileTreesPreviewConfigResponse200Provider
    status: FileTreesPreviewConfigResponse200Status
    credential_source: FileTreesPreviewConfigResponse200CredentialSource
    credential_configured: bool
    max_file_size_bytes: int
    session_ttl_minutes: int
    vault_encryption_configured: bool | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider: str = self.provider

        status: str = self.status

        credential_source: str = self.credential_source

        credential_configured = self.credential_configured

        max_file_size_bytes = self.max_file_size_bytes

        session_ttl_minutes = self.session_ttl_minutes

        vault_encryption_configured: bool | None
        vault_encryption_configured = self.vault_encryption_configured

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "status": status,
                "credentialSource": credential_source,
                "credentialConfigured": credential_configured,
                "maxFileSizeBytes": max_file_size_bytes,
                "sessionTtlMinutes": session_ttl_minutes,
                "vaultEncryptionConfigured": vault_encryption_configured,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        provider = check_file_trees_preview_config_response_200_provider(d.pop("provider"))

        status = check_file_trees_preview_config_response_200_status(d.pop("status"))

        credential_source = check_file_trees_preview_config_response_200_credential_source(d.pop("credentialSource"))

        credential_configured = d.pop("credentialConfigured")

        max_file_size_bytes = d.pop("maxFileSizeBytes")

        session_ttl_minutes = d.pop("sessionTtlMinutes")

        def _parse_vault_encryption_configured(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        vault_encryption_configured = _parse_vault_encryption_configured(d.pop("vaultEncryptionConfigured"))

        file_trees_preview_config_response_200 = cls(
            provider=provider,
            status=status,
            credential_source=credential_source,
            credential_configured=credential_configured,
            max_file_size_bytes=max_file_size_bytes,
            session_ttl_minutes=session_ttl_minutes,
            vault_encryption_configured=vault_encryption_configured,
        )

        file_trees_preview_config_response_200.additional_properties = d
        return file_trees_preview_config_response_200

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
