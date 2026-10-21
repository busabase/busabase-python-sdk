from typing import Literal

CommitTargetType = Literal["base", "node"]

COMMIT_TARGET_TYPE_VALUES: set[CommitTargetType] = {
    "base",
    "node",
}


def check_commit_target_type(value: str) -> CommitTargetType:
    if value in COMMIT_TARGET_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMIT_TARGET_TYPE_VALUES!r}")
