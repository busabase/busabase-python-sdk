from typing import Literal

FileTreesCreateBodyType = Literal["airapp", "drive", "skill"]

FILE_TREES_CREATE_BODY_TYPE_VALUES: set[FileTreesCreateBodyType] = {
    "airapp",
    "drive",
    "skill",
}


def check_file_trees_create_body_type(value: str) -> FileTreesCreateBodyType:
    if value in FILE_TREES_CREATE_BODY_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_TREES_CREATE_BODY_TYPE_VALUES!r}")
