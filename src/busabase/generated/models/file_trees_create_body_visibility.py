from typing import Literal

FileTreesCreateBodyVisibility = Literal["private", "public", "workspace"]

FILE_TREES_CREATE_BODY_VISIBILITY_VALUES: set[FileTreesCreateBodyVisibility] = {
    "private",
    "public",
    "workspace",
}


def check_file_trees_create_body_visibility(value: str) -> FileTreesCreateBodyVisibility:
    if value in FILE_TREES_CREATE_BODY_VISIBILITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_TREES_CREATE_BODY_VISIBILITY_VALUES!r}")
