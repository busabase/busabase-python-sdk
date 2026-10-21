from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.change_request import ChangeRequest


T = TypeVar("T", bound="ChangeRequestsListPageResponse200")


@_attrs_define
class ChangeRequestsListPageResponse200:
    """
    Attributes:
        change_requests (list[ChangeRequest]):
        total (int):
        total_pages (int):
        page (int):
        page_size (int):
    """

    change_requests: list[ChangeRequest]
    total: int
    total_pages: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_requests = []
        for change_requests_item_data in self.change_requests:
            change_requests_item = change_requests_item_data.to_dict()
            change_requests.append(change_requests_item)

        total = self.total

        total_pages = self.total_pages

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changeRequests": change_requests,
                "total": total,
                "totalPages": total_pages,
                "page": page,
                "pageSize": page_size,
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

        total = d.pop("total")

        total_pages = d.pop("totalPages")

        page = d.pop("page")

        page_size = d.pop("pageSize")

        change_requests_list_page_response_200 = cls(
            change_requests=change_requests,
            total=total,
            total_pages=total_pages,
            page=page,
            page_size=page_size,
        )

        change_requests_list_page_response_200.additional_properties = d
        return change_requests_list_page_response_200

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
