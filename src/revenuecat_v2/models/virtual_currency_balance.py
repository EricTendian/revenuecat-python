from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.virtual_currency_balance_object import VirtualCurrencyBalanceObject
from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualCurrencyBalance")


@_attrs_define
class VirtualCurrencyBalance:
    """
    Attributes:
        object_ (VirtualCurrencyBalanceObject): String representing the object's type. Objects of the same type share
            the same value.
        currency_code (str): The code of the virtual currency.
        balance (int): The balance of the virtual currency.
        description (str | Unset): The description of the virtual currency.
        name (str | Unset): The name of the virtual currency.
    """

    object_: VirtualCurrencyBalanceObject
    currency_code: str
    balance: int
    description: str | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        currency_code = self.currency_code

        balance = self.balance

        description = self.description

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "currency_code": currency_code,
                "balance": balance,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = VirtualCurrencyBalanceObject(d.pop("object"))

        currency_code = d.pop("currency_code")

        balance = d.pop("balance")

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        virtual_currency_balance = cls(
            object_=object_,
            currency_code=currency_code,
            balance=balance,
            description=description,
            name=name,
        )

        return virtual_currency_balance
