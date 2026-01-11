from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GrantCustomerEntitlementBody")


@_attrs_define
class GrantCustomerEntitlementBody:
    """
    Attributes:
        entitlement_id (str): The ID of the entitlement to grant to the customer. Example: entla1b2c3d4e5.
        expires_at (int): The date after which the access to the entitlement expires in ms since epoch. Example:
            1658399423658.
    """

    entitlement_id: str
    expires_at: int

    def to_dict(self) -> dict[str, Any]:
        entitlement_id = self.entitlement_id

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entitlement_id": entitlement_id,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entitlement_id = d.pop("entitlement_id")

        expires_at = d.pop("expires_at")

        grant_customer_entitlement_body = cls(
            entitlement_id=entitlement_id,
            expires_at=expires_at,
        )

        return grant_customer_entitlement_body
