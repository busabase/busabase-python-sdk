from typing import Literal

FileTreesCreateBodyMergeMode = Literal["merge", "replace"]

FILE_TREES_CREATE_BODY_MERGE_MODE_VALUES: set[FileTreesCreateBodyMergeMode] = {
    "merge",
    "replace",
}


def check_file_trees_create_body_merge_mode(value: str) -> FileTreesCreateBodyMergeMode:
    if value in FILE_TREES_CREATE_BODY_MERGE_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_TREES_CREATE_BODY_MERGE_MODE_VALUES!r}")
