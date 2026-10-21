from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assets_update_metadata_body_mode import (
    AssetsUpdateMetadataBodyMode,
    check_assets_update_metadata_body_mode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assets_update_metadata_body_metadata import AssetsUpdateMetadataBodyMetadata


T = TypeVar("T", bound="AssetsUpdateMetadataBody")


@_attrs_define
class AssetsUpdateMetadataBody:
    """
    Attributes:
        metadata (AssetsUpdateMetadataBodyMetadata):
        mode (AssetsUpdateMetadataBodyMode | Unset):  Default: 'merge'.
    """

    metadata: AssetsUpdateMetadataBodyMetadata
    mode: AssetsUpdateMetadataBodyMode | Unset = "merge"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assets_update_metadata_body_metadata import AssetsUpdateMetadataBodyMetadata

        d = dict(src_dict)
        metadata = AssetsUpdateMetadataBodyMetadata.from_dict(d.pop("metadata"))

        _mode = d.pop("mode", UNSET)
        mode: AssetsUpdateMetadataBodyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_assets_update_metadata_body_mode(_mode)

        assets_update_metadata_body = cls(
            metadata=metadata,
            mode=mode,
        )

        assets_update_metadata_body.additional_properties = d
        return assets_update_metadata_body

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
