from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grep_prompt_match_field import GrepPromptMatchField, check_grep_prompt_match_field
from ..types import UNSET, Unset

T = TypeVar("T", bound="GrepPromptMatch")


@_attrs_define
class GrepPromptMatch:
    """
    Attributes:
        source (Literal['prompts']):
        node_id (str):
        node_name (str):
        node_type (str):
        node_slug (str):
        key (str):
        locale (str):
        field (GrepPromptMatchField):
        line (int):
        column (int):
        text (str):
        before (list[str]):
        after (list[str]):
        label (str | Unset):
    """

    source: Literal["prompts"]
    node_id: str
    node_name: str
    node_type: str
    node_slug: str
    key: str
    locale: str
    field: GrepPromptMatchField
    line: int
    column: int
    text: str
    before: list[str]
    after: list[str]
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        node_id = self.node_id

        node_name = self.node_name

        node_type = self.node_type

        node_slug = self.node_slug

        key = self.key

        locale = self.locale

        field: str = self.field

        line = self.line

        column = self.column

        text = self.text

        before = self.before

        after = self.after

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "nodeId": node_id,
                "nodeName": node_name,
                "nodeType": node_type,
                "nodeSlug": node_slug,
                "key": key,
                "locale": locale,
                "field": field,
                "line": line,
                "column": column,
                "text": text,
                "before": before,
                "after": after,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source = cast(Literal["prompts"], d.pop("source"))
        if source != "prompts":
            raise ValueError(f"source must match const 'prompts', got '{source}'")

        node_id = d.pop("nodeId")

        node_name = d.pop("nodeName")

        node_type = d.pop("nodeType")

        node_slug = d.pop("nodeSlug")

        key = d.pop("key")

        locale = d.pop("locale")

        field = check_grep_prompt_match_field(d.pop("field"))

        line = d.pop("line")

        column = d.pop("column")

        text = d.pop("text")

        before = cast(list[str], d.pop("before"))

        after = cast(list[str], d.pop("after"))

        label = d.pop("label", UNSET)

        grep_prompt_match = cls(
            source=source,
            node_id=node_id,
            node_name=node_name,
            node_type=node_type,
            node_slug=node_slug,
            key=key,
            locale=locale,
            field=field,
            line=line,
            column=column,
            text=text,
            before=before,
            after=after,
            label=label,
        )

        grep_prompt_match.additional_properties = d
        return grep_prompt_match

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
