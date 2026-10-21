from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dump_import_tables_body_table_type_0 import (
    DumpImportTablesBodyTableType0,
    check_dump_import_tables_body_table_type_0,
)

if TYPE_CHECKING:
    from ..models.dump_import_tables_body_rows_item import DumpImportTablesBodyRowsItem


T = TypeVar("T", bound="DumpImportTablesBody")


@_attrs_define
class DumpImportTablesBody:
    """
    Attributes:
        session_id (str):
        table (DumpImportTablesBodyTableType0 | Literal['assetTextBlobs'] | Literal['attachmentBlobs'] |
            Literal['docBodies']):
        rows (list[DumpImportTablesBodyRowsItem]):
    """

    session_id: str
    table: Literal["assetTextBlobs", "attachmentBlobs", "docBodies"] | DumpImportTablesBodyTableType0
    rows: list[DumpImportTablesBodyRowsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        table: Literal["assetTextBlobs", "attachmentBlobs", "docBodies"] | str
        if isinstance(self.table, str):
            table = self.table
        else:
            table = self.table

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sessionId": session_id,
                "table": table,
                "rows": rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dump_import_tables_body_rows_item import DumpImportTablesBodyRowsItem

        d = dict(src_dict)
        session_id = d.pop("sessionId")

        def _parse_table(
            data: object,
        ) -> Literal["assetTextBlobs", "attachmentBlobs", "docBodies"] | DumpImportTablesBodyTableType0:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                table_type_0 = check_dump_import_tables_body_table_type_0(data)

                return table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            table_type_1 = cast(Literal["docBodies"], data)
            if table_type_1 != "docBodies":
                raise ValueError(f"table_type_1 must match const 'docBodies', got '{table_type_1}'")
            return table_type_1
            table_type_2 = cast(Literal["attachmentBlobs"], data)
            if table_type_2 != "attachmentBlobs":
                raise ValueError(f"table_type_2 must match const 'attachmentBlobs', got '{table_type_2}'")
            return table_type_2
            table_type_3 = cast(Literal["assetTextBlobs"], data)
            if table_type_3 != "assetTextBlobs":
                raise ValueError(f"table_type_3 must match const 'assetTextBlobs', got '{table_type_3}'")
            return table_type_3

        table = _parse_table(d.pop("table"))

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = DumpImportTablesBodyRowsItem.from_dict(rows_item_data)

            rows.append(rows_item)

        dump_import_tables_body = cls(
            session_id=session_id,
            table=table,
            rows=rows,
        )

        dump_import_tables_body.additional_properties = d
        return dump_import_tables_body

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
