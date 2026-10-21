from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pending_change_request_status import PendingChangeRequestStatus, check_pending_change_request_status
from ..models.pending_change_request_target_type import (
    PendingChangeRequestTargetType,
    check_pending_change_request_target_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base import Base
    from ..models.node import Node
    from ..models.operation import Operation
    from ..models.pending_change_request_merge_summary import PendingChangeRequestMergeSummary
    from ..models.pending_change_request_review_policy_snapshot import PendingChangeRequestReviewPolicySnapshot
    from ..models.pending_change_request_source_meta import PendingChangeRequestSourceMeta
    from ..models.review import Review
    from ..models.source_attribution import SourceAttribution
    from ..models.user_ref import UserRef


T = TypeVar("T", bound="PendingChangeRequest")


@_attrs_define
class PendingChangeRequest:
    """
    Attributes:
        id (str):
        base_id (None | str):
        target_type (PendingChangeRequestTargetType):
        node_id (None | str):
        status (PendingChangeRequestStatus):
        submitted_by (str):
        source_meta (PendingChangeRequestSourceMeta):
        review_policy_snapshot (PendingChangeRequestReviewPolicySnapshot):
        merge_summary (PendingChangeRequestMergeSummary): Filled in when the change request merges. `slugChanges`
            (present only when non-empty) lists items a restore brought back under a new slug because another item took the
            old one while they were in the Trash: `{ nodeId, nodeType, name, fromSlug, toSlug }`. Read the new slug from
            here instead of assuming the old one.
        rejected_reason (None | str):
        reviewed_at (None | str):
        merged_at (None | str):
        created_at (str):
        updated_at (str):
        base (Base | None):
        node (Node | None):
        operations (list[Operation]):
        primary_operation (None | Operation):
        operation_count (float):
        reviews (list[Review]):
        materialized (Literal[False]):
        submitted_by_user (None | Unset | UserRef):
        source_attribution (None | SourceAttribution | Unset):
    """

    id: str
    base_id: None | str
    target_type: PendingChangeRequestTargetType
    node_id: None | str
    status: PendingChangeRequestStatus
    submitted_by: str
    source_meta: PendingChangeRequestSourceMeta
    review_policy_snapshot: PendingChangeRequestReviewPolicySnapshot
    merge_summary: PendingChangeRequestMergeSummary
    rejected_reason: None | str
    reviewed_at: None | str
    merged_at: None | str
    created_at: str
    updated_at: str
    base: Base | None
    node: Node | None
    operations: list[Operation]
    primary_operation: None | Operation
    operation_count: float
    reviews: list[Review]
    materialized: Literal[False]
    submitted_by_user: None | Unset | UserRef = UNSET
    source_attribution: None | SourceAttribution | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.base import Base
        from ..models.node import Node
        from ..models.operation import Operation
        from ..models.source_attribution import SourceAttribution
        from ..models.user_ref import UserRef

        id = self.id

        base_id: None | str
        base_id = self.base_id

        target_type: str = self.target_type

        node_id: None | str
        node_id = self.node_id

        status: str = self.status

        submitted_by = self.submitted_by

        source_meta = self.source_meta.to_dict()

        review_policy_snapshot = self.review_policy_snapshot.to_dict()

        merge_summary = self.merge_summary.to_dict()

        rejected_reason: None | str
        rejected_reason = self.rejected_reason

        reviewed_at: None | str
        reviewed_at = self.reviewed_at

        merged_at: None | str
        merged_at = self.merged_at

        created_at = self.created_at

        updated_at = self.updated_at

        base: dict[str, Any] | None
        if isinstance(self.base, Base):
            base = self.base.to_dict()
        else:
            base = self.base

        node: dict[str, Any] | None
        if isinstance(self.node, Node):
            node = self.node.to_dict()
        else:
            node = self.node

        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()
            operations.append(operations_item)

        primary_operation: dict[str, Any] | None
        if isinstance(self.primary_operation, Operation):
            primary_operation = self.primary_operation.to_dict()
        else:
            primary_operation = self.primary_operation

        operation_count = self.operation_count

        reviews = []
        for reviews_item_data in self.reviews:
            reviews_item = reviews_item_data.to_dict()
            reviews.append(reviews_item)

        materialized = self.materialized

        submitted_by_user: dict[str, Any] | None | Unset
        if isinstance(self.submitted_by_user, Unset):
            submitted_by_user = UNSET
        elif isinstance(self.submitted_by_user, UserRef):
            submitted_by_user = self.submitted_by_user.to_dict()
        else:
            submitted_by_user = self.submitted_by_user

        source_attribution: dict[str, Any] | None | Unset
        if isinstance(self.source_attribution, Unset):
            source_attribution = UNSET
        elif isinstance(self.source_attribution, SourceAttribution):
            source_attribution = self.source_attribution.to_dict()
        else:
            source_attribution = self.source_attribution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "baseId": base_id,
                "targetType": target_type,
                "nodeId": node_id,
                "status": status,
                "submittedBy": submitted_by,
                "sourceMeta": source_meta,
                "reviewPolicySnapshot": review_policy_snapshot,
                "mergeSummary": merge_summary,
                "rejectedReason": rejected_reason,
                "reviewedAt": reviewed_at,
                "mergedAt": merged_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "base": base,
                "node": node,
                "operations": operations,
                "primaryOperation": primary_operation,
                "operationCount": operation_count,
                "reviews": reviews,
                "materialized": materialized,
            }
        )
        if submitted_by_user is not UNSET:
            field_dict["submittedByUser"] = submitted_by_user
        if source_attribution is not UNSET:
            field_dict["sourceAttribution"] = source_attribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.base import Base
        from ..models.node import Node
        from ..models.operation import Operation
        from ..models.pending_change_request_merge_summary import PendingChangeRequestMergeSummary
        from ..models.pending_change_request_review_policy_snapshot import PendingChangeRequestReviewPolicySnapshot
        from ..models.pending_change_request_source_meta import PendingChangeRequestSourceMeta
        from ..models.review import Review
        from ..models.source_attribution import SourceAttribution
        from ..models.user_ref import UserRef

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_base_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        base_id = _parse_base_id(d.pop("baseId"))

        target_type = check_pending_change_request_target_type(d.pop("targetType"))

        def _parse_node_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        node_id = _parse_node_id(d.pop("nodeId"))

        status = check_pending_change_request_status(d.pop("status"))

        submitted_by = d.pop("submittedBy")

        source_meta = PendingChangeRequestSourceMeta.from_dict(d.pop("sourceMeta"))

        review_policy_snapshot = PendingChangeRequestReviewPolicySnapshot.from_dict(d.pop("reviewPolicySnapshot"))

        merge_summary = PendingChangeRequestMergeSummary.from_dict(d.pop("mergeSummary"))

        def _parse_rejected_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rejected_reason = _parse_rejected_reason(d.pop("rejectedReason"))

        def _parse_reviewed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewedAt"))

        def _parse_merged_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        merged_at = _parse_merged_at(d.pop("mergedAt"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_base(data: object) -> Base | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                base_type_0 = Base.from_dict(data)

                return base_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Base | None, data)

        base = _parse_base(d.pop("base"))

        def _parse_node(data: object) -> Node | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                node_type_0 = Node.from_dict(data)

                return node_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Node | None, data)

        node = _parse_node(d.pop("node"))

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = Operation.from_dict(operations_item_data)

            operations.append(operations_item)

        def _parse_primary_operation(data: object) -> None | Operation:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_operation_type_0 = Operation.from_dict(data)

                return primary_operation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Operation, data)

        primary_operation = _parse_primary_operation(d.pop("primaryOperation"))

        operation_count = d.pop("operationCount")

        reviews = []
        _reviews = d.pop("reviews")
        for reviews_item_data in _reviews:
            reviews_item = Review.from_dict(reviews_item_data)

            reviews.append(reviews_item)

        materialized = cast(Literal[False], d.pop("materialized"))
        if materialized != False:
            raise ValueError(f"materialized must match const False, got '{materialized}'")

        def _parse_submitted_by_user(data: object) -> None | Unset | UserRef:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                submitted_by_user_type_0 = UserRef.from_dict(data)

                return submitted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserRef, data)

        submitted_by_user = _parse_submitted_by_user(d.pop("submittedByUser", UNSET))

        def _parse_source_attribution(data: object) -> None | SourceAttribution | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_attribution_type_0 = SourceAttribution.from_dict(data)

                return source_attribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceAttribution | Unset, data)

        source_attribution = _parse_source_attribution(d.pop("sourceAttribution", UNSET))

        pending_change_request = cls(
            id=id,
            base_id=base_id,
            target_type=target_type,
            node_id=node_id,
            status=status,
            submitted_by=submitted_by,
            source_meta=source_meta,
            review_policy_snapshot=review_policy_snapshot,
            merge_summary=merge_summary,
            rejected_reason=rejected_reason,
            reviewed_at=reviewed_at,
            merged_at=merged_at,
            created_at=created_at,
            updated_at=updated_at,
            base=base,
            node=node,
            operations=operations,
            primary_operation=primary_operation,
            operation_count=operation_count,
            reviews=reviews,
            materialized=materialized,
            submitted_by_user=submitted_by_user,
            source_attribution=source_attribution,
        )

        pending_change_request.additional_properties = d
        return pending_change_request

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
