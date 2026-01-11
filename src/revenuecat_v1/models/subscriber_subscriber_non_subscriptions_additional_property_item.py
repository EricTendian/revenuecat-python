from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_subscriber_non_subscriptions_additional_property_item_price import (
        SubscriberSubscriberNonSubscriptionsAdditionalPropertyItemPrice,
    )


T = TypeVar("T", bound="SubscriberSubscriberNonSubscriptionsAdditionalPropertyItem")


@_attrs_define
class SubscriberSubscriberNonSubscriptionsAdditionalPropertyItem:
    """
    Attributes:
        display_name (str | Unset): The display name of the product as configured in the RevenueCat dashboard. Example:
            Lifetime Access.
        id (str | Unset): A unique ID of the purchase. Example: cadba0c81b.
        is_sandbox (bool | Unset): Whether or not the purchase was made in sandbox mode.
        price (SubscriberSubscriberNonSubscriptionsAdditionalPropertyItemPrice | Unset): The price of the transaction in
            the currency the product was purchased in.
        purchase_date (str | Unset): Date of the purchase (in ISO 8601 format). Example: 2019-04-05T21:52:45Z.
        store (str | Unset): Identifier of the store of the purchase:
            - `app_store`: The product was purchased through Apple App Store.
            - `mac_app_store`: The product was purchased through the Mac App Store.
            - `play_store`: The product was purchased through the Google Play Store.
            - `amazon`: The product was purchased through the Amazon Appstore.
            - `stripe`: The product was purchased through Stripe.
            - `roku`: The product was purchased through Roku.
            - `paddle`: The product was purchased through Paddle.
             Example: app_store.
        store_transaction_id (str | Unset): The identifier associated with the purchase in the underlying store.
            Example: 1000000819074923.
    """

    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    is_sandbox: bool | Unset = UNSET
    price: SubscriberSubscriberNonSubscriptionsAdditionalPropertyItemPrice | Unset = UNSET
    purchase_date: str | Unset = UNSET
    store: str | Unset = UNSET
    store_transaction_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        id = self.id

        is_sandbox = self.is_sandbox

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        purchase_date = self.purchase_date

        store = self.store

        store_transaction_id = self.store_transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if is_sandbox is not UNSET:
            field_dict["is_sandbox"] = is_sandbox
        if price is not UNSET:
            field_dict["price"] = price
        if purchase_date is not UNSET:
            field_dict["purchase_date"] = purchase_date
        if store is not UNSET:
            field_dict["store"] = store
        if store_transaction_id is not UNSET:
            field_dict["store_transaction_id"] = store_transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscriber_subscriber_non_subscriptions_additional_property_item_price import (
            SubscriberSubscriberNonSubscriptionsAdditionalPropertyItemPrice,
        )

        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        is_sandbox = d.pop("is_sandbox", UNSET)

        _price = d.pop("price", UNSET)
        price: SubscriberSubscriberNonSubscriptionsAdditionalPropertyItemPrice | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = SubscriberSubscriberNonSubscriptionsAdditionalPropertyItemPrice.from_dict(_price)

        purchase_date = d.pop("purchase_date", UNSET)

        store = d.pop("store", UNSET)

        store_transaction_id = d.pop("store_transaction_id", UNSET)

        subscriber_subscriber_non_subscriptions_additional_property_item = cls(
            display_name=display_name,
            id=id,
            is_sandbox=is_sandbox,
            price=price,
            purchase_date=purchase_date,
            store=store,
            store_transaction_id=store_transaction_id,
        )

        subscriber_subscriber_non_subscriptions_additional_property_item.additional_properties = d
        return subscriber_subscriber_non_subscriptions_additional_property_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
