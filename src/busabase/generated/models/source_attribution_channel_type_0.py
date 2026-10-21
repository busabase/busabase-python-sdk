from typing import Literal

SourceAttributionChannelType0 = Literal[
    "automation", "browser", "cli", "import", "mcp", "openapi", "sdk", "skill", "web_ui", "webhook"
]

SOURCE_ATTRIBUTION_CHANNEL_TYPE_0_VALUES: set[SourceAttributionChannelType0] = {
    "automation",
    "browser",
    "cli",
    "import",
    "mcp",
    "openapi",
    "sdk",
    "skill",
    "web_ui",
    "webhook",
}


def check_source_attribution_channel_type_0(value: str) -> SourceAttributionChannelType0:
    if value in SOURCE_ATTRIBUTION_CHANNEL_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SOURCE_ATTRIBUTION_CHANNEL_TYPE_0_VALUES!r}")
