from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="InstallPlanFromGithubResponse200Package")


@_attrs_define
class InstallPlanFromGithubResponse200Package:
    """
    Attributes:
        name (str):
        display_name (LocalizedText | str | Unset): i18n string
        description (LocalizedText | str | Unset): i18n string Default: ''.
        version (str | Unset):
        author (str | Unset):
        license_ (str | Unset):
        homepage (str | Unset):
        tags (list[str] | Unset):
    """

    name: str
    display_name: LocalizedText | str | Unset = UNSET
    description: LocalizedText | str | Unset = ""
    version: str | Unset = UNSET
    author: str | Unset = UNSET
    license_: str | Unset = UNSET
    homepage: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_text import LocalizedText

        name = self.name

        display_name: dict[str, Any] | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        elif isinstance(self.display_name, LocalizedText):
            display_name = self.display_name.to_dict()
        else:
            display_name = self.display_name

        description: dict[str, Any] | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, LocalizedText):
            description = self.description.to_dict()
        else:
            description = self.description

        version = self.version

        author = self.author

        license_ = self.license_

        homepage = self.homepage

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version
        if author is not UNSET:
            field_dict["author"] = author
        if license_ is not UNSET:
            field_dict["license"] = license_
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.localized_text import LocalizedText

        d = dict(src_dict)
        name = d.pop("name")

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

        def _parse_description(data: object) -> LocalizedText | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                description_type_1 = LocalizedText.from_dict(data)

                return description_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedText | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        version = d.pop("version", UNSET)

        author = d.pop("author", UNSET)

        license_ = d.pop("license", UNSET)

        homepage = d.pop("homepage", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        install_plan_from_github_response_200_package = cls(
            name=name,
            display_name=display_name,
            description=description,
            version=version,
            author=author,
            license_=license_,
            homepage=homepage,
            tags=tags,
        )

        install_plan_from_github_response_200_package.additional_properties = d
        return install_plan_from_github_response_200_package

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
