from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whiteboard_document_app_state import WhiteboardDocumentAppState


T = TypeVar("T", bound="WhiteboardDocument")


@_attrs_define
class WhiteboardDocument:
    """
    Attributes:
        version (Literal[1]):
        elements (list[Any | None] | Unset):
        app_state (WhiteboardDocumentAppState | Unset):
    """

    version: Literal[1]
    elements: list[Any | None] | Unset = UNSET
    app_state: WhiteboardDocumentAppState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        elements: list[Any | None] | Unset = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item: Any | None
                elements_item = elements_item_data
                elements.append(elements_item)

        app_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_state, Unset):
            app_state = self.app_state.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
            }
        )
        if elements is not UNSET:
            field_dict["elements"] = elements
        if app_state is not UNSET:
            field_dict["appState"] = app_state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.whiteboard_document_app_state import WhiteboardDocumentAppState

        d = dict(src_dict)
        version = cast(Literal[1], d.pop("version"))
        if version != 1:
            raise ValueError(f"version must match const 1, got '{version}'")

        _elements = d.pop("elements", UNSET)
        elements: list[Any | None] | Unset = UNSET
        if _elements is not UNSET:
            elements = []
            for elements_item_data in _elements:

                def _parse_elements_item(data: object) -> Any | None:
                    if data is None:
                        return data
                    return cast(Any | None, data)

                elements_item = _parse_elements_item(elements_item_data)

                elements.append(elements_item)

        _app_state = d.pop("appState", UNSET)
        app_state: WhiteboardDocumentAppState | Unset
        if isinstance(_app_state, Unset):
            app_state = UNSET
        else:
            app_state = WhiteboardDocumentAppState.from_dict(_app_state)

        whiteboard_document = cls(
            version=version,
            elements=elements,
            app_state=app_state,
        )

        whiteboard_document.additional_properties = d
        return whiteboard_document

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
