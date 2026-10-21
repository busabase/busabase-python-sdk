from typing import Literal

ChangeRequestsReviewBodyVerdict = Literal["approved", "rejected"]

CHANGE_REQUESTS_REVIEW_BODY_VERDICT_VALUES: set[ChangeRequestsReviewBodyVerdict] = {
    "approved",
    "rejected",
}


def check_change_requests_review_body_verdict(value: str) -> ChangeRequestsReviewBodyVerdict:
    if value in CHANGE_REQUESTS_REVIEW_BODY_VERDICT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHANGE_REQUESTS_REVIEW_BODY_VERDICT_VALUES!r}")
