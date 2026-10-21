from typing import Literal

PlaybookAttributionKind = Literal["prompt", "skill"]

PLAYBOOK_ATTRIBUTION_KIND_VALUES: set[PlaybookAttributionKind] = {
    "prompt",
    "skill",
}


def check_playbook_attribution_kind(value: str) -> PlaybookAttributionKind:
    if value in PLAYBOOK_ATTRIBUTION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAYBOOK_ATTRIBUTION_KIND_VALUES!r}")
