from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.vault_item import VaultItem


T = TypeVar("T", bound="VaultSettings")


@_attrs_define
class VaultSettings:
    """
    Attributes:
        owner_id (None | str):
        items (list[VaultItem]):
        updated_at (None | str):
    """

    owner_id: None | str
    items: list[VaultItem]
    updated_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_id: None | str
        owner_id = self.owner_id

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        updated_at: None | str
        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ownerId": owner_id,
                "items": items,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vault_item import VaultItem

        d = dict(src_dict)

        def _parse_owner_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        owner_id = _parse_owner_id(d.pop("ownerId"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = VaultItem.from_dict(items_item_data)

            items.append(items_item)

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        vault_settings = cls(
            owner_id=owner_id,
            items=items,
            updated_at=updated_at,
        )

        vault_settings.additional_properties = d
        return vault_settings

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
