from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bases_field_change_request_body_patch_help_type_0 import BasesFieldChangeRequestBodyPatchHelpType0
    from ..models.bases_field_change_request_body_patch_name_type_1 import BasesFieldChangeRequestBodyPatchNameType1
    from ..models.bases_field_change_request_body_patch_options import BasesFieldChangeRequestBodyPatchOptions


T = TypeVar("T", bound="BasesFieldChangeRequestBodyPatch")


@_attrs_define
class BasesFieldChangeRequestBodyPatch:
    """
    Attributes:
        name (BasesFieldChangeRequestBodyPatchNameType1 | str | Unset):
        required (bool | Unset):
        options (BasesFieldChangeRequestBodyPatchOptions | Unset):
        help_ (BasesFieldChangeRequestBodyPatchHelpType0 | None | Unset):
        type_ (Any | Unset):
    """

    name: BasesFieldChangeRequestBodyPatchNameType1 | str | Unset = UNSET
    required: bool | Unset = UNSET
    options: BasesFieldChangeRequestBodyPatchOptions | Unset = UNSET
    help_: BasesFieldChangeRequestBodyPatchHelpType0 | None | Unset = UNSET
    type_: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bases_field_change_request_body_patch_help_type_0 import BasesFieldChangeRequestBodyPatchHelpType0
        from ..models.bases_field_change_request_body_patch_name_type_1 import BasesFieldChangeRequestBodyPatchNameType1

        name: dict[str, Any] | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, BasesFieldChangeRequestBodyPatchNameType1):
            name = self.name.to_dict()
        else:
            name = self.name

        required = self.required

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        help_: dict[str, Any] | None | Unset
        if isinstance(self.help_, Unset):
            help_ = UNSET
        elif isinstance(self.help_, BasesFieldChangeRequestBodyPatchHelpType0):
            help_ = self.help_.to_dict()
        else:
            help_ = self.help_

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if required is not UNSET:
            field_dict["required"] = required
        if options is not UNSET:
            field_dict["options"] = options
        if help_ is not UNSET:
            field_dict["help"] = help_
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bases_field_change_request_body_patch_help_type_0 import BasesFieldChangeRequestBodyPatchHelpType0
        from ..models.bases_field_change_request_body_patch_name_type_1 import BasesFieldChangeRequestBodyPatchNameType1
        from ..models.bases_field_change_request_body_patch_options import BasesFieldChangeRequestBodyPatchOptions

        d = dict(src_dict)

        def _parse_name(data: object) -> BasesFieldChangeRequestBodyPatchNameType1 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_type_1 = BasesFieldChangeRequestBodyPatchNameType1.from_dict(data)

                return name_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BasesFieldChangeRequestBodyPatchNameType1 | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        required = d.pop("required", UNSET)

        _options = d.pop("options", UNSET)
        options: BasesFieldChangeRequestBodyPatchOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = BasesFieldChangeRequestBodyPatchOptions.from_dict(_options)

        def _parse_help_(data: object) -> BasesFieldChangeRequestBodyPatchHelpType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                help_type_0 = BasesFieldChangeRequestBodyPatchHelpType0.from_dict(data)

                return help_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BasesFieldChangeRequestBodyPatchHelpType0 | None | Unset, data)

        help_ = _parse_help_(d.pop("help", UNSET))

        type_ = d.pop("type", UNSET)

        bases_field_change_request_body_patch = cls(
            name=name,
            required=required,
            options=options,
            help_=help_,
            type_=type_,
        )

        bases_field_change_request_body_patch.additional_properties = d
        return bases_field_change_request_body_patch

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
