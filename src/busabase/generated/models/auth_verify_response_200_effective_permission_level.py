from typing import Literal

AuthVerifyResponse200EffectivePermissionLevel = Literal["changeRequest", "manage", "read", "write"]

AUTH_VERIFY_RESPONSE_200_EFFECTIVE_PERMISSION_LEVEL_VALUES: set[AuthVerifyResponse200EffectivePermissionLevel] = {
    "changeRequest",
    "manage",
    "read",
    "write",
}


def check_auth_verify_response_200_effective_permission_level(
    value: str,
) -> AuthVerifyResponse200EffectivePermissionLevel:
    if value in AUTH_VERIFY_RESPONSE_200_EFFECTIVE_PERMISSION_LEVEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUTH_VERIFY_RESPONSE_200_EFFECTIVE_PERMISSION_LEVEL_VALUES!r}"
    )
