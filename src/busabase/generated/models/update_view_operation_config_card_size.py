from typing import Literal

UpdateViewOperationConfigCardSize = Literal["large", "medium", "small"]

UPDATE_VIEW_OPERATION_CONFIG_CARD_SIZE_VALUES: set[UpdateViewOperationConfigCardSize] = {
    "large",
    "medium",
    "small",
}


def check_update_view_operation_config_card_size(value: str) -> UpdateViewOperationConfigCardSize:
    if value in UPDATE_VIEW_OPERATION_CONFIG_CARD_SIZE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_VIEW_OPERATION_CONFIG_CARD_SIZE_VALUES!r}")
