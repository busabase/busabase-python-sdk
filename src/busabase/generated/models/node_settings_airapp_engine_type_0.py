from typing import Literal

NodeSettingsAirappEngineType0 = Literal["browser", "local", "remote"]

NODE_SETTINGS_AIRAPP_ENGINE_TYPE_0_VALUES: set[NodeSettingsAirappEngineType0] = {
    "browser",
    "local",
    "remote",
}


def check_node_settings_airapp_engine_type_0(value: str) -> NodeSettingsAirappEngineType0:
    if value in NODE_SETTINGS_AIRAPP_ENGINE_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NODE_SETTINGS_AIRAPP_ENGINE_TYPE_0_VALUES!r}")
