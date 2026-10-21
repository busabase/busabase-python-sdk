from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_icon_attachment_crop import NodeIconAttachmentCrop


T = TypeVar("T", bound="NodeIconAttachment")


@_attrs_define
class NodeIconAttachment:
    """
    Attributes:
        type_ (Literal['attachment']):
        url (str):
        attachment_id (str):
        original_url (str | Unset):
        original_attachment_id (str | Unset):
        crop (NodeIconAttachmentCrop | Unset):
    """

    type_: Literal["attachment"]
    url: str
    attachment_id: str
    original_url: str | Unset = UNSET
    original_attachment_id: str | Unset = UNSET
    crop: NodeIconAttachmentCrop | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        url = self.url

        attachment_id = self.attachment_id

        original_url = self.original_url

        original_attachment_id = self.original_attachment_id

        crop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.crop, Unset):
            crop = self.crop.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "url": url,
                "attachmentId": attachment_id,
            }
        )
        if original_url is not UNSET:
            field_dict["originalUrl"] = original_url
        if original_attachment_id is not UNSET:
            field_dict["originalAttachmentId"] = original_attachment_id
        if crop is not UNSET:
            field_dict["crop"] = crop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.node_icon_attachment_crop import NodeIconAttachmentCrop

        d = dict(src_dict)
        type_ = cast(Literal["attachment"], d.pop("type"))
        if type_ != "attachment":
            raise ValueError(f"type must match const 'attachment', got '{type_}'")

        url = d.pop("url")

        attachment_id = d.pop("attachmentId")

        original_url = d.pop("originalUrl", UNSET)

        original_attachment_id = d.pop("originalAttachmentId", UNSET)

        _crop = d.pop("crop", UNSET)
        crop: NodeIconAttachmentCrop | Unset
        if isinstance(_crop, Unset):
            crop = UNSET
        else:
            crop = NodeIconAttachmentCrop.from_dict(_crop)

        node_icon_attachment = cls(
            type_=type_,
            url=url,
            attachment_id=attachment_id,
            original_url=original_url,
            original_attachment_id=original_attachment_id,
            crop=crop,
        )

        node_icon_attachment.additional_properties = d
        return node_icon_attachment

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
