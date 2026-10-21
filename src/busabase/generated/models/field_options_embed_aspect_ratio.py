from typing import Literal

FieldOptionsEmbedAspectRatio = Literal["16:9", "1:1", "4:3"]

FIELD_OPTIONS_EMBED_ASPECT_RATIO_VALUES: set[FieldOptionsEmbedAspectRatio] = {
    "16:9",
    "1:1",
    "4:3",
}


def check_field_options_embed_aspect_ratio(value: str) -> FieldOptionsEmbedAspectRatio:
    if value in FIELD_OPTIONS_EMBED_ASPECT_RATIO_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FIELD_OPTIONS_EMBED_ASPECT_RATIO_VALUES!r}")
