from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_activity import AuditActivity
    from ..models.change_request_activity import ChangeRequestActivity
    from ..models.operation_activity import OperationActivity
    from ..models.record_activity import RecordActivity


T = TypeVar("T", bound="ActivityListForRecordPagedResponse200")


@_attrs_define
class ActivityListForRecordPagedResponse200:
    """
    Attributes:
        items (list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity]):
        next_cursor (None | str):
    """

    items: list[AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity]
    next_cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.change_request_activity import ChangeRequestActivity
        from ..models.operation_activity import OperationActivity
        from ..models.record_activity import RecordActivity

        items = []
        for items_item_data in self.items:
            items_item: dict[str, Any]
            if (
                isinstance(items_item_data, ChangeRequestActivity)
                or isinstance(items_item_data, OperationActivity)
                or isinstance(items_item_data, RecordActivity)
            ):
                items_item = items_item_data.to_dict()
            else:
                items_item = items_item_data.to_dict()

            items.append(items_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "nextCursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_activity import AuditActivity
        from ..models.change_request_activity import ChangeRequestActivity
        from ..models.operation_activity import OperationActivity
        from ..models.record_activity import RecordActivity

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:

            def _parse_items_item(
                data: object,
            ) -> AuditActivity | ChangeRequestActivity | OperationActivity | RecordActivity:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_activity_item_type_0 = ChangeRequestActivity.from_dict(data)

                    return componentsschemas_activity_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_activity_item_type_1 = OperationActivity.from_dict(data)

                    return componentsschemas_activity_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_activity_item_type_2 = RecordActivity.from_dict(data)

                    return componentsschemas_activity_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_activity_item_type_3 = AuditActivity.from_dict(data)

                return componentsschemas_activity_item_type_3

            items_item = _parse_items_item(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))

        activity_list_for_record_paged_response_200 = cls(
            items=items,
            next_cursor=next_cursor,
        )

        activity_list_for_record_paged_response_200.additional_properties = d
        return activity_list_for_record_paged_response_200

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
