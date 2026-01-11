from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePackagesBody")


@_attrs_define
class CreatePackagesBody:
    """
    Attributes:
        lookup_key (str): The lookup_key of the package Example: monthly.
        display_name (str): The display name of the package Example: monthly with one-week trial.
        position (int | Unset): The position of the package in the offering Example: 1.
    """

    lookup_key: str
    display_name: str
    position: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        lookup_key = self.lookup_key

        display_name = self.display_name

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "lookup_key": lookup_key,
                "display_name": display_name,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lookup_key = d.pop("lookup_key")

        display_name = d.pop("display_name")

        position = d.pop("position", UNSET)

        create_packages_body = cls(
            lookup_key=lookup_key,
            display_name=display_name,
            position=position,
        )

        return create_packages_body
