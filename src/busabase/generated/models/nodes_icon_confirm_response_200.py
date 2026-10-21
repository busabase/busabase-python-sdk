from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodesIconConfirmResponse200")


@_attrs_define
class NodesIconConfirmResponse200:
    """
    Attributes:
        success (bool):
        attachment_id (str):
        storage_key (str):
        public_url (str):
        asset_id (str | Unset):
    """

    success: bool
    attachment_id: str
    storage_key: str
    public_url: str
    asset_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        attachment_id = self.attachment_id

        storage_key = self.storage_key

        public_url = self.public_url

        asset_id = self.asset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "attachmentId": attachment_id,
                "storageKey": storage_key,
                "publicUrl": public_url,
            }
        )
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        success = d.pop("success")

        attachment_id = d.pop("attachmentId")

        storage_key = d.pop("storageKey")

        public_url = d.pop("publicUrl")

        asset_id = d.pop("assetId", UNSET)

        nodes_icon_confirm_response_200 = cls(
            success=success,
            attachment_id=attachment_id,
            storage_key=storage_key,
            public_url=public_url,
            asset_id=asset_id,
        )

        nodes_icon_confirm_response_200.additional_properties = d
        return nodes_icon_confirm_response_200

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
