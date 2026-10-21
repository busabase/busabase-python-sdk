from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SystemMetaResponse200")


@_attrs_define
class SystemMetaResponse200:
    """
    Attributes:
        service (str):
        version (str):
        timestamp (float):
    """

    service: str
    version: str
    timestamp: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service = self.service

        version = self.version

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "service": service,
                "version": version,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service = d.pop("service")

        version = d.pop("version")

        timestamp = d.pop("timestamp")

        system_meta_response_200 = cls(
            service=service,
            version=version,
            timestamp=timestamp,
        )

        system_meta_response_200.additional_properties = d
        return system_meta_response_200

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
