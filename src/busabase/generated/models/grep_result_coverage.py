from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grep_result_coverage_files import GrepResultCoverageFiles
    from ..models.grep_result_coverage_nodes import GrepResultCoverageNodes
    from ..models.grep_result_coverage_prompts import GrepResultCoveragePrompts
    from ..models.grep_result_coverage_records import GrepResultCoverageRecords


T = TypeVar("T", bound="GrepResultCoverage")


@_attrs_define
class GrepResultCoverage:
    """
    Attributes:
        files (GrepResultCoverageFiles):
        nodes (GrepResultCoverageNodes):
        records (GrepResultCoverageRecords):
        prompts (GrepResultCoveragePrompts | Unset):
    """

    files: GrepResultCoverageFiles
    nodes: GrepResultCoverageNodes
    records: GrepResultCoverageRecords
    prompts: GrepResultCoveragePrompts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = self.files.to_dict()

        nodes = self.nodes.to_dict()

        records = self.records.to_dict()

        prompts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prompts, Unset):
            prompts = self.prompts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
                "nodes": nodes,
                "records": records,
            }
        )
        if prompts is not UNSET:
            field_dict["prompts"] = prompts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grep_result_coverage_files import GrepResultCoverageFiles
        from ..models.grep_result_coverage_nodes import GrepResultCoverageNodes
        from ..models.grep_result_coverage_prompts import GrepResultCoveragePrompts
        from ..models.grep_result_coverage_records import GrepResultCoverageRecords

        d = dict(src_dict)
        files = GrepResultCoverageFiles.from_dict(d.pop("files"))

        nodes = GrepResultCoverageNodes.from_dict(d.pop("nodes"))

        records = GrepResultCoverageRecords.from_dict(d.pop("records"))

        _prompts = d.pop("prompts", UNSET)
        prompts: GrepResultCoveragePrompts | Unset
        if isinstance(_prompts, Unset):
            prompts = UNSET
        else:
            prompts = GrepResultCoveragePrompts.from_dict(_prompts)

        grep_result_coverage = cls(
            files=files,
            nodes=nodes,
            records=records,
            prompts=prompts,
        )

        grep_result_coverage.additional_properties = d
        return grep_result_coverage

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
