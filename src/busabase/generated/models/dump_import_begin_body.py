from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DumpImportBeginBody")


@_attrs_define
class DumpImportBeginBody:
    """
    Attributes:
        source_space_id (str):
        resume (bool | Unset):  Default: False.
    """

    source_space_id: str
    resume: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_space_id = self.source_space_id

        resume = self.resume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceSpaceId": source_space_id,
            }
        )
        if resume is not UNSET:
            field_dict["resume"] = resume

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_space_id = d.pop("sourceSpaceId")

        resume = d.pop("resume", UNSET)

        dump_import_begin_body = cls(
            source_space_id=source_space_id,
            resume=resume,
        )

        dump_import_begin_body.additional_properties = d
        return dump_import_begin_body

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
