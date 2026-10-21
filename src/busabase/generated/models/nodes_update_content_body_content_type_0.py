from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NodesUpdateContentBodyContentType0")


@_attrs_define
class NodesUpdateContentBodyContentType0:
    """
    Attributes:
        kind (Literal['doc']):
        body (str):
    """

    kind: Literal["doc"]
    body: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = cast(Literal["doc"], d.pop("kind"))
        if kind != "doc":
            raise ValueError(f"kind must match const 'doc', got '{kind}'")

        body = d.pop("body")

        nodes_update_content_body_content_type_0 = cls(
            kind=kind,
            body=body,
        )

        nodes_update_content_body_content_type_0.additional_properties = d
        return nodes_update_content_body_content_type_0

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
