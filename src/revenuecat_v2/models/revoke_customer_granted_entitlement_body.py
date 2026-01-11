from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RevokeCustomerGrantedEntitlementBody")


@_attrs_define
class RevokeCustomerGrantedEntitlementBody:
    """
    Attributes:
        entitlement_id (str): The ID of the granted entitlement to revoke from the customer. Example: entla1b2c3d4e5.
    """

    entitlement_id: str

    def to_dict(self) -> dict[str, Any]:
        entitlement_id = self.entitlement_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entitlement_id": entitlement_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entitlement_id = d.pop("entitlement_id")

        revoke_customer_granted_entitlement_body = cls(
            entitlement_id=entitlement_id,
        )

        return revoke_customer_granted_entitlement_body
