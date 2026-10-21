from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assets_put_text_response_200_text_status import (
    AssetsPutTextResponse200TextStatus,
    check_assets_put_text_response_200_text_status,
)

T = TypeVar("T", bound="AssetsPutTextResponse200")


@_attrs_define
class AssetsPutTextResponse200:
    """
    Attributes:
        asset_id (str):
        text_status (AssetsPutTextResponse200TextStatus):
        line_count (int):
        char_count (int):
        byte_count (int):
    """

    asset_id: str
    text_status: AssetsPutTextResponse200TextStatus
    line_count: int
    char_count: int
    byte_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        text_status: str = self.text_status

        line_count = self.line_count

        char_count = self.char_count

        byte_count = self.byte_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
                "textStatus": text_status,
                "lineCount": line_count,
                "charCount": char_count,
                "byteCount": byte_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        asset_id = d.pop("assetId")

        text_status = check_assets_put_text_response_200_text_status(d.pop("textStatus"))

        line_count = d.pop("lineCount")

        char_count = d.pop("charCount")

        byte_count = d.pop("byteCount")

        assets_put_text_response_200 = cls(
            asset_id=asset_id,
            text_status=text_status,
            line_count=line_count,
            char_count=char_count,
            byte_count=byte_count,
        )

        assets_put_text_response_200.additional_properties = d
        return assets_put_text_response_200

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
