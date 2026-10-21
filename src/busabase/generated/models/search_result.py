from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_result_kind import SearchResultKind, check_search_result_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResult")


@_attrs_define
class SearchResult:
    """
    Attributes:
        id (str):
        kind (SearchResultKind):
        title (str):
        body (str):
        eyebrow (str):
        href (str):
        updated_at (None | str):
        created_by (None | str | Unset):
    """

    id: str
    kind: SearchResultKind
    title: str
    body: str
    eyebrow: str
    href: str
    updated_at: None | str
    created_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind: str = self.kind

        title = self.title

        body = self.body

        eyebrow = self.eyebrow

        href = self.href

        updated_at: None | str
        updated_at = self.updated_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "title": title,
                "body": body,
                "eyebrow": eyebrow,
                "href": href,
                "updatedAt": updated_at,
            }
        )
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        kind = check_search_result_kind(d.pop("kind"))

        title = d.pop("title")

        body = d.pop("body")

        eyebrow = d.pop("eyebrow")

        href = d.pop("href")

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))

        search_result = cls(
            id=id,
            kind=kind,
            title=title,
            body=body,
            eyebrow=eyebrow,
            href=href,
            updated_at=updated_at,
            created_by=created_by,
        )

        search_result.additional_properties = d
        return search_result

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
