from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.playbook_intent import PlaybookIntent, check_playbook_intent
from ..models.playbook_kind import PlaybookKind, check_playbook_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.playbook_files_item import PlaybookFilesItem


T = TypeVar("T", bound="Playbook")


@_attrs_define
class Playbook:
    """
    Attributes:
        kind (PlaybookKind):
        node_id (str):
        node_type (str):
        node_name (str):
        node_slug (str):
        path (list[str]):
        content (str):
        key (str | Unset):
        label (str | Unset):
        intent (PlaybookIntent | Unset):
        locale (str | Unset):
        name (str | Unset):
        description (str | Unset):
        files (list[PlaybookFilesItem] | Unset):
    """

    kind: PlaybookKind
    node_id: str
    node_type: str
    node_name: str
    node_slug: str
    path: list[str]
    content: str
    key: str | Unset = UNSET
    label: str | Unset = UNSET
    intent: PlaybookIntent | Unset = UNSET
    locale: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    files: list[PlaybookFilesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        node_id = self.node_id

        node_type = self.node_type

        node_name = self.node_name

        node_slug = self.node_slug

        path = self.path

        content = self.content

        key = self.key

        label = self.label

        intent: str | Unset = UNSET
        if not isinstance(self.intent, Unset):
            intent = self.intent

        locale = self.locale

        name = self.name

        description = self.description

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "nodeId": node_id,
                "nodeType": node_type,
                "nodeName": node_name,
                "nodeSlug": node_slug,
                "path": path,
                "content": content,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label
        if intent is not UNSET:
            field_dict["intent"] = intent
        if locale is not UNSET:
            field_dict["locale"] = locale
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.playbook_files_item import PlaybookFilesItem

        d = dict(src_dict)
        kind = check_playbook_kind(d.pop("kind"))

        node_id = d.pop("nodeId")

        node_type = d.pop("nodeType")

        node_name = d.pop("nodeName")

        node_slug = d.pop("nodeSlug")

        path = cast(list[str], d.pop("path"))

        content = d.pop("content")

        key = d.pop("key", UNSET)

        label = d.pop("label", UNSET)

        _intent = d.pop("intent", UNSET)
        intent: PlaybookIntent | Unset
        if isinstance(_intent, Unset):
            intent = UNSET
        else:
            intent = check_playbook_intent(_intent)

        locale = d.pop("locale", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _files = d.pop("files", UNSET)
        files: list[PlaybookFilesItem] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = PlaybookFilesItem.from_dict(files_item_data)

                files.append(files_item)

        playbook = cls(
            kind=kind,
            node_id=node_id,
            node_type=node_type,
            node_name=node_name,
            node_slug=node_slug,
            path=path,
            content=content,
            key=key,
            label=label,
            intent=intent,
            locale=locale,
            name=name,
            description=description,
            files=files,
        )

        playbook.additional_properties = d
        return playbook

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
