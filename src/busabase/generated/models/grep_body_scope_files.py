from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GrepBodyScopeFiles")


@_attrs_define
class GrepBodyScopeFiles:
    """
    Attributes:
        asset_ids (list[str] | Unset):
        drive_path (str | Unset):
        mime_types (list[str] | Unset):
    """

    asset_ids: list[str] | Unset = UNSET
    drive_path: str | Unset = UNSET
    mime_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_ids: list[str] | Unset = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = self.asset_ids

        drive_path = self.drive_path

        mime_types: list[str] | Unset = UNSET
        if not isinstance(self.mime_types, Unset):
            mime_types = self.mime_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_ids is not UNSET:
            field_dict["assetIds"] = asset_ids
        if drive_path is not UNSET:
            field_dict["drivePath"] = drive_path
        if mime_types is not UNSET:
            field_dict["mimeTypes"] = mime_types

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        asset_ids = cast(list[str], d.pop("assetIds", UNSET))

        drive_path = d.pop("drivePath", UNSET)

        mime_types = cast(list[str], d.pop("mimeTypes", UNSET))

        grep_body_scope_files = cls(
            asset_ids=asset_ids,
            drive_path=drive_path,
            mime_types=mime_types,
        )

        grep_body_scope_files.additional_properties = d
        return grep_body_scope_files

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
