from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_result import SearchResult


T = TypeVar("T", bound="SearchResponse200")


@_attrs_define
class SearchResponse200:
    """
    Attributes:
        query (str):
        limit (float):
        offset (float):
        has_more (bool):
        results (list[SearchResult]):
        content_truncated (bool | Unset):  Default: False.
    """

    query: str
    limit: float
    offset: float
    has_more: bool
    results: list[SearchResult]
    content_truncated: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        limit = self.limit

        offset = self.offset

        has_more = self.has_more

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        content_truncated = self.content_truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "limit": limit,
                "offset": offset,
                "hasMore": has_more,
                "results": results,
            }
        )
        if content_truncated is not UNSET:
            field_dict["contentTruncated"] = content_truncated

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.search_result import SearchResult

        d = dict(src_dict)
        query = d.pop("query")

        limit = d.pop("limit")

        offset = d.pop("offset")

        has_more = d.pop("hasMore")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = SearchResult.from_dict(results_item_data)

            results.append(results_item)

        content_truncated = d.pop("contentTruncated", UNSET)

        search_response_200 = cls(
            query=query,
            limit=limit,
            offset=offset,
            has_more=has_more,
            results=results,
            content_truncated=content_truncated,
        )

        search_response_200.additional_properties = d
        return search_response_200

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
