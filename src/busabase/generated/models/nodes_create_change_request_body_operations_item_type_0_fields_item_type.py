from typing import Literal

NodesCreateChangeRequestBodyOperationsItemType0FieldsItemType = Literal[
    "ai_summary",
    "ai_tags",
    "attachment",
    "auto_number",
    "checkbox",
    "code",
    "created_by",
    "created_time",
    "date",
    "email",
    "embed",
    "formula",
    "html",
    "json",
    "longtext",
    "lookup",
    "markdown",
    "member",
    "multiselect",
    "number",
    "phone",
    "relation",
    "select",
    "text",
    "updated_by",
    "updated_time",
    "url",
    "whiteboard",
    "yaml",
]

NODES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_0_FIELDS_ITEM_TYPE_VALUES: set[
    NodesCreateChangeRequestBodyOperationsItemType0FieldsItemType
] = {
    "ai_summary",
    "ai_tags",
    "attachment",
    "auto_number",
    "checkbox",
    "code",
    "created_by",
    "created_time",
    "date",
    "email",
    "embed",
    "formula",
    "html",
    "json",
    "longtext",
    "lookup",
    "markdown",
    "member",
    "multiselect",
    "number",
    "phone",
    "relation",
    "select",
    "text",
    "updated_by",
    "updated_time",
    "url",
    "whiteboard",
    "yaml",
}


def check_nodes_create_change_request_body_operations_item_type_0_fields_item_type(
    value: str,
) -> NodesCreateChangeRequestBodyOperationsItemType0FieldsItemType:
    if value in NODES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_0_FIELDS_ITEM_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NODES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_0_FIELDS_ITEM_TYPE_VALUES!r}"
    )
