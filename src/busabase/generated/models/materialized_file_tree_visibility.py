from typing import Literal

MaterializedFileTreeVisibility = Literal["private", "public", "workspace"]

MATERIALIZED_FILE_TREE_VISIBILITY_VALUES: set[MaterializedFileTreeVisibility] = {
    "private",
    "public",
    "workspace",
}


def check_materialized_file_tree_visibility(value: str) -> MaterializedFileTreeVisibility:
    if value in MATERIALIZED_FILE_TREE_VISIBILITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATERIALIZED_FILE_TREE_VISIBILITY_VALUES!r}")
