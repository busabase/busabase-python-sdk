from typing import Literal

PlaybooksGetKind = Literal["prompt", "skill"]

PLAYBOOKS_GET_KIND_VALUES: set[PlaybooksGetKind] = {
    "prompt",
    "skill",
}


def check_playbooks_get_kind(value: str) -> PlaybooksGetKind:
    if value in PLAYBOOKS_GET_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOKS_GET_KIND_VALUES!r}")
