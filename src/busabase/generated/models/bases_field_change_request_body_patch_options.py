from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bases_field_change_request_body_patch_options_ai import BasesFieldChangeRequestBodyPatchOptionsAi
    from ..models.bases_field_change_request_body_patch_options_attachment import (
        BasesFieldChangeRequestBodyPatchOptionsAttachment,
    )
    from ..models.bases_field_change_request_body_patch_options_choices_item import (
        BasesFieldChangeRequestBodyPatchOptionsChoicesItem,
    )
    from ..models.bases_field_change_request_body_patch_options_code import BasesFieldChangeRequestBodyPatchOptionsCode
    from ..models.bases_field_change_request_body_patch_options_date import BasesFieldChangeRequestBodyPatchOptionsDate
    from ..models.bases_field_change_request_body_patch_options_embed import (
        BasesFieldChangeRequestBodyPatchOptionsEmbed,
    )
    from ..models.bases_field_change_request_body_patch_options_formula import (
        BasesFieldChangeRequestBodyPatchOptionsFormula,
    )
    from ..models.bases_field_change_request_body_patch_options_help import BasesFieldChangeRequestBodyPatchOptionsHelp
    from ..models.bases_field_change_request_body_patch_options_lookup import (
        BasesFieldChangeRequestBodyPatchOptionsLookup,
    )
    from ..models.bases_field_change_request_body_patch_options_number import (
        BasesFieldChangeRequestBodyPatchOptionsNumber,
    )


T = TypeVar("T", bound="BasesFieldChangeRequestBodyPatchOptions")


@_attrs_define
class BasesFieldChangeRequestBodyPatchOptions:
    """
    Attributes:
        help_ (BasesFieldChangeRequestBodyPatchOptionsHelp | Unset):
        ai (BasesFieldChangeRequestBodyPatchOptionsAi | Unset):
        attachment (BasesFieldChangeRequestBodyPatchOptionsAttachment | Unset):
        choices (list[BasesFieldChangeRequestBodyPatchOptionsChoicesItem] | Unset):
        code (BasesFieldChangeRequestBodyPatchOptionsCode | Unset):
        date (BasesFieldChangeRequestBodyPatchOptionsDate | Unset):
        embed (BasesFieldChangeRequestBodyPatchOptionsEmbed | Unset):
        formula (BasesFieldChangeRequestBodyPatchOptionsFormula | Unset):
        inverse_field_id (str | Unset):
        lookup (BasesFieldChangeRequestBodyPatchOptionsLookup | Unset):
        multiple (bool | Unset):
        number (BasesFieldChangeRequestBodyPatchOptionsNumber | Unset):
        target_base_id (str | Unset): Relation target Base id (bse_…). Or pass targetBaseSlug to name it by slug.
        target_base_slug (str | Unset): Relation target Base by slug — a convenience alias for targetBaseId, resolved
            server-side (active bases in the current space). If both are given, targetBaseId wins.
    """

    help_: BasesFieldChangeRequestBodyPatchOptionsHelp | Unset = UNSET
    ai: BasesFieldChangeRequestBodyPatchOptionsAi | Unset = UNSET
    attachment: BasesFieldChangeRequestBodyPatchOptionsAttachment | Unset = UNSET
    choices: list[BasesFieldChangeRequestBodyPatchOptionsChoicesItem] | Unset = UNSET
    code: BasesFieldChangeRequestBodyPatchOptionsCode | Unset = UNSET
    date: BasesFieldChangeRequestBodyPatchOptionsDate | Unset = UNSET
    embed: BasesFieldChangeRequestBodyPatchOptionsEmbed | Unset = UNSET
    formula: BasesFieldChangeRequestBodyPatchOptionsFormula | Unset = UNSET
    inverse_field_id: str | Unset = UNSET
    lookup: BasesFieldChangeRequestBodyPatchOptionsLookup | Unset = UNSET
    multiple: bool | Unset = UNSET
    number: BasesFieldChangeRequestBodyPatchOptionsNumber | Unset = UNSET
    target_base_id: str | Unset = UNSET
    target_base_slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        help_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.help_, Unset):
            help_ = self.help_.to_dict()

        ai: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ai, Unset):
            ai = self.ai.to_dict()

        attachment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = self.attachment.to_dict()

        choices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.choices, Unset):
            choices = []
            for choices_item_data in self.choices:
                choices_item = choices_item_data.to_dict()
                choices.append(choices_item)

        code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.to_dict()

        date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        embed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embed, Unset):
            embed = self.embed.to_dict()

        formula: dict[str, Any] | Unset = UNSET
        if not isinstance(self.formula, Unset):
            formula = self.formula.to_dict()

        inverse_field_id = self.inverse_field_id

        lookup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lookup, Unset):
            lookup = self.lookup.to_dict()

        multiple = self.multiple

        number: dict[str, Any] | Unset = UNSET
        if not isinstance(self.number, Unset):
            number = self.number.to_dict()

        target_base_id = self.target_base_id

        target_base_slug = self.target_base_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if help_ is not UNSET:
            field_dict["help"] = help_
        if ai is not UNSET:
            field_dict["ai"] = ai
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if choices is not UNSET:
            field_dict["choices"] = choices
        if code is not UNSET:
            field_dict["code"] = code
        if date is not UNSET:
            field_dict["date"] = date
        if embed is not UNSET:
            field_dict["embed"] = embed
        if formula is not UNSET:
            field_dict["formula"] = formula
        if inverse_field_id is not UNSET:
            field_dict["inverseFieldId"] = inverse_field_id
        if lookup is not UNSET:
            field_dict["lookup"] = lookup
        if multiple is not UNSET:
            field_dict["multiple"] = multiple
        if number is not UNSET:
            field_dict["number"] = number
        if target_base_id is not UNSET:
            field_dict["targetBaseId"] = target_base_id
        if target_base_slug is not UNSET:
            field_dict["targetBaseSlug"] = target_base_slug

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bases_field_change_request_body_patch_options_ai import BasesFieldChangeRequestBodyPatchOptionsAi
        from ..models.bases_field_change_request_body_patch_options_attachment import (
            BasesFieldChangeRequestBodyPatchOptionsAttachment,
        )
        from ..models.bases_field_change_request_body_patch_options_choices_item import (
            BasesFieldChangeRequestBodyPatchOptionsChoicesItem,
        )
        from ..models.bases_field_change_request_body_patch_options_code import (
            BasesFieldChangeRequestBodyPatchOptionsCode,
        )
        from ..models.bases_field_change_request_body_patch_options_date import (
            BasesFieldChangeRequestBodyPatchOptionsDate,
        )
        from ..models.bases_field_change_request_body_patch_options_embed import (
            BasesFieldChangeRequestBodyPatchOptionsEmbed,
        )
        from ..models.bases_field_change_request_body_patch_options_formula import (
            BasesFieldChangeRequestBodyPatchOptionsFormula,
        )
        from ..models.bases_field_change_request_body_patch_options_help import (
            BasesFieldChangeRequestBodyPatchOptionsHelp,
        )
        from ..models.bases_field_change_request_body_patch_options_lookup import (
            BasesFieldChangeRequestBodyPatchOptionsLookup,
        )
        from ..models.bases_field_change_request_body_patch_options_number import (
            BasesFieldChangeRequestBodyPatchOptionsNumber,
        )

        d = dict(src_dict)
        _help_ = d.pop("help", UNSET)
        help_: BasesFieldChangeRequestBodyPatchOptionsHelp | Unset
        if isinstance(_help_, Unset):
            help_ = UNSET
        else:
            help_ = BasesFieldChangeRequestBodyPatchOptionsHelp.from_dict(_help_)

        _ai = d.pop("ai", UNSET)
        ai: BasesFieldChangeRequestBodyPatchOptionsAi | Unset
        if isinstance(_ai, Unset):
            ai = UNSET
        else:
            ai = BasesFieldChangeRequestBodyPatchOptionsAi.from_dict(_ai)

        _attachment = d.pop("attachment", UNSET)
        attachment: BasesFieldChangeRequestBodyPatchOptionsAttachment | Unset
        if isinstance(_attachment, Unset):
            attachment = UNSET
        else:
            attachment = BasesFieldChangeRequestBodyPatchOptionsAttachment.from_dict(_attachment)

        _choices = d.pop("choices", UNSET)
        choices: list[BasesFieldChangeRequestBodyPatchOptionsChoicesItem] | Unset = UNSET
        if _choices is not UNSET:
            choices = []
            for choices_item_data in _choices:
                choices_item = BasesFieldChangeRequestBodyPatchOptionsChoicesItem.from_dict(choices_item_data)

                choices.append(choices_item)

        _code = d.pop("code", UNSET)
        code: BasesFieldChangeRequestBodyPatchOptionsCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = BasesFieldChangeRequestBodyPatchOptionsCode.from_dict(_code)

        _date = d.pop("date", UNSET)
        date: BasesFieldChangeRequestBodyPatchOptionsDate | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = BasesFieldChangeRequestBodyPatchOptionsDate.from_dict(_date)

        _embed = d.pop("embed", UNSET)
        embed: BasesFieldChangeRequestBodyPatchOptionsEmbed | Unset
        if isinstance(_embed, Unset):
            embed = UNSET
        else:
            embed = BasesFieldChangeRequestBodyPatchOptionsEmbed.from_dict(_embed)

        _formula = d.pop("formula", UNSET)
        formula: BasesFieldChangeRequestBodyPatchOptionsFormula | Unset
        if isinstance(_formula, Unset):
            formula = UNSET
        else:
            formula = BasesFieldChangeRequestBodyPatchOptionsFormula.from_dict(_formula)

        inverse_field_id = d.pop("inverseFieldId", UNSET)

        _lookup = d.pop("lookup", UNSET)
        lookup: BasesFieldChangeRequestBodyPatchOptionsLookup | Unset
        if isinstance(_lookup, Unset):
            lookup = UNSET
        else:
            lookup = BasesFieldChangeRequestBodyPatchOptionsLookup.from_dict(_lookup)

        multiple = d.pop("multiple", UNSET)

        _number = d.pop("number", UNSET)
        number: BasesFieldChangeRequestBodyPatchOptionsNumber | Unset
        if isinstance(_number, Unset):
            number = UNSET
        else:
            number = BasesFieldChangeRequestBodyPatchOptionsNumber.from_dict(_number)

        target_base_id = d.pop("targetBaseId", UNSET)

        target_base_slug = d.pop("targetBaseSlug", UNSET)

        bases_field_change_request_body_patch_options = cls(
            help_=help_,
            ai=ai,
            attachment=attachment,
            choices=choices,
            code=code,
            date=date,
            embed=embed,
            formula=formula,
            inverse_field_id=inverse_field_id,
            lookup=lookup,
            multiple=multiple,
            number=number,
            target_base_id=target_base_id,
            target_base_slug=target_base_slug,
        )

        bases_field_change_request_body_patch_options.additional_properties = d
        return bases_field_change_request_body_patch_options

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
