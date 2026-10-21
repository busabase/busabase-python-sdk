from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FileTreeFile")


@_attrs_define
class FileTreeFile:
    """
    Attributes:
        path (str):
        name (str):
        size (float):
        updated_at (None | str):
        mime_type (None | str):
        asset_id (str):
        display_name (None | str):
    """

    path: str
    name: str
    size: float
    updated_at: None | str
    mime_type: None | str
    asset_id: str
    display_name: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        name = self.name

        size = self.size

        updated_at: None | str
        updated_at = self.updated_at

        mime_type: None | str
        mime_type = self.mime_type

        asset_id = self.asset_id

        display_name: None | str
        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "name": name,
                "size": size,
                "updatedAt": updated_at,
                "mimeType": mime_type,
                "assetId": asset_id,
                "displayName": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        path = d.pop("path")

        name = d.pop("name")

        size = d.pop("size")

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        def _parse_mime_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mime_type = _parse_mime_type(d.pop("mimeType"))

        asset_id = d.pop("assetId")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("displayName"))

        file_tree_file = cls(
            path=path,
            name=name,
            size=size,
            updated_at=updated_at,
            mime_type=mime_type,
            asset_id=asset_id,
            display_name=display_name,
        )

        file_tree_file.additional_properties = d
        return file_tree_file

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
