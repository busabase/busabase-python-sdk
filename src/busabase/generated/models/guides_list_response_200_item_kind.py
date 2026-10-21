from typing import Literal

GuidesListResponse200ItemKind = Literal["reference", "walkthrough"]

GUIDES_LIST_RESPONSE_200_ITEM_KIND_VALUES: set[GuidesListResponse200ItemKind] = {
    "reference",
    "walkthrough",
}


def check_guides_list_response_200_item_kind(value: str) -> GuidesListResponse200ItemKind:
    if value in GUIDES_LIST_RESPONSE_200_ITEM_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GUIDES_LIST_RESPONSE_200_ITEM_KIND_VALUES!r}")
