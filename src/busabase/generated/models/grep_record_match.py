from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GrepRecordMatch")


@_attrs_define
class GrepRecordMatch:
    """
    Attributes:
        source (Literal['records']):
        base_id (str):
        base_slug (str):
        record_id (str):
        field_slug (str):
        line (int):
        column (int):
        text (str):
        before (list[str]):
        after (list[str]):
    """

    source: Literal["records"]
    base_id: str
    base_slug: str
    record_id: str
    field_slug: str
    line: int
    column: int
    text: str
    before: list[str]
    after: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        base_id = self.base_id

        base_slug = self.base_slug

        record_id = self.record_id

        field_slug = self.field_slug

        line = self.line

        column = self.column

        text = self.text

        before = self.before

        after = self.after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "baseId": base_id,
                "baseSlug": base_slug,
                "recordId": record_id,
                "fieldSlug": field_slug,
                "line": line,
                "column": column,
                "text": text,
                "before": before,
                "after": after,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source = cast(Literal["records"], d.pop("source"))
        if source != "records":
            raise ValueError(f"source must match const 'records', got '{source}'")

        base_id = d.pop("baseId")

        base_slug = d.pop("baseSlug")

        record_id = d.pop("recordId")

        field_slug = d.pop("fieldSlug")

        line = d.pop("line")

        column = d.pop("column")

        text = d.pop("text")

        before = cast(list[str], d.pop("before"))

        after = cast(list[str], d.pop("after"))

        grep_record_match = cls(
            source=source,
            base_id=base_id,
            base_slug=base_slug,
            record_id=record_id,
            field_slug=field_slug,
            line=line,
            column=column,
            text=text,
            before=before,
            after=after,
        )

        grep_record_match.additional_properties = d
        return grep_record_match

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
