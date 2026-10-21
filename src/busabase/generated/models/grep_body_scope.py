from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grep_body_scope_files import GrepBodyScopeFiles
    from ..models.grep_body_scope_nodes import GrepBodyScopeNodes
    from ..models.grep_body_scope_records import GrepBodyScopeRecords


T = TypeVar("T", bound="GrepBodyScope")


@_attrs_define
class GrepBodyScope:
    """
    Attributes:
        files (GrepBodyScopeFiles | Unset):
        nodes (GrepBodyScopeNodes | Unset):
        records (GrepBodyScopeRecords | Unset):
    """

    files: GrepBodyScopeFiles | Unset = UNSET
    nodes: GrepBodyScopeNodes | Unset = UNSET
    records: GrepBodyScopeRecords | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        nodes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes.to_dict()

        records: dict[str, Any] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = self.records.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grep_body_scope_files import GrepBodyScopeFiles
        from ..models.grep_body_scope_nodes import GrepBodyScopeNodes
        from ..models.grep_body_scope_records import GrepBodyScopeRecords

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: GrepBodyScopeFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = GrepBodyScopeFiles.from_dict(_files)

        _nodes = d.pop("nodes", UNSET)
        nodes: GrepBodyScopeNodes | Unset
        if isinstance(_nodes, Unset):
            nodes = UNSET
        else:
            nodes = GrepBodyScopeNodes.from_dict(_nodes)

        _records = d.pop("records", UNSET)
        records: GrepBodyScopeRecords | Unset
        if isinstance(_records, Unset):
            records = UNSET
        else:
            records = GrepBodyScopeRecords.from_dict(_records)

        grep_body_scope = cls(
            files=files,
            nodes=nodes,
            records=records,
        )

        grep_body_scope.additional_properties = d
        return grep_body_scope

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
