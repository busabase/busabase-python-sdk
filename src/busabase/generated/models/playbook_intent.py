from typing import Literal

PlaybookIntent = Literal["change", "read-only"]

PLAYBOOK_INTENT_VALUES: set[PlaybookIntent] = {
    "change",
    "read-only",
}


def check_playbook_intent(value: str) -> PlaybookIntent:
    if value in PLAYBOOK_INTENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOK_INTENT_VALUES!r}")
