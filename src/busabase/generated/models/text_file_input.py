from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextFileInput")


@_attrs_define
class TextFileInput:
    """
    Attributes:
        path (str):
        content (str | Unset):  Default: ''.
        mime_type (str | Unset):
    """

    path: str
    content: str | Unset = ""
    mime_type: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        content = self.content

        mime_type = self.mime_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "path": path,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        path = d.pop("path")

        content = d.pop("content", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        text_file_input = cls(
            path=path,
            content=content,
            mime_type=mime_type,
        )

        return text_file_input
