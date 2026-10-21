from typing import Literal

ViewConfigSortsItemDirection = Literal["asc", "desc"]

VIEW_CONFIG_SORTS_ITEM_DIRECTION_VALUES: set[ViewConfigSortsItemDirection] = {
    "asc",
    "desc",
}


def check_view_config_sorts_item_direction(value: str) -> ViewConfigSortsItemDirection:
    if value in VIEW_CONFIG_SORTS_ITEM_DIRECTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VIEW_CONFIG_SORTS_ITEM_DIRECTION_VALUES!r}")
