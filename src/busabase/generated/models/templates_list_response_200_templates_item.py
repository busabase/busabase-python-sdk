from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.templates_list_response_200_templates_item_risk import (
    TemplatesListResponse200TemplatesItemRisk,
    check_templates_list_response_200_templates_item_risk,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText
    from ..models.templates_list_response_200_templates_item_install import TemplatesListResponse200TemplatesItemInstall
    from ..models.templates_list_response_200_templates_item_stats import TemplatesListResponse200TemplatesItemStats


T = TypeVar("T", bound="TemplatesListResponse200TemplatesItem")


@_attrs_define
class TemplatesListResponse200TemplatesItem:
    """
    Attributes:
        id (str):
        name (str):
        description (LocalizedText | str): i18n string
        category (str):
        stats (TemplatesListResponse200TemplatesItemStats):
        install (TemplatesListResponse200TemplatesItemInstall):
        source_url (str):
        display_name (LocalizedText | str | Unset): i18n string
        risk (TemplatesListResponse200TemplatesItemRisk | Unset):
        tags (list[str] | Unset):
        screenshots (list[str] | Unset):
        video (str | Unset):
        agent_prompts (list[str] | Unset):
        version (str | Unset):
        author (str | Unset):
        license_ (str | Unset):
    """

    id: str
    name: str
    description: LocalizedText | str
    category: str
    stats: TemplatesListResponse200TemplatesItemStats
    install: TemplatesListResponse200TemplatesItemInstall
    source_url: str
    display_name: LocalizedText | str | Unset = UNSET
    risk: TemplatesListResponse200TemplatesItemRisk | Unset = UNSET
    tags: list[str] | Unset = UNSET
    screenshots: list[str] | Unset = UNSET
    video: str | Unset = UNSET
    agent_prompts: list[str] | Unset = UNSET
    version: str | Unset = UNSET
    author: str | Unset = UNSET
    license_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_text import LocalizedText

        id = self.id

        name = self.name

        description: dict[str, Any] | str
        if isinstance(self.description, LocalizedText):
            description = self.description.to_dict()
        else:
            description = self.description

        category = self.category

        stats = self.stats.to_dict()

        install = self.install.to_dict()

        source_url = self.source_url

        display_name: dict[str, Any] | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        elif isinstance(self.display_name, LocalizedText):
            display_name = self.display_name.to_dict()
        else:
            display_name = self.display_name

        risk: str | Unset = UNSET
        if not isinstance(self.risk, Unset):
            risk = self.risk

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        screenshots: list[str] | Unset = UNSET
        if not isinstance(self.screenshots, Unset):
            screenshots = self.screenshots

        video = self.video

        agent_prompts: list[str] | Unset = UNSET
        if not isinstance(self.agent_prompts, Unset):
            agent_prompts = self.agent_prompts

        version = self.version

        author = self.author

        license_ = self.license_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "category": category,
                "stats": stats,
                "install": install,
                "sourceUrl": source_url,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if risk is not UNSET:
            field_dict["risk"] = risk
        if tags is not UNSET:
            field_dict["tags"] = tags
        if screenshots is not UNSET:
            field_dict["screenshots"] = screenshots
        if video is not UNSET:
            field_dict["video"] = video
        if agent_prompts is not UNSET:
            field_dict["agentPrompts"] = agent_prompts
        if version is not UNSET:
            field_dict["version"] = version
        if author is not UNSET:
            field_dict["author"] = author
        if license_ is not UNSET:
            field_dict["license"] = license_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.localized_text import LocalizedText
        from ..models.templates_list_response_200_templates_item_install import (
            TemplatesListResponse200TemplatesItemInstall,
        )
        from ..models.templates_list_response_200_templates_item_stats import TemplatesListResponse200TemplatesItemStats

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> LocalizedText | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                description_type_1 = LocalizedText.from_dict(data)

                return description_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedText | str, data)

        description = _parse_description(d.pop("description"))

        category = d.pop("category")

        stats = TemplatesListResponse200TemplatesItemStats.from_dict(d.pop("stats"))

        install = TemplatesListResponse200TemplatesItemInstall.from_dict(d.pop("install"))

        source_url = d.pop("sourceUrl")

        def _parse_display_name(data: object) -> LocalizedText | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                display_name_type_1 = LocalizedText.from_dict(data)

                return display_name_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedText | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        _risk = d.pop("risk", UNSET)
        risk: TemplatesListResponse200TemplatesItemRisk | Unset
        if isinstance(_risk, Unset):
            risk = UNSET
        else:
            risk = check_templates_list_response_200_templates_item_risk(_risk)

        tags = cast(list[str], d.pop("tags", UNSET))

        screenshots = cast(list[str], d.pop("screenshots", UNSET))

        video = d.pop("video", UNSET)

        agent_prompts = cast(list[str], d.pop("agentPrompts", UNSET))

        version = d.pop("version", UNSET)

        author = d.pop("author", UNSET)

        license_ = d.pop("license", UNSET)

        templates_list_response_200_templates_item = cls(
            id=id,
            name=name,
            description=description,
            category=category,
            stats=stats,
            install=install,
            source_url=source_url,
            display_name=display_name,
            risk=risk,
            tags=tags,
            screenshots=screenshots,
            video=video,
            agent_prompts=agent_prompts,
            version=version,
            author=author,
            license_=license_,
        )

        templates_list_response_200_templates_item.additional_properties = d
        return templates_list_response_200_templates_item

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
