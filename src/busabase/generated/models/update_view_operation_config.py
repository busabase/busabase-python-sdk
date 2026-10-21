from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_view_operation_config_card_size import (
    UpdateViewOperationConfigCardSize,
    check_update_view_operation_config_card_size,
)
from ..models.update_view_operation_config_cover_fit import (
    UpdateViewOperationConfigCoverFit,
    check_update_view_operation_config_cover_fit,
)
from ..models.update_view_operation_config_gantt_scale import (
    UpdateViewOperationConfigGanttScale,
    check_update_view_operation_config_gantt_scale,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_view_operation_config_field_widths import UpdateViewOperationConfigFieldWidths
    from ..models.view_filter import ViewFilter
    from ..models.view_sort import ViewSort


T = TypeVar("T", bound="UpdateViewOperationConfig")


@_attrs_define
class UpdateViewOperationConfig:
    """Only supplied config keys change; empty arrays and null clear supported settings.

    Attributes:
        visible_field_slugs (list[str] | None | Unset):
        field_widths (UpdateViewOperationConfigFieldWidths | Unset):
        cover_field_slug (None | str | Unset):
        cover_fit (UpdateViewOperationConfigCoverFit | Unset):
        card_size (UpdateViewOperationConfigCardSize | Unset):
        show_field_labels (bool | Unset):
        stack_by_field_slug (None | str | Unset):
        date_field_slug (None | str | Unset):
        start_field_slug (None | str | Unset):
        end_field_slug (None | str | Unset):
        gantt_scale (UpdateViewOperationConfigGanttScale | Unset):
        filters (list[ViewFilter] | Unset):
        sorts (list[ViewSort] | Unset):
    """

    visible_field_slugs: list[str] | None | Unset = UNSET
    field_widths: UpdateViewOperationConfigFieldWidths | Unset = UNSET
    cover_field_slug: None | str | Unset = UNSET
    cover_fit: UpdateViewOperationConfigCoverFit | Unset = UNSET
    card_size: UpdateViewOperationConfigCardSize | Unset = UNSET
    show_field_labels: bool | Unset = UNSET
    stack_by_field_slug: None | str | Unset = UNSET
    date_field_slug: None | str | Unset = UNSET
    start_field_slug: None | str | Unset = UNSET
    end_field_slug: None | str | Unset = UNSET
    gantt_scale: UpdateViewOperationConfigGanttScale | Unset = UNSET
    filters: list[ViewFilter] | Unset = UNSET
    sorts: list[ViewSort] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visible_field_slugs: list[str] | None | Unset
        if isinstance(self.visible_field_slugs, Unset):
            visible_field_slugs = UNSET
        elif isinstance(self.visible_field_slugs, list):
            visible_field_slugs = self.visible_field_slugs

        else:
            visible_field_slugs = self.visible_field_slugs

        field_widths: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_widths, Unset):
            field_widths = self.field_widths.to_dict()

        cover_field_slug: None | str | Unset
        if isinstance(self.cover_field_slug, Unset):
            cover_field_slug = UNSET
        else:
            cover_field_slug = self.cover_field_slug

        cover_fit: str | Unset = UNSET
        if not isinstance(self.cover_fit, Unset):
            cover_fit = self.cover_fit

        card_size: str | Unset = UNSET
        if not isinstance(self.card_size, Unset):
            card_size = self.card_size

        show_field_labels = self.show_field_labels

        stack_by_field_slug: None | str | Unset
        if isinstance(self.stack_by_field_slug, Unset):
            stack_by_field_slug = UNSET
        else:
            stack_by_field_slug = self.stack_by_field_slug

        date_field_slug: None | str | Unset
        if isinstance(self.date_field_slug, Unset):
            date_field_slug = UNSET
        else:
            date_field_slug = self.date_field_slug

        start_field_slug: None | str | Unset
        if isinstance(self.start_field_slug, Unset):
            start_field_slug = UNSET
        else:
            start_field_slug = self.start_field_slug

        end_field_slug: None | str | Unset
        if isinstance(self.end_field_slug, Unset):
            end_field_slug = UNSET
        else:
            end_field_slug = self.end_field_slug

        gantt_scale: str | Unset = UNSET
        if not isinstance(self.gantt_scale, Unset):
            gantt_scale = self.gantt_scale

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        sorts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sorts, Unset):
            sorts = []
            for sorts_item_data in self.sorts:
                sorts_item = sorts_item_data.to_dict()
                sorts.append(sorts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if visible_field_slugs is not UNSET:
            field_dict["visibleFieldSlugs"] = visible_field_slugs
        if field_widths is not UNSET:
            field_dict["fieldWidths"] = field_widths
        if cover_field_slug is not UNSET:
            field_dict["coverFieldSlug"] = cover_field_slug
        if cover_fit is not UNSET:
            field_dict["coverFit"] = cover_fit
        if card_size is not UNSET:
            field_dict["cardSize"] = card_size
        if show_field_labels is not UNSET:
            field_dict["showFieldLabels"] = show_field_labels
        if stack_by_field_slug is not UNSET:
            field_dict["stackByFieldSlug"] = stack_by_field_slug
        if date_field_slug is not UNSET:
            field_dict["dateFieldSlug"] = date_field_slug
        if start_field_slug is not UNSET:
            field_dict["startFieldSlug"] = start_field_slug
        if end_field_slug is not UNSET:
            field_dict["endFieldSlug"] = end_field_slug
        if gantt_scale is not UNSET:
            field_dict["ganttScale"] = gantt_scale
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sorts is not UNSET:
            field_dict["sorts"] = sorts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_view_operation_config_field_widths import UpdateViewOperationConfigFieldWidths
        from ..models.view_filter import ViewFilter
        from ..models.view_sort import ViewSort

        d = dict(src_dict)

        def _parse_visible_field_slugs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                visible_field_slugs_type_0 = cast(list[str], data)

                return visible_field_slugs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        visible_field_slugs = _parse_visible_field_slugs(d.pop("visibleFieldSlugs", UNSET))

        _field_widths = d.pop("fieldWidths", UNSET)
        field_widths: UpdateViewOperationConfigFieldWidths | Unset
        if isinstance(_field_widths, Unset):
            field_widths = UNSET
        else:
            field_widths = UpdateViewOperationConfigFieldWidths.from_dict(_field_widths)

        def _parse_cover_field_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_field_slug = _parse_cover_field_slug(d.pop("coverFieldSlug", UNSET))

        _cover_fit = d.pop("coverFit", UNSET)
        cover_fit: UpdateViewOperationConfigCoverFit | Unset
        if isinstance(_cover_fit, Unset):
            cover_fit = UNSET
        else:
            cover_fit = check_update_view_operation_config_cover_fit(_cover_fit)

        _card_size = d.pop("cardSize", UNSET)
        card_size: UpdateViewOperationConfigCardSize | Unset
        if isinstance(_card_size, Unset):
            card_size = UNSET
        else:
            card_size = check_update_view_operation_config_card_size(_card_size)

        show_field_labels = d.pop("showFieldLabels", UNSET)

        def _parse_stack_by_field_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stack_by_field_slug = _parse_stack_by_field_slug(d.pop("stackByFieldSlug", UNSET))

        def _parse_date_field_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_field_slug = _parse_date_field_slug(d.pop("dateFieldSlug", UNSET))

        def _parse_start_field_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_field_slug = _parse_start_field_slug(d.pop("startFieldSlug", UNSET))

        def _parse_end_field_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_field_slug = _parse_end_field_slug(d.pop("endFieldSlug", UNSET))

        _gantt_scale = d.pop("ganttScale", UNSET)
        gantt_scale: UpdateViewOperationConfigGanttScale | Unset
        if isinstance(_gantt_scale, Unset):
            gantt_scale = UNSET
        else:
            gantt_scale = check_update_view_operation_config_gantt_scale(_gantt_scale)

        _filters = d.pop("filters", UNSET)
        filters: list[ViewFilter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = ViewFilter.from_dict(filters_item_data)

                filters.append(filters_item)

        _sorts = d.pop("sorts", UNSET)
        sorts: list[ViewSort] | Unset = UNSET
        if _sorts is not UNSET:
            sorts = []
            for sorts_item_data in _sorts:
                sorts_item = ViewSort.from_dict(sorts_item_data)

                sorts.append(sorts_item)

        update_view_operation_config = cls(
            visible_field_slugs=visible_field_slugs,
            field_widths=field_widths,
            cover_field_slug=cover_field_slug,
            cover_fit=cover_fit,
            card_size=card_size,
            show_field_labels=show_field_labels,
            stack_by_field_slug=stack_by_field_slug,
            date_field_slug=date_field_slug,
            start_field_slug=start_field_slug,
            end_field_slug=end_field_slug,
            gantt_scale=gantt_scale,
            filters=filters,
            sorts=sorts,
        )

        update_view_operation_config.additional_properties = d
        return update_view_operation_config

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
