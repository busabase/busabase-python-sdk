from typing import Literal

VaultItemEnvironment = Literal["development", "local", "production", "staging"]

VAULT_ITEM_ENVIRONMENT_VALUES: set[VaultItemEnvironment] = {
    "development",
    "local",
    "production",
    "staging",
}


def check_vault_item_environment(value: str) -> VaultItemEnvironment:
    if value in VAULT_ITEM_ENVIRONMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VAULT_ITEM_ENVIRONMENT_VALUES!r}")
