from typing import Literal

GrepPromptMatchField = Literal["body", "label"]

GREP_PROMPT_MATCH_FIELD_VALUES: set[GrepPromptMatchField] = {
    "body",
    "label",
}


def check_grep_prompt_match_field(value: str) -> GrepPromptMatchField:
    if value in GREP_PROMPT_MATCH_FIELD_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GREP_PROMPT_MATCH_FIELD_VALUES!r}")
