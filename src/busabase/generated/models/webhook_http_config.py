from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_http_config_headers import WebhookHttpConfigHeaders


T = TypeVar("T", bound="WebhookHttpConfig")


@_attrs_define
class WebhookHttpConfig:
    """
    Attributes:
        target_url (str):
        has_secret (bool):
        headers (WebhookHttpConfigHeaders | Unset):
    """

    target_url: str
    has_secret: bool
    headers: WebhookHttpConfigHeaders | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_url = self.target_url

        has_secret = self.has_secret

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetUrl": target_url,
                "hasSecret": has_secret,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_http_config_headers import WebhookHttpConfigHeaders

        d = dict(src_dict)
        target_url = d.pop("targetUrl")

        has_secret = d.pop("hasSecret")

        _headers = d.pop("headers", UNSET)
        headers: WebhookHttpConfigHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = WebhookHttpConfigHeaders.from_dict(_headers)

        webhook_http_config = cls(
            target_url=target_url,
            has_secret=has_secret,
            headers=headers,
        )

        webhook_http_config.additional_properties = d
        return webhook_http_config

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
