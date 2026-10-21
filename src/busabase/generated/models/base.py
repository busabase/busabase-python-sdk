from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.base_field import BaseField
    from ..models.base_review_policy import BaseReviewPolicy


T = TypeVar("T", bound="Base")


@_attrs_define
class Base:
    """
    Attributes:
        id (str):
        node_id (str):
        slug (str):
        name (str):
        description (str):
        review_policy (BaseReviewPolicy):
        created_at (str):
        fields (list[BaseField]):
    """

    id: str
    node_id: str
    slug: str
    name: str
    description: str
    review_policy: BaseReviewPolicy
    created_at: str
    fields: list[BaseField]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        node_id = self.node_id

        slug = self.slug

        name = self.name

        description = self.description

        review_policy = self.review_policy.to_dict()

        created_at = self.created_at

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nodeId": node_id,
                "slug": slug,
                "name": name,
                "description": description,
                "reviewPolicy": review_policy,
                "createdAt": created_at,
                "fields": fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.base_field import BaseField
        from ..models.base_review_policy import BaseReviewPolicy

        d = dict(src_dict)
        id = d.pop("id")

        node_id = d.pop("nodeId")

        slug = d.pop("slug")

        name = d.pop("name")

        description = d.pop("description")

        review_policy = BaseReviewPolicy.from_dict(d.pop("reviewPolicy"))

        created_at = d.pop("createdAt")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = BaseField.from_dict(fields_item_data)

            fields.append(fields_item)

        base = cls(
            id=id,
            node_id=node_id,
            slug=slug,
            name=name,
            description=description,
            review_policy=review_policy,
            created_at=created_at,
            fields=fields,
        )

        base.additional_properties = d
        return base

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
