from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_attribution_channel_type_0 import (
    SourceAttributionChannelType0,
    check_source_attribution_channel_type_0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.playbook_attribution import PlaybookAttribution


T = TypeVar("T", bound="SourceAttribution")


@_attrs_define
class SourceAttribution:
    """
    Attributes:
        display_name (None | str):
        owner_name (None | str):
        channel (None | SourceAttributionChannelType0):
        playbook (None | PlaybookAttribution | Unset):
    """

    display_name: None | str
    owner_name: None | str
    channel: None | SourceAttributionChannelType0
    playbook: None | PlaybookAttribution | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.playbook_attribution import PlaybookAttribution

        display_name: None | str
        display_name = self.display_name

        owner_name: None | str
        owner_name = self.owner_name

        channel: None | str
        if isinstance(self.channel, str):
            channel = self.channel
        else:
            channel = self.channel

        playbook: dict[str, Any] | None | Unset
        if isinstance(self.playbook, Unset):
            playbook = UNSET
        elif isinstance(self.playbook, PlaybookAttribution):
            playbook = self.playbook.to_dict()
        else:
            playbook = self.playbook

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "ownerName": owner_name,
                "channel": channel,
            }
        )
        if playbook is not UNSET:
            field_dict["playbook"] = playbook

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.playbook_attribution import PlaybookAttribution

        d = dict(src_dict)

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("displayName"))

        def _parse_owner_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        owner_name = _parse_owner_name(d.pop("ownerName"))

        def _parse_channel(data: object) -> None | SourceAttributionChannelType0:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                channel_type_0 = check_source_attribution_channel_type_0(data)

                return channel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceAttributionChannelType0, data)

        channel = _parse_channel(d.pop("channel"))

        def _parse_playbook(data: object) -> None | PlaybookAttribution | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                playbook_type_0 = PlaybookAttribution.from_dict(data)

                return playbook_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlaybookAttribution | Unset, data)

        playbook = _parse_playbook(d.pop("playbook", UNSET))

        source_attribution = cls(
            display_name=display_name,
            owner_name=owner_name,
            channel=channel,
            playbook=playbook,
        )

        source_attribution.additional_properties = d
        return source_attribution

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
