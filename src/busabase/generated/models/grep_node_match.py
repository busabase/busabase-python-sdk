from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grep_node_match_type import GrepNodeMatchType, check_grep_node_match_type

T = TypeVar("T", bound="GrepNodeMatch")


@_attrs_define
class GrepNodeMatch:
    """
    Attributes:
        source (Literal['nodes']):
        type_ (GrepNodeMatchType):
        node_id (str):
        slug (str):
        name (str):
        line (int):
        column (int):
        text (str):
        before (list[str]):
        after (list[str]):
    """

    source: Literal["nodes"]
    type_: GrepNodeMatchType
    node_id: str
    slug: str
    name: str
    line: int
    column: int
    text: str
    before: list[str]
    after: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        type_: str = self.type_

        node_id = self.node_id

        slug = self.slug

        name = self.name

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
                "type": type_,
                "nodeId": node_id,
                "slug": slug,
                "name": name,
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
        source = cast(Literal["nodes"], d.pop("source"))
        if source != "nodes":
            raise ValueError(f"source must match const 'nodes', got '{source}'")

        type_ = check_grep_node_match_type(d.pop("type"))

        node_id = d.pop("nodeId")

        slug = d.pop("slug")

        name = d.pop("name")

        line = d.pop("line")

        column = d.pop("column")

        text = d.pop("text")

        before = cast(list[str], d.pop("before"))

        after = cast(list[str], d.pop("after"))

        grep_node_match = cls(
            source=source,
            type_=type_,
            node_id=node_id,
            slug=slug,
            name=name,
            line=line,
            column=column,
            text=text,
            before=before,
            after=after,
        )

        grep_node_match.additional_properties = d
        return grep_node_match

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
