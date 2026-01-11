from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscriber_subscriber_subscriptions_additional_property_ownership_type import (
    SubscriberSubscriberSubscriptionsAdditionalPropertyOwnershipType,
)
from ..models.subscriber_subscriber_subscriptions_additional_property_period_type import (
    SubscriberSubscriberSubscriptionsAdditionalPropertyPeriodType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_subscriber_subscriptions_additional_property_price import (
        SubscriberSubscriberSubscriptionsAdditionalPropertyPrice,
    )


T = TypeVar("T", bound="SubscriberSubscriberSubscriptionsAdditionalProperty")


@_attrs_define
class SubscriberSubscriberSubscriptionsAdditionalProperty:
    """One subscription product purchased by the Customer.

    Attributes:
        auto_resume_date (str | Unset): Date when the subscription will automatically resume after being paused (in ISO
            8601 format). Google Play only.
        billing_issues_detected_at (str | Unset): Date when RevenueCat detected any billing issues with this
            subscription (in ISO 8601 format). If and when the billing issue gets resolved, this field is set to `null`.
            Note the subscription may still be active, check the `expires_date` attribute.
        expires_date (str | Unset): Date when the subscription expires/expired (in ISO 8601 format). Example:
            2019-08-14T21:07:40Z.
        display_name (str | Unset): The display name of the product as configured in the RevenueCat dashboard. Example:
            Monthly Subscription.
        grace_period_expires_date (str | Unset): Date when any grace period for this subscription expires/expired (in
            ISO 8601 format). `null` if the Customer has never been in a grace period. Example: 2019-08-14T21:07:40Z.
        is_sandbox (bool | Unset): Whether or not the purchase was made in sandbox mode.
        original_purchase_date (str | Unset): Date when this subscription first started (in ISO 8601 format). This
            property does not update with renewals. On iOS, this property also does not update for product changes within a
            subscription group or resubscriptions by lapsed subscribers. Example: 2019-02-21T00:42:05Z.
        ownership_type (SubscriberSubscriberSubscriptionsAdditionalPropertyOwnershipType | Unset): How the Customer
            received access to this subscription:
            - `PURCHASED`: The Customer purchased the product.
            - `FAMILY_SHARED`: The Customer has access to the product via their family.
        period_type (SubscriberSubscriberSubscriptionsAdditionalPropertyPeriodType | Unset): Type of the current
            subscription period_type:
            - `normal`: The product is in a normal period (default)
            - `trial`: The product is in a free trial period
            - `intro`: The product is in an introductory pricing period
             Example: NORMAL.
        price (SubscriberSubscriberSubscriptionsAdditionalPropertyPrice | Unset): The price of the transaction in the
            currency the product was purchased in. Can be 0 for free trials.
        purchase_date (str | Unset): Date when the last subscription period started (in ISO 8601 format). Example:
            2019-07-14T20:07:40Z.
        refunded_at (str | Unset): Date when RevenueCat detected a refund of this subscription.
        store (str | Unset): Identifier of the store of the purchase:
            - `app_store`: The product was purchased through Apple App Store.
            - `mac_app_store`: The product was purchased through the Mac App Store.
            - `play_store`: The product was purchased through the Google Play Store.
            - `amazon`: The product was purchased through the Amazon Appstore.
            - `stripe`: The product was purchased through Stripe.
            - `promotional`: The product was [granted via RevenueCat](#tag/entitlements/operation/grant-a-promotional-
            entitlement).
            - `roku`: The product was purchased through Roku.
            - `paddle`: The product was purchased through Paddle.
             Example: app_store.
        store_transaction_id (str | Unset): Identifier of the purchase in the store's API.
             Example: GPA.6801-7988-0152-76034..5.
        unsubscribe_detected_at (str | Unset): Date when RevenueCat detected that auto-renewal was turned off for this
            subsription (in ISO 8601 format). Note the subscription may still be active, check the `expires_date` attribute.
            Example: 2019-07-17T22:48:38Z.
    """

    auto_resume_date: str | Unset = UNSET
    billing_issues_detected_at: str | Unset = UNSET
    expires_date: str | Unset = UNSET
    display_name: str | Unset = UNSET
    grace_period_expires_date: str | Unset = UNSET
    is_sandbox: bool | Unset = UNSET
    original_purchase_date: str | Unset = UNSET
    ownership_type: SubscriberSubscriberSubscriptionsAdditionalPropertyOwnershipType | Unset = UNSET
    period_type: SubscriberSubscriberSubscriptionsAdditionalPropertyPeriodType | Unset = UNSET
    price: SubscriberSubscriberSubscriptionsAdditionalPropertyPrice | Unset = UNSET
    purchase_date: str | Unset = UNSET
    refunded_at: str | Unset = UNSET
    store: str | Unset = UNSET
    store_transaction_id: str | Unset = UNSET
    unsubscribe_detected_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_resume_date = self.auto_resume_date

        billing_issues_detected_at = self.billing_issues_detected_at

        expires_date = self.expires_date

        display_name = self.display_name

        grace_period_expires_date = self.grace_period_expires_date

        is_sandbox = self.is_sandbox

        original_purchase_date = self.original_purchase_date

        ownership_type: str | Unset = UNSET
        if not isinstance(self.ownership_type, Unset):
            ownership_type = self.ownership_type.value

        period_type: str | Unset = UNSET
        if not isinstance(self.period_type, Unset):
            period_type = self.period_type.value

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        purchase_date = self.purchase_date

        refunded_at = self.refunded_at

        store = self.store

        store_transaction_id = self.store_transaction_id

        unsubscribe_detected_at = self.unsubscribe_detected_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_resume_date is not UNSET:
            field_dict["auto_resume_date"] = auto_resume_date
        if billing_issues_detected_at is not UNSET:
            field_dict["billing_issues_detected_at"] = billing_issues_detected_at
        if expires_date is not UNSET:
            field_dict["expires_date"] = expires_date
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if grace_period_expires_date is not UNSET:
            field_dict["grace_period_expires_date"] = grace_period_expires_date
        if is_sandbox is not UNSET:
            field_dict["is_sandbox"] = is_sandbox
        if original_purchase_date is not UNSET:
            field_dict["original_purchase_date"] = original_purchase_date
        if ownership_type is not UNSET:
            field_dict["ownership_type"] = ownership_type
        if period_type is not UNSET:
            field_dict["period_type"] = period_type
        if price is not UNSET:
            field_dict["price"] = price
        if purchase_date is not UNSET:
            field_dict["purchase_date"] = purchase_date
        if refunded_at is not UNSET:
            field_dict["refunded_at"] = refunded_at
        if store is not UNSET:
            field_dict["store"] = store
        if store_transaction_id is not UNSET:
            field_dict["store_transaction_id"] = store_transaction_id
        if unsubscribe_detected_at is not UNSET:
            field_dict["unsubscribe_detected_at"] = unsubscribe_detected_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscriber_subscriber_subscriptions_additional_property_price import (
            SubscriberSubscriberSubscriptionsAdditionalPropertyPrice,
        )

        d = dict(src_dict)
        auto_resume_date = d.pop("auto_resume_date", UNSET)

        billing_issues_detected_at = d.pop("billing_issues_detected_at", UNSET)

        expires_date = d.pop("expires_date", UNSET)

        display_name = d.pop("display_name", UNSET)

        grace_period_expires_date = d.pop("grace_period_expires_date", UNSET)

        is_sandbox = d.pop("is_sandbox", UNSET)

        original_purchase_date = d.pop("original_purchase_date", UNSET)

        _ownership_type = d.pop("ownership_type", UNSET)
        ownership_type: SubscriberSubscriberSubscriptionsAdditionalPropertyOwnershipType | Unset
        if isinstance(_ownership_type, Unset):
            ownership_type = UNSET
        else:
            ownership_type = SubscriberSubscriberSubscriptionsAdditionalPropertyOwnershipType(_ownership_type)

        _period_type = d.pop("period_type", UNSET)
        period_type: SubscriberSubscriberSubscriptionsAdditionalPropertyPeriodType | Unset
        if isinstance(_period_type, Unset):
            period_type = UNSET
        else:
            period_type = SubscriberSubscriberSubscriptionsAdditionalPropertyPeriodType(_period_type)

        _price = d.pop("price", UNSET)
        price: SubscriberSubscriberSubscriptionsAdditionalPropertyPrice | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = SubscriberSubscriberSubscriptionsAdditionalPropertyPrice.from_dict(_price)

        purchase_date = d.pop("purchase_date", UNSET)

        refunded_at = d.pop("refunded_at", UNSET)

        store = d.pop("store", UNSET)

        store_transaction_id = d.pop("store_transaction_id", UNSET)

        unsubscribe_detected_at = d.pop("unsubscribe_detected_at", UNSET)

        subscriber_subscriber_subscriptions_additional_property = cls(
            auto_resume_date=auto_resume_date,
            billing_issues_detected_at=billing_issues_detected_at,
            expires_date=expires_date,
            display_name=display_name,
            grace_period_expires_date=grace_period_expires_date,
            is_sandbox=is_sandbox,
            original_purchase_date=original_purchase_date,
            ownership_type=ownership_type,
            period_type=period_type,
            price=price,
            purchase_date=purchase_date,
            refunded_at=refunded_at,
            store=store,
            store_transaction_id=store_transaction_id,
            unsubscribe_detected_at=unsubscribe_detected_at,
        )

        subscriber_subscriber_subscriptions_additional_property.additional_properties = d
        return subscriber_subscriber_subscriptions_additional_property

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
