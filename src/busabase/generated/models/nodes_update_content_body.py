from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nodes_update_content_body_content_type_0 import NodesUpdateContentBodyContentType0
    from ..models.nodes_update_content_body_content_type_1 import NodesUpdateContentBodyContentType1
    from ..models.nodes_update_content_body_content_type_2 import NodesUpdateContentBodyContentType2
    from ..models.nodes_update_content_body_content_type_3 import NodesUpdateContentBodyContentType3


T = TypeVar("T", bound="NodesUpdateContentBody")


@_attrs_define
class NodesUpdateContentBody:
    """
    Attributes:
        content (NodesUpdateContentBodyContentType0 | NodesUpdateContentBodyContentType1 |
            NodesUpdateContentBodyContentType2 | NodesUpdateContentBodyContentType3):
        message (str | Unset): Explanation shown to the human reviewer. Write a conventional-commit style subject —
            imperative verb + what + why, e.g. "Add rollback steps to the deploy runbook". Default: 'Update content'.
        submitted_by (str | Unset):  Default: 'local-producer'.
        auto_merge (bool | Unset):
    """

    content: (
        NodesUpdateContentBodyContentType0
        | NodesUpdateContentBodyContentType1
        | NodesUpdateContentBodyContentType2
        | NodesUpdateContentBodyContentType3
    )
    message: str | Unset = "Update content"
    submitted_by: str | Unset = "local-producer"
    auto_merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nodes_update_content_body_content_type_0 import NodesUpdateContentBodyContentType0
        from ..models.nodes_update_content_body_content_type_1 import NodesUpdateContentBodyContentType1
        from ..models.nodes_update_content_body_content_type_2 import NodesUpdateContentBodyContentType2

        content: dict[str, Any]
        if (
            isinstance(self.content, NodesUpdateContentBodyContentType0)
            or isinstance(self.content, NodesUpdateContentBodyContentType1)
            or isinstance(self.content, NodesUpdateContentBodyContentType2)
        ):
            content = self.content.to_dict()
        else:
            content = self.content.to_dict()

        message = self.message

        submitted_by = self.submitted_by

        auto_merge = self.auto_merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if submitted_by is not UNSET:
            field_dict["submittedBy"] = submitted_by
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.nodes_update_content_body_content_type_0 import NodesUpdateContentBodyContentType0
        from ..models.nodes_update_content_body_content_type_1 import NodesUpdateContentBodyContentType1
        from ..models.nodes_update_content_body_content_type_2 import NodesUpdateContentBodyContentType2
        from ..models.nodes_update_content_body_content_type_3 import NodesUpdateContentBodyContentType3

        d = dict(src_dict)

        def _parse_content(
            data: object,
        ) -> (
            NodesUpdateContentBodyContentType0
            | NodesUpdateContentBodyContentType1
            | NodesUpdateContentBodyContentType2
            | NodesUpdateContentBodyContentType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = NodesUpdateContentBodyContentType0.from_dict(data)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = NodesUpdateContentBodyContentType1.from_dict(data)

                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_2 = NodesUpdateContentBodyContentType2.from_dict(data)

                return content_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            content_type_3 = NodesUpdateContentBodyContentType3.from_dict(data)

            return content_type_3

        content = _parse_content(d.pop("content"))

        message = d.pop("message", UNSET)

        submitted_by = d.pop("submittedBy", UNSET)

        auto_merge = d.pop("autoMerge", UNSET)

        nodes_update_content_body = cls(
            content=content,
            message=message,
            submitted_by=submitted_by,
            auto_merge=auto_merge,
        )

        nodes_update_content_body.additional_properties = d
        return nodes_update_content_body

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
