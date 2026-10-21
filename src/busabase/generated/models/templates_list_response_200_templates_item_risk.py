from typing import Literal

TemplatesListResponse200TemplatesItemRisk = Literal["gated-write", "local-write", "read-only", "sandbox"]

TEMPLATES_LIST_RESPONSE_200_TEMPLATES_ITEM_RISK_VALUES: set[TemplatesListResponse200TemplatesItemRisk] = {
    "gated-write",
    "local-write",
    "read-only",
    "sandbox",
}


def check_templates_list_response_200_templates_item_risk(value: str) -> TemplatesListResponse200TemplatesItemRisk:
    if value in TEMPLATES_LIST_RESPONSE_200_TEMPLATES_ITEM_RISK_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TEMPLATES_LIST_RESPONSE_200_TEMPLATES_ITEM_RISK_VALUES!r}"
    )
