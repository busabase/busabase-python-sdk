from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bases_field_change_request_body_new_type import (
    BasesFieldChangeRequestBodyNewType,
    check_bases_field_change_request_body_new_type,
)
from ..models.bases_field_change_request_body_select_choice_mode import (
    BasesFieldChangeRequestBodySelectChoiceMode,
    check_bases_field_change_request_body_select_choice_mode,
)
from ..models.bases_field_change_request_body_type import (
    BasesFieldChangeRequestBodyType,
    check_bases_field_change_request_body_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bases_field_change_request_body_name_type_1 import BasesFieldChangeRequestBodyNameType1
    from ..models.bases_field_change_request_body_patch import BasesFieldChangeRequestBodyPatch
    from ..models.field_options import FieldOptions


T = TypeVar("T", bound="BasesFieldChangeRequestBody")


@_attrs_define
class BasesFieldChangeRequestBody:
    """
    Attributes:
        operation (Literal['convert'] | Literal['create'] | Literal['delete'] | Literal['reorder'] | Literal['restore']
            | Literal['update']):
        name (BasesFieldChangeRequestBodyNameType1 | str | Unset):
        slug (str | Unset):
        type_ (BasesFieldChangeRequestBodyType | Unset):  Default: 'text'.
        required (bool | Unset):  Default: False.
        options (FieldOptions | Unset):
        message (str | Unset):
        submitted_by (str | Unset):  Default: 'local-editor'.
        auto_merge (bool | Unset):
        field_id (str | Unset):
        patch (BasesFieldChangeRequestBodyPatch | Unset):
        new_type (BasesFieldChangeRequestBodyNewType | Unset):
        select_choice_mode (BasesFieldChangeRequestBodySelectChoiceMode | Unset):  Default: 'null_on_missing'.
        field_ids (list[str] | Unset):
    """

    operation: Literal["convert", "create", "delete", "reorder", "restore", "update"]
    name: BasesFieldChangeRequestBodyNameType1 | str | Unset = UNSET
    slug: str | Unset = UNSET
    type_: BasesFieldChangeRequestBodyType | Unset = "text"
    required: bool | Unset = False
    options: FieldOptions | Unset = UNSET
    message: str | Unset = UNSET
    submitted_by: str | Unset = "local-editor"
    auto_merge: bool | Unset = UNSET
    field_id: str | Unset = UNSET
    patch: BasesFieldChangeRequestBodyPatch | Unset = UNSET
    new_type: BasesFieldChangeRequestBodyNewType | Unset = UNSET
    select_choice_mode: BasesFieldChangeRequestBodySelectChoiceMode | Unset = "null_on_missing"
    field_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bases_field_change_request_body_name_type_1 import BasesFieldChangeRequestBodyNameType1

        operation: Literal["convert", "create", "delete", "reorder", "restore", "update"]
        operation = self.operation

        name: dict[str, Any] | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, BasesFieldChangeRequestBodyNameType1):
            name = self.name.to_dict()
        else:
            name = self.name

        slug = self.slug

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        required = self.required

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        message: str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        submitted_by = self.submitted_by

        auto_merge: bool | Unset
        if isinstance(self.auto_merge, Unset):
            auto_merge = UNSET
        else:
            auto_merge = self.auto_merge

        field_id = self.field_id

        patch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.patch, Unset):
            patch = self.patch.to_dict()

        new_type: str | Unset = UNSET
        if not isinstance(self.new_type, Unset):
            new_type = self.new_type

        select_choice_mode: str | Unset = UNSET
        if not isinstance(self.select_choice_mode, Unset):
            select_choice_mode = self.select_choice_mode

        field_ids: list[str] | Unset = UNSET
        if not isinstance(self.field_ids, Unset):
            field_ids = self.field_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if type_ is not UNSET:
            field_dict["type"] = type_
        if required is not UNSET:
            field_dict["required"] = required
        if options is not UNSET:
            field_dict["options"] = options
        if message is not UNSET:
            field_dict["message"] = message
        if submitted_by is not UNSET:
            field_dict["submittedBy"] = submitted_by
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if patch is not UNSET:
            field_dict["patch"] = patch
        if new_type is not UNSET:
            field_dict["newType"] = new_type
        if select_choice_mode is not UNSET:
            field_dict["selectChoiceMode"] = select_choice_mode
        if field_ids is not UNSET:
            field_dict["fieldIds"] = field_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bases_field_change_request_body_name_type_1 import BasesFieldChangeRequestBodyNameType1
        from ..models.bases_field_change_request_body_patch import BasesFieldChangeRequestBodyPatch
        from ..models.field_options import FieldOptions

        d = dict(src_dict)

        def _parse_operation(data: object) -> Literal["convert", "create", "delete", "reorder", "restore", "update"]:
            operation_type_0 = cast(Literal["create"], data)
            if operation_type_0 != "create":
                raise ValueError(f"operation_type_0 must match const 'create', got '{operation_type_0}'")
            return operation_type_0
            operation_type_1 = cast(Literal["update"], data)
            if operation_type_1 != "update":
                raise ValueError(f"operation_type_1 must match const 'update', got '{operation_type_1}'")
            return operation_type_1
            operation_type_2 = cast(Literal["delete"], data)
            if operation_type_2 != "delete":
                raise ValueError(f"operation_type_2 must match const 'delete', got '{operation_type_2}'")
            return operation_type_2
            operation_type_3 = cast(Literal["convert"], data)
            if operation_type_3 != "convert":
                raise ValueError(f"operation_type_3 must match const 'convert', got '{operation_type_3}'")
            return operation_type_3
            operation_type_4 = cast(Literal["reorder"], data)
            if operation_type_4 != "reorder":
                raise ValueError(f"operation_type_4 must match const 'reorder', got '{operation_type_4}'")
            return operation_type_4
            operation_type_5 = cast(Literal["restore"], data)
            if operation_type_5 != "restore":
                raise ValueError(f"operation_type_5 must match const 'restore', got '{operation_type_5}'")
            return operation_type_5

        operation = _parse_operation(d.pop("operation"))

        def _parse_name(data: object) -> BasesFieldChangeRequestBodyNameType1 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_type_1 = BasesFieldChangeRequestBodyNameType1.from_dict(data)

                return name_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BasesFieldChangeRequestBodyNameType1 | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        slug = d.pop("slug", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: BasesFieldChangeRequestBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_bases_field_change_request_body_type(_type_)

        required = d.pop("required", UNSET)

        _options = d.pop("options", UNSET)
        options: FieldOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = FieldOptions.from_dict(_options)

        def _parse_message(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        submitted_by = d.pop("submittedBy", UNSET)

        def _parse_auto_merge(data: object) -> bool | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset, data)

        auto_merge = _parse_auto_merge(d.pop("autoMerge", UNSET))

        field_id = d.pop("fieldId", UNSET)

        _patch = d.pop("patch", UNSET)
        patch: BasesFieldChangeRequestBodyPatch | Unset
        if isinstance(_patch, Unset):
            patch = UNSET
        else:
            patch = BasesFieldChangeRequestBodyPatch.from_dict(_patch)

        _new_type = d.pop("newType", UNSET)
        new_type: BasesFieldChangeRequestBodyNewType | Unset
        if isinstance(_new_type, Unset):
            new_type = UNSET
        else:
            new_type = check_bases_field_change_request_body_new_type(_new_type)

        _select_choice_mode = d.pop("selectChoiceMode", UNSET)
        select_choice_mode: BasesFieldChangeRequestBodySelectChoiceMode | Unset
        if isinstance(_select_choice_mode, Unset):
            select_choice_mode = UNSET
        else:
            select_choice_mode = check_bases_field_change_request_body_select_choice_mode(_select_choice_mode)

        field_ids = cast(list[str], d.pop("fieldIds", UNSET))

        bases_field_change_request_body = cls(
            operation=operation,
            name=name,
            slug=slug,
            type_=type_,
            required=required,
            options=options,
            message=message,
            submitted_by=submitted_by,
            auto_merge=auto_merge,
            field_id=field_id,
            patch=patch,
            new_type=new_type,
            select_choice_mode=select_choice_mode,
            field_ids=field_ids,
        )

        bases_field_change_request_body.additional_properties = d
        return bases_field_change_request_body

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
