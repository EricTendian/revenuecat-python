from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePackageBody")


@_attrs_define
class UpdatePackageBody:
    """
    Attributes:
        display_name (str | Unset): The display name of the package Example: monthly with one-week trial.
        position (int | Unset): The position of the package within the offering Example: 2.
    """

    display_name: str | Unset = UNSET
    position: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        position = d.pop("position", UNSET)

        update_package_body = cls(
            display_name=display_name,
            position=position,
        )

        return update_package_body
