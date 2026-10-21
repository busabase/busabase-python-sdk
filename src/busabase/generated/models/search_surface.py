from typing import Literal

SearchSurface = Literal["advanced", "quick"]

SEARCH_SURFACE_VALUES: set[SearchSurface] = {
    "advanced",
    "quick",
}


def check_search_surface(value: str) -> SearchSurface:
    if value in SEARCH_SURFACE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEARCH_SURFACE_VALUES!r}")
