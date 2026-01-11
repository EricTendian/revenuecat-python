from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateEntitlementBody")


@_attrs_define
class CreateEntitlementBody:
    """
    Attributes:
        lookup_key (str): The identifier of the entitlement Example: premium.
        display_name (str): The display name of the entitlement Example: Premium access to all features.
    """

    lookup_key: str
    display_name: str

    def to_dict(self) -> dict[str, Any]:
        lookup_key = self.lookup_key

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "lookup_key": lookup_key,
                "display_name": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lookup_key = d.pop("lookup_key")

        display_name = d.pop("display_name")

        create_entitlement_body = cls(
            lookup_key=lookup_key,
            display_name=display_name,
        )

        return create_entitlement_body
