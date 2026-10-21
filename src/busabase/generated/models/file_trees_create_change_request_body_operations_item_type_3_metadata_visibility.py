from typing import Literal

FileTreesCreateChangeRequestBodyOperationsItemType3MetadataVisibility = Literal["private", "public", "workspace"]

FILE_TREES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_3_METADATA_VISIBILITY_VALUES: set[
    FileTreesCreateChangeRequestBodyOperationsItemType3MetadataVisibility
] = {
    "private",
    "public",
    "workspace",
}


def check_file_trees_create_change_request_body_operations_item_type_3_metadata_visibility(
    value: str,
) -> FileTreesCreateChangeRequestBodyOperationsItemType3MetadataVisibility:
    if value in FILE_TREES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_3_METADATA_VISIBILITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FILE_TREES_CREATE_CHANGE_REQUEST_BODY_OPERATIONS_ITEM_TYPE_3_METADATA_VISIBILITY_VALUES!r}"
    )
