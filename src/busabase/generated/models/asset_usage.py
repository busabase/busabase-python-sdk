from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_usage_owner_type import AssetUsageOwnerType, check_asset_usage_owner_type

T = TypeVar("T", bound="AssetUsage")


@_attrs_define
class AssetUsage:
    """
    Attributes:
        owner_type (AssetUsageOwnerType):
        node_id (str):
        node_name (str):
        node_type (str):
        node_slug (str):
        path (None | str):
        record_id (None | str):
        field_slug (None | str):
        block_id (None | str):
        created_at (str):
    """

    owner_type: AssetUsageOwnerType
    node_id: str
    node_name: str
    node_type: str
    node_slug: str
    path: None | str
    record_id: None | str
    field_slug: None | str
    block_id: None | str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_type: str = self.owner_type

        node_id = self.node_id

        node_name = self.node_name

        node_type = self.node_type

        node_slug = self.node_slug

        path: None | str
        path = self.path

        record_id: None | str
        record_id = self.record_id

        field_slug: None | str
        field_slug = self.field_slug

        block_id: None | str
        block_id = self.block_id

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ownerType": owner_type,
                "nodeId": node_id,
                "nodeName": node_name,
                "nodeType": node_type,
                "nodeSlug": node_slug,
                "path": path,
                "recordId": record_id,
                "fieldSlug": field_slug,
                "blockId": block_id,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        owner_type = check_asset_usage_owner_type(d.pop("ownerType"))

        node_id = d.pop("nodeId")

        node_name = d.pop("nodeName")

        node_type = d.pop("nodeType")

        node_slug = d.pop("nodeSlug")

        def _parse_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        path = _parse_path(d.pop("path"))

        def _parse_record_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        record_id = _parse_record_id(d.pop("recordId"))

        def _parse_field_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        field_slug = _parse_field_slug(d.pop("fieldSlug"))

        def _parse_block_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        block_id = _parse_block_id(d.pop("blockId"))

        created_at = d.pop("createdAt")

        asset_usage = cls(
            owner_type=owner_type,
            node_id=node_id,
            node_name=node_name,
            node_type=node_type,
            node_slug=node_slug,
            path=path,
            record_id=record_id,
            field_slug=field_slug,
            block_id=block_id,
            created_at=created_at,
        )

        asset_usage.additional_properties = d
        return asset_usage

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
