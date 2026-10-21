from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_document_edges_item import WorkflowDocumentEdgesItem
    from ..models.workflow_document_nodes_item_type_0 import WorkflowDocumentNodesItemType0
    from ..models.workflow_document_nodes_item_type_1 import WorkflowDocumentNodesItemType1
    from ..models.workflow_document_nodes_item_type_2 import WorkflowDocumentNodesItemType2
    from ..models.workflow_document_nodes_item_type_3 import WorkflowDocumentNodesItemType3
    from ..models.workflow_document_nodes_item_type_4 import WorkflowDocumentNodesItemType4
    from ..models.workflow_document_nodes_item_type_5 import WorkflowDocumentNodesItemType5
    from ..models.workflow_document_nodes_item_type_6 import WorkflowDocumentNodesItemType6
    from ..models.workflow_document_nodes_item_type_7 import WorkflowDocumentNodesItemType7
    from ..models.workflow_document_settings import WorkflowDocumentSettings


T = TypeVar("T", bound="WorkflowDocument")


@_attrs_define
class WorkflowDocument:
    """
    Attributes:
        version (Literal[2]):
        nodes (list[WorkflowDocumentNodesItemType0 | WorkflowDocumentNodesItemType1 | WorkflowDocumentNodesItemType2 |
            WorkflowDocumentNodesItemType3 | WorkflowDocumentNodesItemType4 | WorkflowDocumentNodesItemType5 |
            WorkflowDocumentNodesItemType6 | WorkflowDocumentNodesItemType7] | Unset):
        edges (list[WorkflowDocumentEdgesItem] | Unset):
        settings (WorkflowDocumentSettings | Unset):
    """

    version: Literal[2]
    nodes: (
        list[
            WorkflowDocumentNodesItemType0
            | WorkflowDocumentNodesItemType1
            | WorkflowDocumentNodesItemType2
            | WorkflowDocumentNodesItemType3
            | WorkflowDocumentNodesItemType4
            | WorkflowDocumentNodesItemType5
            | WorkflowDocumentNodesItemType6
            | WorkflowDocumentNodesItemType7
        ]
        | Unset
    ) = UNSET
    edges: list[WorkflowDocumentEdgesItem] | Unset = UNSET
    settings: WorkflowDocumentSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_document_nodes_item_type_0 import WorkflowDocumentNodesItemType0
        from ..models.workflow_document_nodes_item_type_1 import WorkflowDocumentNodesItemType1
        from ..models.workflow_document_nodes_item_type_2 import WorkflowDocumentNodesItemType2
        from ..models.workflow_document_nodes_item_type_3 import WorkflowDocumentNodesItemType3
        from ..models.workflow_document_nodes_item_type_4 import WorkflowDocumentNodesItemType4
        from ..models.workflow_document_nodes_item_type_5 import WorkflowDocumentNodesItemType5
        from ..models.workflow_document_nodes_item_type_6 import WorkflowDocumentNodesItemType6

        version = self.version

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item: dict[str, Any]
                if (
                    isinstance(nodes_item_data, WorkflowDocumentNodesItemType0)
                    or isinstance(nodes_item_data, WorkflowDocumentNodesItemType1)
                    or isinstance(nodes_item_data, WorkflowDocumentNodesItemType2)
                    or isinstance(nodes_item_data, WorkflowDocumentNodesItemType3)
                    or isinstance(nodes_item_data, WorkflowDocumentNodesItemType4)
                    or isinstance(nodes_item_data, WorkflowDocumentNodesItemType5)
                    or isinstance(nodes_item_data, WorkflowDocumentNodesItemType6)
                ):
                    nodes_item = nodes_item_data.to_dict()
                else:
                    nodes_item = nodes_item_data.to_dict()

                nodes.append(nodes_item)

        edges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edges, Unset):
            edges = []
            for edges_item_data in self.edges:
                edges_item = edges_item_data.to_dict()
                edges.append(edges_item)

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
            }
        )
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if edges is not UNSET:
            field_dict["edges"] = edges
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_document_edges_item import WorkflowDocumentEdgesItem
        from ..models.workflow_document_nodes_item_type_0 import WorkflowDocumentNodesItemType0
        from ..models.workflow_document_nodes_item_type_1 import WorkflowDocumentNodesItemType1
        from ..models.workflow_document_nodes_item_type_2 import WorkflowDocumentNodesItemType2
        from ..models.workflow_document_nodes_item_type_3 import WorkflowDocumentNodesItemType3
        from ..models.workflow_document_nodes_item_type_4 import WorkflowDocumentNodesItemType4
        from ..models.workflow_document_nodes_item_type_5 import WorkflowDocumentNodesItemType5
        from ..models.workflow_document_nodes_item_type_6 import WorkflowDocumentNodesItemType6
        from ..models.workflow_document_nodes_item_type_7 import WorkflowDocumentNodesItemType7
        from ..models.workflow_document_settings import WorkflowDocumentSettings

        d = dict(src_dict)
        version = cast(Literal[2], d.pop("version"))
        if version != 2:
            raise ValueError(f"version must match const 2, got '{version}'")

        _nodes = d.pop("nodes", UNSET)
        nodes: (
            list[
                WorkflowDocumentNodesItemType0
                | WorkflowDocumentNodesItemType1
                | WorkflowDocumentNodesItemType2
                | WorkflowDocumentNodesItemType3
                | WorkflowDocumentNodesItemType4
                | WorkflowDocumentNodesItemType5
                | WorkflowDocumentNodesItemType6
                | WorkflowDocumentNodesItemType7
            ]
            | Unset
        ) = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:

                def _parse_nodes_item(
                    data: object,
                ) -> (
                    WorkflowDocumentNodesItemType0
                    | WorkflowDocumentNodesItemType1
                    | WorkflowDocumentNodesItemType2
                    | WorkflowDocumentNodesItemType3
                    | WorkflowDocumentNodesItemType4
                    | WorkflowDocumentNodesItemType5
                    | WorkflowDocumentNodesItemType6
                    | WorkflowDocumentNodesItemType7
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        nodes_item_type_0 = WorkflowDocumentNodesItemType0.from_dict(data)

                        return nodes_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        nodes_item_type_1 = WorkflowDocumentNodesItemType1.from_dict(data)

                        return nodes_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        nodes_item_type_2 = WorkflowDocumentNodesItemType2.from_dict(data)

                        return nodes_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        nodes_item_type_3 = WorkflowDocumentNodesItemType3.from_dict(data)

                        return nodes_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        nodes_item_type_4 = WorkflowDocumentNodesItemType4.from_dict(data)

                        return nodes_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        nodes_item_type_5 = WorkflowDocumentNodesItemType5.from_dict(data)

                        return nodes_item_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        nodes_item_type_6 = WorkflowDocumentNodesItemType6.from_dict(data)

                        return nodes_item_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    nodes_item_type_7 = WorkflowDocumentNodesItemType7.from_dict(data)

                    return nodes_item_type_7

                nodes_item = _parse_nodes_item(nodes_item_data)

                nodes.append(nodes_item)

        _edges = d.pop("edges", UNSET)
        edges: list[WorkflowDocumentEdgesItem] | Unset = UNSET
        if _edges is not UNSET:
            edges = []
            for edges_item_data in _edges:
                edges_item = WorkflowDocumentEdgesItem.from_dict(edges_item_data)

                edges.append(edges_item)

        _settings = d.pop("settings", UNSET)
        settings: WorkflowDocumentSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = WorkflowDocumentSettings.from_dict(_settings)

        workflow_document = cls(
            version=version,
            nodes=nodes,
            edges=edges,
            settings=settings,
        )

        workflow_document.additional_properties = d
        return workflow_document

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
