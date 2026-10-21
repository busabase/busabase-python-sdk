from typing import Literal

FileTreeMetadataOperationMetadataVisibility = Literal["private", "public", "workspace"]

FILE_TREE_METADATA_OPERATION_METADATA_VISIBILITY_VALUES: set[FileTreeMetadataOperationMetadataVisibility] = {
    "private",
    "public",
    "workspace",
}


def check_file_tree_metadata_operation_metadata_visibility(value: str) -> FileTreeMetadataOperationMetadataVisibility:
    if value in FILE_TREE_METADATA_OPERATION_METADATA_VISIBILITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FILE_TREE_METADATA_OPERATION_METADATA_VISIBILITY_VALUES!r}"
    )
