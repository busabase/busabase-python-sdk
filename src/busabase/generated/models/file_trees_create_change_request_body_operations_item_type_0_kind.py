from typing import Literal

FileTreesCreateChangeRequestBodyOperationsItemType0Kind = Literal["create", "update"]

FILE_TREES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_0_KIND_VALUES: set[
    FileTreesCreateChangeRequestBodyOperationsItemType0Kind
] = {
    "create",
    "update",
}


def check_file_trees_create_change_request_body_operations_item_type_0_kind(
    value: str,
) -> FileTreesCreateChangeRequestBodyOperationsItemType0Kind:
    if value in FILE_TREES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_0_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FILE_TREES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_0_KIND_VALUES!r}"
    )
