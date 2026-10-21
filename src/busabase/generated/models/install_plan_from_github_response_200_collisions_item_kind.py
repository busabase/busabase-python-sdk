from typing import Literal

InstallPlanFromGithubResponse200CollisionsItemKind = Literal["base", "node"]

INSTALL_PLAN_FROM_GITHUB_RESPONSE_200_COLLISIONS_ITEM_KIND_VALUES: set[
    InstallPlanFromGithubResponse200CollisionsItemKind
] = {
    "base",
    "node",
}


def check_install_plan_from_github_response_200_collisions_item_kind(
    value: str,
) -> InstallPlanFromGithubResponse200CollisionsItemKind:
    if value in INSTALL_PLAN_FROM_GITHUB_RESPONSE_200_COLLISIONS_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INSTALL_PLAN_FROM_GITHUB_RESPONSE_200_COLLISIONS_ITEM_KIND_VALUES!r}"
    )
