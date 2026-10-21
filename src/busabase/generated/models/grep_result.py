from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.grep_file_match import GrepFileMatch
    from ..models.grep_node_match import GrepNodeMatch
    from ..models.grep_prompt_match import GrepPromptMatch
    from ..models.grep_record_match import GrepRecordMatch
    from ..models.grep_result_coverage import GrepResultCoverage


T = TypeVar("T", bound="GrepResult")


@_attrs_define
class GrepResult:
    """
    Attributes:
        matches (list[GrepFileMatch | GrepNodeMatch | GrepPromptMatch | GrepRecordMatch]):
        coverage (GrepResultCoverage):
        truncated (bool):
    """

    matches: list[GrepFileMatch | GrepNodeMatch | GrepPromptMatch | GrepRecordMatch]
    coverage: GrepResultCoverage
    truncated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.grep_file_match import GrepFileMatch
        from ..models.grep_node_match import GrepNodeMatch
        from ..models.grep_record_match import GrepRecordMatch

        matches = []
        for matches_item_data in self.matches:
            matches_item: dict[str, Any]
            if (
                isinstance(matches_item_data, GrepFileMatch)
                or isinstance(matches_item_data, GrepNodeMatch)
                or isinstance(matches_item_data, GrepRecordMatch)
            ):
                matches_item = matches_item_data.to_dict()
            else:
                matches_item = matches_item_data.to_dict()

            matches.append(matches_item)

        coverage = self.coverage.to_dict()

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matches": matches,
                "coverage": coverage,
                "truncated": truncated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grep_file_match import GrepFileMatch
        from ..models.grep_node_match import GrepNodeMatch
        from ..models.grep_prompt_match import GrepPromptMatch
        from ..models.grep_record_match import GrepRecordMatch
        from ..models.grep_result_coverage import GrepResultCoverage

        d = dict(src_dict)
        matches = []
        _matches = d.pop("matches")
        for matches_item_data in _matches:

            def _parse_matches_item(data: object) -> GrepFileMatch | GrepNodeMatch | GrepPromptMatch | GrepRecordMatch:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_grep_match_type_0 = GrepFileMatch.from_dict(data)

                    return componentsschemas_grep_match_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_grep_match_type_1 = GrepNodeMatch.from_dict(data)

                    return componentsschemas_grep_match_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_grep_match_type_2 = GrepRecordMatch.from_dict(data)

                    return componentsschemas_grep_match_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_grep_match_type_3 = GrepPromptMatch.from_dict(data)

                return componentsschemas_grep_match_type_3

            matches_item = _parse_matches_item(matches_item_data)

            matches.append(matches_item)

        coverage = GrepResultCoverage.from_dict(d.pop("coverage"))

        truncated = d.pop("truncated")

        grep_result = cls(
            matches=matches,
            coverage=coverage,
            truncated=truncated,
        )

        grep_result.additional_properties = d
        return grep_result

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
