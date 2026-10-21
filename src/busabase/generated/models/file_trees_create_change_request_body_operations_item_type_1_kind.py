from typing import Literal

FileTreesCreateChangeRequestBodyOperationsItemType1Kind = Literal["create", "update"]

FILE_TREES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_1_KIND_VALUES: set[
    FileTreesCreateChangeRequestBodyOperationsItemType1Kind
] = {
    "create",
    "update",
}


def check_file_trees_create_change_request_body_operations_item_type_1_kind(
    value: str,
) -> FileTreesCreateChangeRequestBodyOperationsItemType1Kind:
    if value in FILE_TREES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_1_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FILE_TREES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_1_KIND_VALUES!r}"
    )
