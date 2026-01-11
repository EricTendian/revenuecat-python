from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roku_app_roku import RokuAppRoku


T = TypeVar("T", bound="RokuApp")


@_attrs_define
class RokuApp:
    """
    Attributes:
        roku (RokuAppRoku | Unset): Roku Channel Store type details
    """

    roku: RokuAppRoku | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        roku: dict[str, Any] | Unset = UNSET
        if not isinstance(self.roku, Unset):
            roku = self.roku.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if roku is not UNSET:
            field_dict["roku"] = roku

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roku_app_roku import RokuAppRoku

        d = dict(src_dict)
        _roku = d.pop("roku", UNSET)
        roku: RokuAppRoku | Unset
        if isinstance(_roku, Unset):
            roku = UNSET
        else:
            roku = RokuAppRoku.from_dict(_roku)

        roku_app = cls(
            roku=roku,
        )

        roku_app.additional_properties = d
        return roku_app

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
