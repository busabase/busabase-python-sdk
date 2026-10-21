from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhooks_create_body_type_1_config_headers import WebhooksCreateBodyType1ConfigHeaders


T = TypeVar("T", bound="WebhooksCreateBodyType1Config")


@_attrs_define
class WebhooksCreateBodyType1Config:
    """
    Attributes:
        target_url (str):
        secret (str | Unset):
        headers (WebhooksCreateBodyType1ConfigHeaders | Unset):
    """

    target_url: str
    secret: str | Unset = UNSET
    headers: WebhooksCreateBodyType1ConfigHeaders | Unset = UNSET
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
        from ..models.webhooks_create_body_type_1_config_headers import WebhooksCreateBodyType1ConfigHeaders

        d = dict(src_dict)
        target_url = d.pop("targetUrl")

        secret = d.pop("secret", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: WebhooksCreateBodyType1ConfigHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = WebhooksCreateBodyType1ConfigHeaders.from_dict(_headers)

        webhooks_create_body_type_1_config = cls(
            target_url=target_url,
            secret=secret,
            headers=headers,
        )

        webhooks_create_body_type_1_config.additional_properties = d
        return webhooks_create_body_type_1_config

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
