from typing import Literal

VaultItemScopeType = Literal["agent", "api_key", "base", "personal", "tool", "workspace"]

VAULT_ITEM_SCOPE_TYPE_VALUES: set[VaultItemScopeType] = {
    "agent",
    "api_key",
    "base",
    "personal",
    "tool",
    "workspace",
}


def check_vault_item_scope_type(value: str) -> VaultItemScopeType:
    if value in VAULT_ITEM_SCOPE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VAULT_ITEM_SCOPE_TYPE_VALUES!r}")
