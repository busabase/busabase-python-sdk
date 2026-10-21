from typing import Literal

DumpExportTablesBodyTable = Literal[
    "assets",
    "assetTexts",
    "assetUsages",
    "attachments",
    "auditEvents",
    "baseFields",
    "bases",
    "changeRequests",
    "comments",
    "commits",
    "fieldValues",
    "nodePrincipals",
    "nodes",
    "operations",
    "recordLinks",
    "records",
    "reviews",
    "views",
]

DUMP_EXPORT_TABLES_BODY_TABLE_VALUES: set[DumpExportTablesBodyTable] = {
    "assets",
    "assetTexts",
    "assetUsages",
    "attachments",
    "auditEvents",
    "baseFields",
    "bases",
    "changeRequests",
    "comments",
    "commits",
    "fieldValues",
    "nodePrincipals",
    "nodes",
    "operations",
    "recordLinks",
    "records",
    "reviews",
    "views",
}


def check_dump_export_tables_body_table(value: str) -> DumpExportTablesBodyTable:
    if value in DUMP_EXPORT_TABLES_BODY_TABLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUMP_EXPORT_TABLES_BODY_TABLE_VALUES!r}")
