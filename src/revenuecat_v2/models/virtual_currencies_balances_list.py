from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.virtual_currencies_balances_list_object import VirtualCurrenciesBalancesListObject

if TYPE_CHECKING:
    from ..models.virtual_currency_balance import VirtualCurrencyBalance


T = TypeVar("T", bound="VirtualCurrenciesBalancesList")


@_attrs_define
class VirtualCurrenciesBalancesList:
    """
    Attributes:
        object_ (VirtualCurrenciesBalancesListObject): String representing the object's type. Objects of the same type
            share the same value.
        items (list[VirtualCurrencyBalance]): Details about each object.
        next_page (None | str): URL to access the next page of the customer's balances. If not present / null, there is
            no next page Example: /v2/projects/proj1ab2c3d4/customers/19b8de26-77c1-49f1-aa18-
            019a391603e2/virtual_currencies?starting_after=9fjeja8fjed.
        url (str): The URL where this list can be accessed. Example:
            /v2/projects/proj1ab2c3d4/customers/19b8de26-77c1-49f1-aa18-019a391603e2/virtual_currencies.
    """

    object_: VirtualCurrenciesBalancesListObject
    items: list[VirtualCurrencyBalance]
    next_page: None | str
    url: str

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_page: None | str
        next_page = self.next_page

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "items": items,
                "next_page": next_page,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.virtual_currency_balance import VirtualCurrencyBalance

        d = dict(src_dict)
        object_ = VirtualCurrenciesBalancesListObject(d.pop("object"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = VirtualCurrencyBalance.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_page(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_page = _parse_next_page(d.pop("next_page"))

        url = d.pop("url")

        virtual_currencies_balances_list = cls(
            object_=object_,
            items=items,
            next_page=next_page,
            url=url,
        )

        return virtual_currencies_balances_list
