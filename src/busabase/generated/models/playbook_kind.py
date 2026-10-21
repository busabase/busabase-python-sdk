from typing import Literal

PlaybookKind = Literal["prompt", "skill"]

PLAYBOOK_KIND_VALUES: set[PlaybookKind] = {
    "prompt",
    "skill",
}


def check_playbook_kind(value: str) -> PlaybookKind:
    if value in PLAYBOOK_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOK_KIND_VALUES!r}")
