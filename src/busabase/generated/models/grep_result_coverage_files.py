from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GrepResultCoverageFiles")


@_attrs_define
class GrepResultCoverageFiles:
    """
    Attributes:
        scanned (int):
        missing (list[str]):
        stale (list[str]):
        unsearchable (int):
        errored (list[str]):
        not_reached (int):
    """

    scanned: int
    missing: list[str]
    stale: list[str]
    unsearchable: int
    errored: list[str]
    not_reached: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scanned = self.scanned

        missing = self.missing

        stale = self.stale

        unsearchable = self.unsearchable

        errored = self.errored

        not_reached = self.not_reached

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scanned": scanned,
                "missing": missing,
                "stale": stale,
                "unsearchable": unsearchable,
                "errored": errored,
                "notReached": not_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        scanned = d.pop("scanned")

        missing = cast(list[str], d.pop("missing"))

        stale = cast(list[str], d.pop("stale"))

        unsearchable = d.pop("unsearchable")

        errored = cast(list[str], d.pop("errored"))

        not_reached = d.pop("notReached")

        grep_result_coverage_files = cls(
            scanned=scanned,
            missing=missing,
            stale=stale,
            unsearchable=unsearchable,
            errored=errored,
            not_reached=not_reached,
        )

        grep_result_coverage_files.additional_properties = d
        return grep_result_coverage_files

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
