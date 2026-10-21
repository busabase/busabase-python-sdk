from typing import Literal

InstallPlanFromGithubResponse200NodesItemType = Literal["airapp", "base", "doc", "drive", "file", "folder", "skill"]

INSTALL_PLAN_FROM_GITHUB_RESPONSE_200_NODES_ITEM_TYPE_VALUES: set[InstallPlanFromGithubResponse200NodesItemType] = {
    "airapp",
    "base",
    "doc",
    "drive",
    "file",
    "folder",
    "skill",
}


def check_install_plan_from_github_response_200_nodes_item_type(
    value: str,
) -> InstallPlanFromGithubResponse200NodesItemType:
    if value in INSTALL_PLAN_FROM_GITHUB_RESPONSE_200_NODES_ITEM_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INSTALL_PLAN_FROM_GITHUB_RESPONSE_200_NODES_ITEM_TYPE_VALUES!r}"
    )
