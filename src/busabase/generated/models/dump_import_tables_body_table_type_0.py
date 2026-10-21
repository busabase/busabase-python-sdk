from typing import Literal

DumpImportTablesBodyTableType0 = Literal[
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

DUMP_IMPORT_TABLES_BODY_TABLE_TYPE_0_VALUES: set[DumpImportTablesBodyTableType0] = {
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


def check_dump_import_tables_body_table_type_0(value: str) -> DumpImportTablesBodyTableType0:
    if value in DUMP_IMPORT_TABLES_BODY_TABLE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUMP_IMPORT_TABLES_BODY_TABLE_TYPE_0_VALUES!r}")
