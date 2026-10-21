from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.change_request import ChangeRequest
    from ..models.record import Record
    from ..models.view import View


T = TypeVar("T", bound="ChangeRequestMergeSuccess")


@_attrs_define
class ChangeRequestMergeSuccess:
    """
    Attributes:
        change_request_id (str):
        ok (Literal[True]):
        status (str):
        change_request (ChangeRequest):
        record (None | Record):
        view (None | View):
    """

    change_request_id: str
    ok: Literal[True]
    status: str
    change_request: ChangeRequest
    record: None | Record
    view: None | View
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.record import Record
        from ..models.view import View

        change_request_id = self.change_request_id

        ok = self.ok

        status = self.status

        change_request = self.change_request.to_dict()

        record: dict[str, Any] | None
        if isinstance(self.record, Record):
            record = self.record.to_dict()
        else:
            record = self.record

        view: dict[str, Any] | None
        if isinstance(self.view, View):
            view = self.view.to_dict()
        else:
            view = self.view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changeRequestId": change_request_id,
                "ok": ok,
                "status": status,
                "changeRequest": change_request,
                "record": record,
                "view": view,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.change_request import ChangeRequest
        from ..models.record import Record
        from ..models.view import View

        d = dict(src_dict)
        change_request_id = d.pop("changeRequestId")

        ok = cast(Literal[True], d.pop("ok"))
        if ok != True:
            raise ValueError(f"ok must match const True, got '{ok}'")

        status = d.pop("status")

        change_request = ChangeRequest.from_dict(d.pop("changeRequest"))

        def _parse_record(data: object) -> None | Record:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                record_type_0 = Record.from_dict(data)

                return record_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Record, data)

        record = _parse_record(d.pop("record"))

        def _parse_view(data: object) -> None | View:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                view_type_0 = View.from_dict(data)

                return view_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | View, data)

        view = _parse_view(d.pop("view"))

        change_request_merge_success = cls(
            change_request_id=change_request_id,
            ok=ok,
            status=status,
            change_request=change_request,
            record=record,
            view=view,
        )

        change_request_merge_success.additional_properties = d
        return change_request_merge_success

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
