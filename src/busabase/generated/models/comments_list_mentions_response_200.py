from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.comments_list_mentions_response_200_items_item import CommentsListMentionsResponse200ItemsItem


T = TypeVar("T", bound="CommentsListMentionsResponse200")


@_attrs_define
class CommentsListMentionsResponse200:
    """
    Attributes:
        items (list[CommentsListMentionsResponse200ItemsItem]):
        total (int):
        unread_count (int):
    """

    items: list[CommentsListMentionsResponse200ItemsItem]
    total: int
    unread_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total = self.total

        unread_count = self.unread_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "total": total,
                "unreadCount": unread_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.comments_list_mentions_response_200_items_item import CommentsListMentionsResponse200ItemsItem

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = CommentsListMentionsResponse200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        total = d.pop("total")

        unread_count = d.pop("unreadCount")

        comments_list_mentions_response_200 = cls(
            items=items,
            total=total,
            unread_count=unread_count,
        )

        comments_list_mentions_response_200.additional_properties = d
        return comments_list_mentions_response_200

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
