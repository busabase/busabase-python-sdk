from typing import Literal

FileTreesReadFileType = Literal["airapp", "drive", "skill"]

FILE_TREES_READ_FILE_TYPE_VALUES: set[FileTreesReadFileType] = {
    "airapp",
    "drive",
    "skill",
}


def check_file_trees_read_file_type(value: str) -> FileTreesReadFileType:
    if value in FILE_TREES_READ_FILE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_TREES_READ_FILE_TYPE_VALUES!r}")
