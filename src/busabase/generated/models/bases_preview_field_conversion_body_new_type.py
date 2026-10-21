from typing import Literal

BasesPreviewFieldConversionBodyNewType = Literal[
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

BASES_PREVIEW_FIELD_CONVERSION_BODY_NEW_TYPE_VALUES: set[BasesPreviewFieldConversionBodyNewType] = {
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


def check_bases_preview_field_conversion_body_new_type(value: str) -> BasesPreviewFieldConversionBodyNewType:
    if value in BASES_PREVIEW_FIELD_CONVERSION_BODY_NEW_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASES_PREVIEW_FIELD_CONVERSION_BODY_NEW_TYPE_VALUES!r}"
    )
