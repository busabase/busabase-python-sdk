from typing import Literal

FileTreesCreateChangeRequestBodyType = Literal["airapp", "drive", "skill"]

FILE_TREES_CREATE_CHANGE_REQUEST_BODY_TYPE_VALUES: set[FileTreesCreateChangeRequestBodyType] = {
    "airapp",
    "drive",
    "skill",
}


def check_file_trees_create_change_request_body_type(value: str) -> FileTreesCreateChangeRequestBodyType:
    if value in FILE_TREES_CREATE_CHANGE_REQUEST_BODY_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FILE_TREES_CREATE_CHANGE_REQUEST_BODY_TYPE_VALUES!r}"
    )
