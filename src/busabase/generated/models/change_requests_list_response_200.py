from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.change_request import ChangeRequest


T = TypeVar("T", bound="ChangeRequestsListResponse200")


@_attrs_define
class ChangeRequestsListResponse200:
    """
    Attributes:
        change_requests (list[ChangeRequest]):
        next_cursor (None | str):
    """

    change_requests: list[ChangeRequest]
    next_cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_requests = []
        for change_requests_item_data in self.change_requests:
            change_requests_item = change_requests_item_data.to_dict()
            change_requests.append(change_requests_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changeRequests": change_requests,
                "nextCursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.change_request import ChangeRequest

        d = dict(src_dict)
        change_requests = []
        _change_requests = d.pop("changeRequests")
        for change_requests_item_data in _change_requests:
            change_requests_item = ChangeRequest.from_dict(change_requests_item_data)

            change_requests.append(change_requests_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))

        change_requests_list_response_200 = cls(
            change_requests=change_requests,
            next_cursor=next_cursor,
        )

        change_requests_list_response_200.additional_properties = d
        return change_requests_list_response_200

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
