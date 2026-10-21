from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GrepResultCoveragePrompts")


@_attrs_define
class GrepResultCoveragePrompts:
    """
    Attributes:
        scanned (int):
        errored (list[str]):
        not_reached (int):
    """

    scanned: int
    errored: list[str]
    not_reached: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scanned = self.scanned

        errored = self.errored

        not_reached = self.not_reached

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scanned": scanned,
                "errored": errored,
                "notReached": not_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        scanned = d.pop("scanned")

        errored = cast(list[str], d.pop("errored"))

        not_reached = d.pop("notReached")

        grep_result_coverage_prompts = cls(
            scanned=scanned,
            errored=errored,
            not_reached=not_reached,
        )

        grep_result_coverage_prompts.additional_properties = d
        return grep_result_coverage_prompts

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
