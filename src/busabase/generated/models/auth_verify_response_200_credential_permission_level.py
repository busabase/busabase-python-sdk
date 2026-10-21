from typing import Literal

AuthVerifyResponse200CredentialPermissionLevel = Literal["changeRequest", "manage", "read", "write"]

AUTH_VERIFY_RESPONSE_200_CREDENTIAL_PERMISSION_LEVEL_VALUES: set[AuthVerifyResponse200CredentialPermissionLevel] = {
    "changeRequest",
    "manage",
    "read",
    "write",
}


def check_auth_verify_response_200_credential_permission_level(
    value: str,
) -> AuthVerifyResponse200CredentialPermissionLevel:
    if value in AUTH_VERIFY_RESPONSE_200_CREDENTIAL_PERMISSION_LEVEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUTH_VERIFY_RESPONSE_200_CREDENTIAL_PERMISSION_LEVEL_VALUES!r}"
    )
