from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.node_settings_airapp_engine_type_0 import (
    NodeSettingsAirappEngineType0,
    check_node_settings_airapp_engine_type_0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeSettings")


@_attrs_define
class NodeSettings:
    """
    Attributes:
        airapp_engine (NodeSettingsAirappEngineType0 | None | Unset):
    """

    airapp_engine: NodeSettingsAirappEngineType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        airapp_engine: None | str | Unset
        if isinstance(self.airapp_engine, Unset):
            airapp_engine = UNSET
        elif isinstance(self.airapp_engine, str):
            airapp_engine = self.airapp_engine
        else:
            airapp_engine = self.airapp_engine

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if airapp_engine is not UNSET:
            field_dict["airappEngine"] = airapp_engine

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_airapp_engine(data: object) -> NodeSettingsAirappEngineType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airapp_engine_type_0 = check_node_settings_airapp_engine_type_0(data)

                return airapp_engine_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NodeSettingsAirappEngineType0 | None | Unset, data)

        airapp_engine = _parse_airapp_engine(d.pop("airappEngine", UNSET))

        node_settings = cls(
            airapp_engine=airapp_engine,
        )

        return node_settings
