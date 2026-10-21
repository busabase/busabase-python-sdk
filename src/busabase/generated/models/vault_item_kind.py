from typing import Literal

VaultItemKind = Literal["secret", "variable"]

VAULT_ITEM_KIND_VALUES: set[VaultItemKind] = {
    "secret",
    "variable",
}


def check_vault_item_kind(value: str) -> VaultItemKind:
    if value in VAULT_ITEM_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VAULT_ITEM_KIND_VALUES!r}")
