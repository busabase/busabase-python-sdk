from typing import Literal

ViewConfigCardSize = Literal["large", "medium", "small"]

VIEW_CONFIG_CARD_SIZE_VALUES: set[ViewConfigCardSize] = {
    "large",
    "medium",
    "small",
}


def check_view_config_card_size(value: str) -> ViewConfigCardSize:
    if value in VIEW_CONFIG_CARD_SIZE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VIEW_CONFIG_CARD_SIZE_VALUES!r}")
