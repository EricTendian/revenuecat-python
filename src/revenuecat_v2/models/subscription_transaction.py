from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.subscription_transaction_object import SubscriptionTransactionObject

T = TypeVar("T", bound="SubscriptionTransaction")


@_attrs_define
class SubscriptionTransaction:
    """
    Attributes:
        object_ (SubscriptionTransactionObject): String representing the object's type. Objects of the same type share
            the same value.
        id (str): The ID of the subscription transaction in the store Example: GPA.0000-0000-0000-00000.
        purchased_at (int): The date of the transaction in ms since epoch Example: 1658399423658.
    """

    object_: SubscriptionTransactionObject
    id: str
    purchased_at: int

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        purchased_at = self.purchased_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "purchased_at": purchased_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = SubscriptionTransactionObject(d.pop("object"))

        id = d.pop("id")

        purchased_at = d.pop("purchased_at")

        subscription_transaction = cls(
            object_=object_,
            id=id,
            purchased_at=purchased_at,
        )

        return subscription_transaction
