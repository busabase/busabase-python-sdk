from typing import Literal

TextFileOperationKind = Literal["create", "update"]

TEXT_FILE_OPERATION_KIND_VALUES: set[TextFileOperationKind] = {
    "create",
    "update",
}


def check_text_file_operation_kind(value: str) -> TextFileOperationKind:
    if value in TEXT_FILE_OPERATION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEXT_FILE_OPERATION_KIND_VALUES!r}")
