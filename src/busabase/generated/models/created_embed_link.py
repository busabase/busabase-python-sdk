from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.created_embed_link_node_type_type_0 import (
    CreatedEmbedLinkNodeTypeType0,
    check_created_embed_link_node_type_type_0,
)
from ..models.created_embed_link_type import CreatedEmbedLinkType, check_created_embed_link_type

if TYPE_CHECKING:
    from ..models.embed_frame_policy import EmbedFramePolicy


T = TypeVar("T", bound="CreatedEmbedLink")


@_attrs_define
class CreatedEmbedLink:
    """
    Attributes:
        id (str):
        type_ (CreatedEmbedLinkType):
        type_id (str):
        target_name (str):
        node_type (CreatedEmbedLinkNodeTypeType0 | None):
        created_at (datetime.datetime):
        expires_at (datetime.datetime):
        revoked_at (datetime.datetime | None):
        active (bool):
        frame_policy (EmbedFramePolicy):
        url (str):
        iframe_url (str):
    """

    id: str
    type_: CreatedEmbedLinkType
    type_id: str
    target_name: str
    node_type: CreatedEmbedLinkNodeTypeType0 | None
    created_at: datetime.datetime
    expires_at: datetime.datetime
    revoked_at: datetime.datetime | None
    active: bool
    frame_policy: EmbedFramePolicy
    url: str
    iframe_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        type_id = self.type_id

        target_name = self.target_name

        node_type: None | str
        if isinstance(self.node_type, str):
            node_type = self.node_type
        else:
            node_type = self.node_type

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        revoked_at: None | str
        if isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        active = self.active

        frame_policy = self.frame_policy.to_dict()

        url = self.url

        iframe_url = self.iframe_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "typeId": type_id,
                "targetName": target_name,
                "nodeType": node_type,
                "createdAt": created_at,
                "expiresAt": expires_at,
                "revokedAt": revoked_at,
                "active": active,
                "framePolicy": frame_policy,
                "url": url,
                "iframeUrl": iframe_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.embed_frame_policy import EmbedFramePolicy

        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_created_embed_link_type(d.pop("type"))

        type_id = d.pop("typeId")

        target_name = d.pop("targetName")

        def _parse_node_type(data: object) -> CreatedEmbedLinkNodeTypeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                node_type_type_0 = check_created_embed_link_node_type_type_0(data)

                return node_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatedEmbedLinkNodeTypeType0 | None, data)

        node_type = _parse_node_type(d.pop("nodeType"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expiresAt"))

        def _parse_revoked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)

                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        revoked_at = _parse_revoked_at(d.pop("revokedAt"))

        active = d.pop("active")

        frame_policy = EmbedFramePolicy.from_dict(d.pop("framePolicy"))

        url = d.pop("url")

        iframe_url = d.pop("iframeUrl")

        created_embed_link = cls(
            id=id,
            type_=type_,
            type_id=type_id,
            target_name=target_name,
            node_type=node_type,
            created_at=created_at,
            expires_at=expires_at,
            revoked_at=revoked_at,
            active=active,
            frame_policy=frame_policy,
            url=url,
            iframe_url=iframe_url,
        )

        created_embed_link.additional_properties = d
        return created_embed_link

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
