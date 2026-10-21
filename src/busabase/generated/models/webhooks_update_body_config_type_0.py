from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhooks_update_body_config_type_0_headers import WebhooksUpdateBodyConfigType0Headers


T = TypeVar("T", bound="WebhooksUpdateBodyConfigType0")


@_attrs_define
class WebhooksUpdateBodyConfigType0:
    """
    Attributes:
        target_url (str):
        secret (str | Unset):
        headers (WebhooksUpdateBodyConfigType0Headers | Unset):
    """

    target_url: str
    secret: str | Unset = UNSET
    headers: WebhooksUpdateBodyConfigType0Headers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_url = self.target_url

        secret = self.secret

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetUrl": target_url,
            }
        )
        if secret is not UNSET:
            field_dict["secret"] = secret
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhooks_update_body_config_type_0_headers import WebhooksUpdateBodyConfigType0Headers

        d = dict(src_dict)
        target_url = d.pop("targetUrl")

        secret = d.pop("secret", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: WebhooksUpdateBodyConfigType0Headers | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = WebhooksUpdateBodyConfigType0Headers.from_dict(_headers)

        webhooks_update_body_config_type_0 = cls(
            target_url=target_url,
            secret=secret,
            headers=headers,
        )

        webhooks_update_body_config_type_0.additional_properties = d
        return webhooks_update_body_config_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
