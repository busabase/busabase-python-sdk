from typing import Literal

FileTreesReadFileResponse200Encoding = Literal["url", "utf8"]

FILE_TREES_READ_FILE_RESPONSE_200_ENCODING_VALUES: set[FileTreesReadFileResponse200Encoding] = {
    "url",
    "utf8",
}


def check_file_trees_read_file_response_200_encoding(value: str) -> FileTreesReadFileResponse200Encoding:
    if value in FILE_TREES_READ_FILE_RESPONSE_200_ENCODING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FILE_TREES_READ_FILE_RESPONSE_200_ENCODING_VALUES!r}"
    )
