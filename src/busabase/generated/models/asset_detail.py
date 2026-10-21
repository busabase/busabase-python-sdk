from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset import Asset
    from ..models.asset_usage import AssetUsage


T = TypeVar("T", bound="AssetDetail")


@_attrs_define
class AssetDetail:
    """
    Attributes:
        asset (Asset):
        usages (list[AssetUsage]):
    """

    asset: Asset
    usages: list[AssetUsage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset = self.asset.to_dict()

        usages = []
        for usages_item_data in self.usages:
            usages_item = usages_item_data.to_dict()
            usages.append(usages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset": asset,
                "usages": usages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.asset import Asset
        from ..models.asset_usage import AssetUsage

        d = dict(src_dict)
        asset = Asset.from_dict(d.pop("asset"))

        usages = []
        _usages = d.pop("usages")
        for usages_item_data in _usages:
            usages_item = AssetUsage.from_dict(usages_item_data)

            usages.append(usages_item)

        asset_detail = cls(
            asset=asset,
            usages=usages,
        )

        asset_detail.additional_properties = d
        return asset_detail

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
