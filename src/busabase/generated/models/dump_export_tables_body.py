from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dump_export_tables_body_table import DumpExportTablesBodyTable, check_dump_export_tables_body_table
from ..types import UNSET, Unset

T = TypeVar("T", bound="DumpExportTablesBody")


@_attrs_define
class DumpExportTablesBody:
    """
    Attributes:
        table (DumpExportTablesBodyTable):
        cursor (str | Unset):
        limit (int | Unset):  Default: 500.
    """

    table: DumpExportTablesBodyTable
    cursor: str | Unset = UNSET
    limit: int | Unset = 500
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table: str = self.table

        cursor = self.cursor

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "table": table,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        table = check_dump_export_tables_body_table(d.pop("table"))

        cursor = d.pop("cursor", UNSET)

        limit = d.pop("limit", UNSET)

        dump_export_tables_body = cls(
            table=table,
            cursor=cursor,
            limit=limit,
        )

        dump_export_tables_body.additional_properties = d
        return dump_export_tables_body

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
