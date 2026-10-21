from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_node_operation_node_type import CreateNodeOperationNodeType, check_create_node_operation_node_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_node_operation_fields_item import CreateNodeOperationFieldsItem
    from ..models.create_node_operation_metadata import CreateNodeOperationMetadata


T = TypeVar("T", bound="CreateNodeOperation")


@_attrs_define
class CreateNodeOperation:
    """
    Attributes:
        kind (Literal['create']):
        node_type (CreateNodeOperationNodeType):
        slug (str):
        name (str):
        ref (str | Unset): Optional in-change-request temp id for this node. A later operation can set parentNodeRef to
            this value to nest under it — e.g. create a folder with ref "growth", then create Bases with parentNodeRef
            "growth", all in one change request.
        parent_node_id (str | Unset):
        parent_node_ref (str | Unset): Parent this node under a node an EARLIER operation in the same change request
            created (matched by its ref). Mutually exclusive with parentNodeId.
        description (str | Unset):  Default: ''.
        metadata (CreateNodeOperationMetadata | Unset):
        fields (list[CreateNodeOperationFieldsItem] | Unset):
    """

    kind: Literal["create"]
    node_type: CreateNodeOperationNodeType
    slug: str
    name: str
    ref: str | Unset = UNSET
    parent_node_id: str | Unset = UNSET
    parent_node_ref: str | Unset = UNSET
    description: str | Unset = ""
    metadata: CreateNodeOperationMetadata | Unset = UNSET
    fields: list[CreateNodeOperationFieldsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        node_type: str = self.node_type

        slug = self.slug

        name = self.name

        ref = self.ref

        parent_node_id = self.parent_node_id

        parent_node_ref = self.parent_node_ref

        description = self.description

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "nodeType": node_type,
                "slug": slug,
                "name": name,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref
        if parent_node_id is not UNSET:
            field_dict["parentNodeId"] = parent_node_id
        if parent_node_ref is not UNSET:
            field_dict["parentNodeRef"] = parent_node_ref
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_node_operation_fields_item import CreateNodeOperationFieldsItem
        from ..models.create_node_operation_metadata import CreateNodeOperationMetadata

        d = dict(src_dict)
        kind = cast(Literal["create"], d.pop("kind"))
        if kind != "create":
            raise ValueError(f"kind must match const 'create', got '{kind}'")

        node_type = check_create_node_operation_node_type(d.pop("nodeType"))

        slug = d.pop("slug")

        name = d.pop("name")

        ref = d.pop("ref", UNSET)

        parent_node_id = d.pop("parentNodeId", UNSET)

        parent_node_ref = d.pop("parentNodeRef", UNSET)

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateNodeOperationMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateNodeOperationMetadata.from_dict(_metadata)

        _fields = d.pop("fields", UNSET)
        fields: list[CreateNodeOperationFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = CreateNodeOperationFieldsItem.from_dict(fields_item_data)

                fields.append(fields_item)

        create_node_operation = cls(
            kind=kind,
            node_type=node_type,
            slug=slug,
            name=name,
            ref=ref,
            parent_node_id=parent_node_id,
            parent_node_ref=parent_node_ref,
            description=description,
            metadata=metadata,
            fields=fields,
        )

        create_node_operation.additional_properties = d
        return create_node_operation

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
