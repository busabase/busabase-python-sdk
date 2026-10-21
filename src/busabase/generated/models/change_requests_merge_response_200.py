from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.change_requests_merge_response_200_results_item_type_0 import (
        ChangeRequestsMergeResponse200ResultsItemType0,
    )
    from ..models.change_requests_merge_response_200_results_item_type_1 import (
        ChangeRequestsMergeResponse200ResultsItemType1,
    )


T = TypeVar("T", bound="ChangeRequestsMergeResponse200")


@_attrs_define
class ChangeRequestsMergeResponse200:
    """
    Attributes:
        results (list[ChangeRequestsMergeResponse200ResultsItemType0 | ChangeRequestsMergeResponse200ResultsItemType1]):
    """

    results: list[ChangeRequestsMergeResponse200ResultsItemType0 | ChangeRequestsMergeResponse200ResultsItemType1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.change_requests_merge_response_200_results_item_type_0 import (
            ChangeRequestsMergeResponse200ResultsItemType0,
        )

        results = []
        for results_item_data in self.results:
            results_item: dict[str, Any]
            if isinstance(results_item_data, ChangeRequestsMergeResponse200ResultsItemType0):
                results_item = results_item_data.to_dict()
            else:
                results_item = results_item_data.to_dict()

            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.change_requests_merge_response_200_results_item_type_0 import (
            ChangeRequestsMergeResponse200ResultsItemType0,
        )
        from ..models.change_requests_merge_response_200_results_item_type_1 import (
            ChangeRequestsMergeResponse200ResultsItemType1,
        )

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:

            def _parse_results_item(
                data: object,
            ) -> ChangeRequestsMergeResponse200ResultsItemType0 | ChangeRequestsMergeResponse200ResultsItemType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_0 = ChangeRequestsMergeResponse200ResultsItemType0.from_dict(data)

                    return results_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                results_item_type_1 = ChangeRequestsMergeResponse200ResultsItemType1.from_dict(data)

                return results_item_type_1

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        change_requests_merge_response_200 = cls(
            results=results,
        )

        change_requests_merge_response_200.additional_properties = d
        return change_requests_merge_response_200

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
