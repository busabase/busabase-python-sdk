from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetsEditContentBodyEditsItem")


@_attrs_define
class AssetsEditContentBodyEditsItem:
    """
    Attributes:
        old_string (str):
        new_string (str):
        replace_all (bool | Unset):  Default: False.
    """

    old_string: str
    new_string: str
    replace_all: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        old_string = self.old_string

        new_string = self.new_string

        replace_all = self.replace_all

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "oldString": old_string,
                "newString": new_string,
            }
        )
        if replace_all is not UNSET:
            field_dict["replaceAll"] = replace_all

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        old_string = d.pop("oldString")

        new_string = d.pop("newString")

        replace_all = d.pop("replaceAll", UNSET)

        assets_edit_content_body_edits_item = cls(
            old_string=old_string,
            new_string=new_string,
            replace_all=replace_all,
        )

        return assets_edit_content_body_edits_item
