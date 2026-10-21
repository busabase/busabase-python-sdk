from typing import Literal

AirAppNodeDetailVisibility = Literal["private", "public", "workspace"]

AIR_APP_NODE_DETAIL_VISIBILITY_VALUES: set[AirAppNodeDetailVisibility] = {
    "private",
    "public",
    "workspace",
}


def check_air_app_node_detail_visibility(value: str) -> AirAppNodeDetailVisibility:
    if value in AIR_APP_NODE_DETAIL_VISIBILITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AIR_APP_NODE_DETAIL_VISIBILITY_VALUES!r}")
