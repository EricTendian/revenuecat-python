from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreatePaywallBody")


@_attrs_define
class CreatePaywallBody:
    """
    Attributes:
        offering_id (str): The ID of the offering the paywall will be created for.
             Example: ofrng123456789a.
    """

    offering_id: str

    def to_dict(self) -> dict[str, Any]:
        offering_id = self.offering_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offering_id": offering_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offering_id = d.pop("offering_id")

        create_paywall_body = cls(
            offering_id=offering_id,
        )

        return create_paywall_body
