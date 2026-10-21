from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_options_lookup_limit import FieldOptionsLookupLimit, check_field_options_lookup_limit
from ..models.field_options_lookup_rollup import FieldOptionsLookupRollup, check_field_options_lookup_rollup
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldOptionsLookup")


@_attrs_define
class FieldOptionsLookup:
    """
    Attributes:
        relation_field_slug (str): Slug of a `relation` field on THIS Base — the hop to follow.
        target_field_slug (str): Slug of the field on the related Base whose values are pulled over.
        rollup (FieldOptionsLookupRollup | Unset):  Default: 'values'.
        limit (FieldOptionsLookupLimit | Unset): `first` looks at only the first linked record; default `all`.
    """

    relation_field_slug: str
    target_field_slug: str
    rollup: FieldOptionsLookupRollup | Unset = "values"
    limit: FieldOptionsLookupLimit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relation_field_slug = self.relation_field_slug

        target_field_slug = self.target_field_slug

        rollup: str | Unset = UNSET
        if not isinstance(self.rollup, Unset):
            rollup = self.rollup

        limit: str | Unset = UNSET
        if not isinstance(self.limit, Unset):
            limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relationFieldSlug": relation_field_slug,
                "targetFieldSlug": target_field_slug,
            }
        )
        if rollup is not UNSET:
            field_dict["rollup"] = rollup
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        relation_field_slug = d.pop("relationFieldSlug")

        target_field_slug = d.pop("targetFieldSlug")

        _rollup = d.pop("rollup", UNSET)
        rollup: FieldOptionsLookupRollup | Unset
        if isinstance(_rollup, Unset):
            rollup = UNSET
        else:
            rollup = check_field_options_lookup_rollup(_rollup)

        _limit = d.pop("limit", UNSET)
        limit: FieldOptionsLookupLimit | Unset
        if isinstance(_limit, Unset):
            limit = UNSET
        else:
            limit = check_field_options_lookup_limit(_limit)

        field_options_lookup = cls(
            relation_field_slug=relation_field_slug,
            target_field_slug=target_field_slug,
            rollup=rollup,
            limit=limit,
        )

        field_options_lookup.additional_properties = d
        return field_options_lookup

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
