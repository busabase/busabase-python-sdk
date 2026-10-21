from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assets_edit_content_body_edits_item import AssetsEditContentBodyEditsItem


T = TypeVar("T", bound="AssetsEditContentBody")


@_attrs_define
class AssetsEditContentBody:
    """
    Attributes:
        edits (list[AssetsEditContentBodyEditsItem]):
        message (str | Unset): Explanation shown to the human reviewer. Write a conventional-commit style subject —
            imperative verb + what + why, e.g. "Fix typo in setup instructions". Default: 'Edit file content'.
        submitted_by (str | Unset):  Default: 'agent'.
        auto_merge (bool | Unset): Whether to approve and merge this change immediately. Omitted defaults to merging
            immediately if the actor has write access on the target node, otherwise falling back to a pending Change
            Request; pass explicit false to force review even with write access. This rewrites the real mounted file bytes;
            the previous content stays in the Change Request history, so it is recoverable but not one-click undoable.
    """

    edits: list[AssetsEditContentBodyEditsItem]
    message: str | Unset = "Edit file content"
    submitted_by: str | Unset = "agent"
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edits = []
        for edits_item_data in self.edits:
            edits_item = edits_item_data.to_dict()
            edits.append(edits_item)

        message = self.message

        submitted_by = self.submitted_by

        auto_merge = self.auto_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edits": edits,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if submitted_by is not UNSET:
            field_dict["submittedBy"] = submitted_by
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assets_edit_content_body_edits_item import AssetsEditContentBodyEditsItem

        d = dict(src_dict)
        edits = []
        _edits = d.pop("edits")
        for edits_item_data in _edits:
            edits_item = AssetsEditContentBodyEditsItem.from_dict(edits_item_data)

            edits.append(edits_item)

        message = d.pop("message", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        assets_edit_content_body = cls(
            edits=edits,
            message=message,
            submitted_by=submitted_by,
            auto_merge=auto_merge,
        )

        assets_edit_content_body.additional_properties = d
        return assets_edit_content_body

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
