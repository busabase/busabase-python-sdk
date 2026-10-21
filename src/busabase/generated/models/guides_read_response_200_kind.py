from typing import Literal

GuidesReadResponse200Kind = Literal["reference", "walkthrough"]

GUIDES_READ_RESPONSE_200_KIND_VALUES: set[GuidesReadResponse200Kind] = {
    "reference",
    "walkthrough",
}


def check_guides_read_response_200_kind(value: str) -> GuidesReadResponse200Kind:
    if value in GUIDES_READ_RESPONSE_200_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GUIDES_READ_RESPONSE_200_KIND_VALUES!r}")
