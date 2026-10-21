from typing import Literal

BasesFieldChangeRequestBodyPatchOptionsEmbedAspectRatio = Literal["16:9", "1:1", "4:3"]

BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_EMBED_ASPECT_RATIO_VALUES: set[
    BasesFieldChangeRequestBodyPatchOptionsEmbedAspectRatio
] = {
    "16:9",
    "1:1",
    "4:3",
}


def check_bases_field_change_request_body_patch_options_embed_aspect_ratio(
    value: str,
) -> BasesFieldChangeRequestBodyPatchOptionsEmbedAspectRatio:
    if value in BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_EMBED_ASPECT_RATIO_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BASES_FIELD_CHANGE_REQUEST_BODY_PATCH_OPTIONS_EMBED_ASPECT_RATIO_VALUES!r}"
    )
