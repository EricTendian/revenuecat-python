from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateEntitlementBody")


@_attrs_define
class UpdateEntitlementBody:
    """
    Attributes:
        display_name (str): The display name of the entitlement Example: Premium.
    """

    display_name: str

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "display_name": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        update_entitlement_body = cls(
            display_name=display_name,
        )

        return update_entitlement_body
