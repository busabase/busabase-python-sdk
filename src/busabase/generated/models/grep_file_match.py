from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grep_match_owner import GrepMatchOwner


T = TypeVar("T", bound="GrepFileMatch")


@_attrs_define
class GrepFileMatch:
    """
    Attributes:
        source (Literal['files']):
        asset_id (str):
        file_name (str):
        drive_path (str):
        line (int):
        column (int):
        text (str):
        before (list[str]):
        after (list[str]):
        owner (GrepMatchOwner | Unset):
    """

    source: Literal["files"]
    asset_id: str
    file_name: str
    drive_path: str
    line: int
    column: int
    text: str
    before: list[str]
    after: list[str]
    owner: GrepMatchOwner | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        asset_id = self.asset_id

        file_name = self.file_name

        drive_path = self.drive_path

        line = self.line

        column = self.column

        text = self.text

        before = self.before

        after = self.after

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "assetId": asset_id,
                "fileName": file_name,
                "drivePath": drive_path,
                "line": line,
                "column": column,
                "text": text,
                "before": before,
                "after": after,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grep_match_owner import GrepMatchOwner

        d = dict(src_dict)
        source = cast(Literal["files"], d.pop("source"))
        if source != "files":
            raise ValueError(f"source must match const 'files', got '{source}'")

        asset_id = d.pop("assetId")

        file_name = d.pop("fileName")

        drive_path = d.pop("drivePath")

        line = d.pop("line")

        column = d.pop("column")

        text = d.pop("text")

        before = cast(list[str], d.pop("before"))

        after = cast(list[str], d.pop("after"))

        _owner = d.pop("owner", UNSET)
        owner: GrepMatchOwner | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = GrepMatchOwner.from_dict(_owner)

        grep_file_match = cls(
            source=source,
            asset_id=asset_id,
            file_name=file_name,
            drive_path=drive_path,
            line=line,
            column=column,
            text=text,
            before=before,
            after=after,
            owner=owner,
        )

        grep_file_match.additional_properties = d
        return grep_file_match

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
