from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.embed_links_create_body_type import EmbedLinksCreateBodyType, check_embed_links_create_body_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embed_links_create_body_frame_policy_type_0 import EmbedLinksCreateBodyFramePolicyType0
    from ..models.embed_links_create_body_frame_policy_type_1 import EmbedLinksCreateBodyFramePolicyType1
    from ..models.embed_links_create_body_frame_policy_type_2 import EmbedLinksCreateBodyFramePolicyType2


T = TypeVar("T", bound="EmbedLinksCreateBody")


@_attrs_define
class EmbedLinksCreateBody:
    """
    Attributes:
        type_ (EmbedLinksCreateBodyType):
        type_id (str):
        expires_in_minutes (int | Unset):  Default: 15.
        frame_policy (EmbedLinksCreateBodyFramePolicyType0 | EmbedLinksCreateBodyFramePolicyType1 |
            EmbedLinksCreateBodyFramePolicyType2 | Unset): Defaults to `{"mode":"anywhere","allowedOrigins":[]}` when
            omitted.
    """

    type_: EmbedLinksCreateBodyType
    type_id: str
    expires_in_minutes: int | Unset = 15
    frame_policy: (
        EmbedLinksCreateBodyFramePolicyType0
        | EmbedLinksCreateBodyFramePolicyType1
        | EmbedLinksCreateBodyFramePolicyType2
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embed_links_create_body_frame_policy_type_0 import EmbedLinksCreateBodyFramePolicyType0
        from ..models.embed_links_create_body_frame_policy_type_1 import EmbedLinksCreateBodyFramePolicyType1

        type_: str = self.type_

        type_id = self.type_id

        expires_in_minutes = self.expires_in_minutes

        frame_policy: dict[str, Any] | Unset
        if isinstance(self.frame_policy, Unset):
            frame_policy = UNSET
        elif isinstance(self.frame_policy, EmbedLinksCreateBodyFramePolicyType0) or isinstance(
            self.frame_policy, EmbedLinksCreateBodyFramePolicyType1
        ):
            frame_policy = self.frame_policy.to_dict()
        else:
            frame_policy = self.frame_policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "typeId": type_id,
            }
        )
        if expires_in_minutes is not UNSET:
            field_dict["expiresInMinutes"] = expires_in_minutes
        if frame_policy is not UNSET:
            field_dict["framePolicy"] = frame_policy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.embed_links_create_body_frame_policy_type_0 import EmbedLinksCreateBodyFramePolicyType0
        from ..models.embed_links_create_body_frame_policy_type_1 import EmbedLinksCreateBodyFramePolicyType1
        from ..models.embed_links_create_body_frame_policy_type_2 import EmbedLinksCreateBodyFramePolicyType2

        d = dict(src_dict)
        type_ = check_embed_links_create_body_type(d.pop("type"))

        type_id = d.pop("typeId")

        expires_in_minutes = d.pop("expiresInMinutes", UNSET)

        def _parse_frame_policy(
            data: object,
        ) -> (
            EmbedLinksCreateBodyFramePolicyType0
            | EmbedLinksCreateBodyFramePolicyType1
            | EmbedLinksCreateBodyFramePolicyType2
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                frame_policy_type_0 = EmbedLinksCreateBodyFramePolicyType0.from_dict(data)

                return frame_policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                frame_policy_type_1 = EmbedLinksCreateBodyFramePolicyType1.from_dict(data)

                return frame_policy_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            frame_policy_type_2 = EmbedLinksCreateBodyFramePolicyType2.from_dict(data)

            return frame_policy_type_2

        frame_policy = _parse_frame_policy(d.pop("framePolicy", UNSET))

        embed_links_create_body = cls(
            type_=type_,
            type_id=type_id,
            expires_in_minutes=expires_in_minutes,
            frame_policy=frame_policy,
        )

        embed_links_create_body.additional_properties = d
        return embed_links_create_body

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
