from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VaultItemAccess")


@_attrs_define
class VaultItemAccess:
    """
    Attributes:
        runtime (bool | Unset):  Default: True.
        reveal (bool | Unset):  Default: True.
        edit (bool | Unset):  Default: True.
        share (bool | Unset):  Default: False.
    """

    runtime: bool | Unset = True
    reveal: bool | Unset = True
    edit: bool | Unset = True
    share: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runtime = self.runtime

        reveal = self.reveal

        edit = self.edit

        share = self.share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if reveal is not UNSET:
            field_dict["reveal"] = reveal
        if edit is not UNSET:
            field_dict["edit"] = edit
        if share is not UNSET:
            field_dict["share"] = share

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        runtime = d.pop("runtime", UNSET)

        reveal = d.pop("reveal", UNSET)

        edit = d.pop("edit", UNSET)

        share = d.pop("share", UNSET)

        vault_item_access = cls(
            runtime=runtime,
            reveal=reveal,
            edit=edit,
            share=share,
        )

        vault_item_access.additional_properties = d
        return vault_item_access

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
