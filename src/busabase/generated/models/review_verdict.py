from typing import Literal

ReviewVerdict = Literal["approved", "rejected"]

REVIEW_VERDICT_VALUES: set[ReviewVerdict] = {
    "approved",
    "rejected",
}


def check_review_verdict(value: str) -> ReviewVerdict:
    if value in REVIEW_VERDICT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REVIEW_VERDICT_VALUES!r}")
