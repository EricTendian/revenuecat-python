from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.customer_entitlement_object import CustomerEntitlementObject

T = TypeVar("T", bound="CustomerEntitlement")


@_attrs_define
class CustomerEntitlement:
    """
    Attributes:
        object_ (CustomerEntitlementObject): String representing the object's type. Objects of the same type share the
            same value.
        entitlement_id (str): ID of the entitlement granted to the customer Example: entla1b2c3d4e5.
        expires_at (int | None): The date after which the access to the entitlement expires in ms since epoch Example:
            1658399423658.
    """

    object_: CustomerEntitlementObject
    entitlement_id: str
    expires_at: int | None

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        entitlement_id = self.entitlement_id

        expires_at: int | None
        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "entitlement_id": entitlement_id,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = CustomerEntitlementObject(d.pop("object"))

        entitlement_id = d.pop("entitlement_id")

        def _parse_expires_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        customer_entitlement = cls(
            object_=object_,
            entitlement_id=entitlement_id,
            expires_at=expires_at,
        )

        return customer_entitlement
