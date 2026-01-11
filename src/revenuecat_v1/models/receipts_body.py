from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.receipts_body_attributes import ReceiptsBodyAttributes


T = TypeVar("T", bound="ReceiptsBody")


@_attrs_define
class ReceiptsBody:
    """
    Attributes:
        app_user_id (str): App User ID of the Customer the receipt is associated with.
        fetch_token (str): For iOS, the base64 encoded receipt file (or JWSTransaction for StoreKit2), for Android the
            receipt token, for Amazon the receipt, for Stripe the subscription ID or the Stripe Checkout Session ID, for
            Roku the transaction ID, and for Paddle the subscription ID or transaction ID.
        product_id (str | Unset): The Apple, Google, Amazon, Roku, or Paddle product identifier or SKU. Required for
            Google. Example: com.my.product.iap.
        price (float | Unset): The price of the product. **Required if you provide a currency.** Example: 1.99.
        currency (str | Unset): The currency of the product. The currency must be in [ISO 4217
            format](https://en.wikipedia.org/wiki/ISO_4217). **Required if you provide a price.** Default: 'USD'. Example:
            USD.
        payment_mode (str | Unset): Optionally used by the iOS SDK to communicate intro pricing periods. Either
            `pay_as_you_go = 0`, `pay_up_front = 1`, or `free_trial = 2`. Defaults to `2` (free trial) if an introductory
            period is detected in the receipt but this value is not provided.
        introductory_price (float | Unset): Introductory price paid
        is_restore (bool | Unset): If true, the fetch token will trigger your configured [restore
            behavior](https://www.revenuecat.com/docs/restoring-purchases#restore-behavior) for any other users sharing the
            same fetch token. Default: False.
        presented_offering_identifier (str | Unset): Optional. The offering that was presented to the Customer at the
            time of purchase.  This will be attached to any new transactions in this fetch token and will be available in
            ETL exports and webhooks. This is mostly useful if you're sending fetch tokens from your backend.
        attributes (ReceiptsBodyAttributes | Unset): Any [Attributes](/docs/customers/customer-attributes) to set on the
            Customer as a dictionary keyed by the Attribute name.
    """

    app_user_id: str
    fetch_token: str
    product_id: str | Unset = UNSET
    price: float | Unset = UNSET
    currency: str | Unset = "USD"
    payment_mode: str | Unset = UNSET
    introductory_price: float | Unset = UNSET
    is_restore: bool | Unset = False
    presented_offering_identifier: str | Unset = UNSET
    attributes: ReceiptsBodyAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_user_id = self.app_user_id

        fetch_token = self.fetch_token

        product_id = self.product_id

        price = self.price

        currency = self.currency

        payment_mode = self.payment_mode

        introductory_price = self.introductory_price

        is_restore = self.is_restore

        presented_offering_identifier = self.presented_offering_identifier

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_user_id": app_user_id,
                "fetch_token": fetch_token,
            }
        )
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if price is not UNSET:
            field_dict["price"] = price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if payment_mode is not UNSET:
            field_dict["payment_mode"] = payment_mode
        if introductory_price is not UNSET:
            field_dict["introductory_price"] = introductory_price
        if is_restore is not UNSET:
            field_dict["is_restore"] = is_restore
        if presented_offering_identifier is not UNSET:
            field_dict["presented_offering_identifier"] = presented_offering_identifier
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.receipts_body_attributes import ReceiptsBodyAttributes

        d = dict(src_dict)
        app_user_id = d.pop("app_user_id")

        fetch_token = d.pop("fetch_token")

        product_id = d.pop("product_id", UNSET)

        price = d.pop("price", UNSET)

        currency = d.pop("currency", UNSET)

        payment_mode = d.pop("payment_mode", UNSET)

        introductory_price = d.pop("introductory_price", UNSET)

        is_restore = d.pop("is_restore", UNSET)

        presented_offering_identifier = d.pop("presented_offering_identifier", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: ReceiptsBodyAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ReceiptsBodyAttributes.from_dict(_attributes)

        receipts_body = cls(
            app_user_id=app_user_id,
            fetch_token=fetch_token,
            product_id=product_id,
            price=price,
            currency=currency,
            payment_mode=payment_mode,
            introductory_price=introductory_price,
            is_restore=is_restore,
            presented_offering_identifier=presented_offering_identifier,
            attributes=attributes,
        )

        receipts_body.additional_properties = d
        return receipts_body

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
