from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_document_settings_error_policy import (
    WorkflowDocumentSettingsErrorPolicy,
    check_workflow_document_settings_error_policy,
)
from ..models.workflow_document_settings_execution_mode import (
    WorkflowDocumentSettingsExecutionMode,
    check_workflow_document_settings_execution_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowDocumentSettings")


@_attrs_define
class WorkflowDocumentSettings:
    """
    Attributes:
        execution_mode (WorkflowDocumentSettingsExecutionMode | Unset):  Default: 'manual'.
        concurrency (int | Unset):  Default: 1.
        timeout_ms (int | Unset):  Default: 30000.
        error_policy (WorkflowDocumentSettingsErrorPolicy | Unset):  Default: 'stop'.
    """

    execution_mode: WorkflowDocumentSettingsExecutionMode | Unset = "manual"
    concurrency: int | Unset = 1
    timeout_ms: int | Unset = 30000
    error_policy: WorkflowDocumentSettingsErrorPolicy | Unset = "stop"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_mode: str | Unset = UNSET
        if not isinstance(self.execution_mode, Unset):
            execution_mode = self.execution_mode

        concurrency = self.concurrency

        timeout_ms = self.timeout_ms

        error_policy: str | Unset = UNSET
        if not isinstance(self.error_policy, Unset):
            error_policy = self.error_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_mode is not UNSET:
            field_dict["executionMode"] = execution_mode
        if concurrency is not UNSET:
            field_dict["concurrency"] = concurrency
        if timeout_ms is not UNSET:
            field_dict["timeoutMs"] = timeout_ms
        if error_policy is not UNSET:
            field_dict["errorPolicy"] = error_policy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _execution_mode = d.pop("executionMode", UNSET)
        execution_mode: WorkflowDocumentSettingsExecutionMode | Unset
        if isinstance(_execution_mode, Unset):
            execution_mode = UNSET
        else:
            execution_mode = check_workflow_document_settings_execution_mode(_execution_mode)

        concurrency = d.pop("concurrency", UNSET)

        timeout_ms = d.pop("timeoutMs", UNSET)

        _error_policy = d.pop("errorPolicy", UNSET)
        error_policy: WorkflowDocumentSettingsErrorPolicy | Unset
        if isinstance(_error_policy, Unset):
            error_policy = UNSET
        else:
            error_policy = check_workflow_document_settings_error_policy(_error_policy)

        workflow_document_settings = cls(
            execution_mode=execution_mode,
            concurrency=concurrency,
            timeout_ms=timeout_ms,
            error_policy=error_policy,
        )

        workflow_document_settings.additional_properties = d
        return workflow_document_settings

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
