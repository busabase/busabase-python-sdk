from typing import Literal

FileTreesListFilesType = Literal["airapp", "drive", "skill"]

FILE_TREES_LIST_FILES_TYPE_VALUES: set[FileTreesListFilesType] = {
    "airapp",
    "drive",
    "skill",
}


def check_file_trees_list_files_type(value: str) -> FileTreesListFilesType:
    if value in FILE_TREES_LIST_FILES_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILE_TREES_LIST_FILES_TYPE_VALUES!r}")
