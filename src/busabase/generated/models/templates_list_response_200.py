from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.templates_list_response_200_templates_item import TemplatesListResponse200TemplatesItem


T = TypeVar("T", bound="TemplatesListResponse200")


@_attrs_define
class TemplatesListResponse200:
    """
    Attributes:
        templates (list[TemplatesListResponse200TemplatesItem]):
        repo (str):
        ref (str):
        error (str | Unset):
    """

    templates: list[TemplatesListResponse200TemplatesItem]
    repo: str
    ref: str
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        templates = []
        for templates_item_data in self.templates:
            templates_item = templates_item_data.to_dict()
            templates.append(templates_item)

        repo = self.repo

        ref = self.ref

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templates": templates,
                "repo": repo,
                "ref": ref,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.templates_list_response_200_templates_item import TemplatesListResponse200TemplatesItem

        d = dict(src_dict)
        templates = []
        _templates = d.pop("templates")
        for templates_item_data in _templates:
            templates_item = TemplatesListResponse200TemplatesItem.from_dict(templates_item_data)

            templates.append(templates_item)

        repo = d.pop("repo")

        ref = d.pop("ref")

        error = d.pop("error", UNSET)

        templates_list_response_200 = cls(
            templates=templates,
            repo=repo,
            ref=ref,
            error=error,
        )

        templates_list_response_200.additional_properties = d
        return templates_list_response_200

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
