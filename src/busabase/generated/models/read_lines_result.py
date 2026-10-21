from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReadLinesResult")


@_attrs_define
class ReadLinesResult:
    """
    Attributes:
        lines (list[str]):
        start_line (int):
        end_line (int):
        total_lines (int):
        truncated (bool):
    """

    lines: list[str]
    start_line: int
    end_line: int
    total_lines: int
    truncated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lines = self.lines

        start_line = self.start_line

        end_line = self.end_line

        total_lines = self.total_lines

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lines": lines,
                "startLine": start_line,
                "endLine": end_line,
                "totalLines": total_lines,
                "truncated": truncated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lines = cast(list[str], d.pop("lines"))

        start_line = d.pop("startLine")

        end_line = d.pop("endLine")

        total_lines = d.pop("totalLines")

        truncated = d.pop("truncated")

        read_lines_result = cls(
            lines=lines,
            start_line=start_line,
            end_line=end_line,
            total_lines=total_lines,
            truncated=truncated,
        )

        read_lines_result.additional_properties = d
        return read_lines_result

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
