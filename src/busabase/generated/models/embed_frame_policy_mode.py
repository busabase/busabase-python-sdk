from typing import Literal

EmbedFramePolicyMode = Literal["anywhere", "origins", "top-level-only"]

EMBED_FRAME_POLICY_MODE_VALUES: set[EmbedFramePolicyMode] = {
    "anywhere",
    "origins",
    "top-level-only",
}


def check_embed_frame_policy_mode(value: str) -> EmbedFramePolicyMode:
    if value in EMBED_FRAME_POLICY_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EMBED_FRAME_POLICY_MODE_VALUES!r}")
