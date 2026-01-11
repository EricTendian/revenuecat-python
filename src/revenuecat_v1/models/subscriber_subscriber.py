from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_subscriber_entitlements import SubscriberSubscriberEntitlements
    from ..models.subscriber_subscriber_non_subscriptions import SubscriberSubscriberNonSubscriptions
    from ..models.subscriber_subscriber_other_purchases import SubscriberSubscriberOtherPurchases
    from ..models.subscriber_subscriber_subscriber_attributes import SubscriberSubscriberSubscriberAttributes
    from ..models.subscriber_subscriber_subscriptions import SubscriberSubscriberSubscriptions


T = TypeVar("T", bound="SubscriberSubscriber")


@_attrs_define
class SubscriberSubscriber:
    """Information about the Customer.

    Attributes:
        entitlements (SubscriberSubscriberEntitlements | Unset): Dictionary of the entitlements of this Customer
            (including any expired entitlements).
        first_seen (str | Unset): The ISO 8601 datetime string corresponding to when the Customer was first seen by
            RevenueCat. Example: 2019-02-21T00:08:41Z.
        last_seen (str | Unset): The ISO 8601 datetime string corresponding to when the Customer was last seen by
            RevenueCat. Example: 2019-02-21T00:08:41Z.
        management_url (str | Unset): URL to manage the active subscription of the Customer. If the Customer has an
            active iOS subscription, this will point to the App Store, if the Customer has an active Play Store subscription
            it will point there.

            If there are no active subscriptions it will be null.

            If the Customer has multiple active subscriptions for different platforms, this will take the value of the OS in
            the `X-Platform` header into consideration:
            - If the request was made on an OS for which there are active subscriptions, this will return the URL for the
            store that matches the header.
            - If the request was made on a different OS or the OS was not included in the X-Platform header, this will
            return the URL for the store of the subscription with the farthest future expiration date.
             Example: https://apps.apple.com/account/subscriptions.
        non_subscriptions (SubscriberSubscriberNonSubscriptions | Unset): Non-subscription purchases of the Customer,
            keyed by the product identifier.
        original_app_user_id (str | Unset): The App User ID under which this Customer was first known to RevenueCat.
            Example: XXX-XXXXX-XXXXX-XX.
        original_application_version (str | Unset): *Only available on iOS*. This will be `null` until an iOS receipt is
            sent for the Customer. After a receipt has been sent, it will indicate the first App Store version of your app
            that the Customer installed. Example: 1.0.
        original_purchase_date (str | Unset): **Only available on iOS**. The date that the app was first
            purchased/downloaded by the Customer. Will be `null` if no receipt is recorded for the Customer. Useful for
            [Migrating Subscriptions](/docs/migrating-to-revenuecat/migrating-existing-subscriptions). Example:
            2019-01-30T23:54:10Z.
        other_purchases (SubscriberSubscriberOtherPurchases | Unset):
        subscriber_attributes (SubscriberSubscriberSubscriberAttributes | Unset): A dictionary of any Attributes set on
            this Customer. **Only included in responses to requests made with a secret API key**.
        subscriptions (SubscriberSubscriberSubscriptions | Unset): Subscription purchases of the Customer, keyed by the
            product identifier.
    """

    entitlements: SubscriberSubscriberEntitlements | Unset = UNSET
    first_seen: str | Unset = UNSET
    last_seen: str | Unset = UNSET
    management_url: str | Unset = UNSET
    non_subscriptions: SubscriberSubscriberNonSubscriptions | Unset = UNSET
    original_app_user_id: str | Unset = UNSET
    original_application_version: str | Unset = UNSET
    original_purchase_date: str | Unset = UNSET
    other_purchases: SubscriberSubscriberOtherPurchases | Unset = UNSET
    subscriber_attributes: SubscriberSubscriberSubscriberAttributes | Unset = UNSET
    subscriptions: SubscriberSubscriberSubscriptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entitlements: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entitlements, Unset):
            entitlements = self.entitlements.to_dict()

        first_seen = self.first_seen

        last_seen = self.last_seen

        management_url = self.management_url

        non_subscriptions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.non_subscriptions, Unset):
            non_subscriptions = self.non_subscriptions.to_dict()

        original_app_user_id = self.original_app_user_id

        original_application_version = self.original_application_version

        original_purchase_date = self.original_purchase_date

        other_purchases: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_purchases, Unset):
            other_purchases = self.other_purchases.to_dict()

        subscriber_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscriber_attributes, Unset):
            subscriber_attributes = self.subscriber_attributes.to_dict()

        subscriptions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entitlements is not UNSET:
            field_dict["entitlements"] = entitlements
        if first_seen is not UNSET:
            field_dict["first_seen"] = first_seen
        if last_seen is not UNSET:
            field_dict["last_seen"] = last_seen
        if management_url is not UNSET:
            field_dict["management_url"] = management_url
        if non_subscriptions is not UNSET:
            field_dict["non_subscriptions"] = non_subscriptions
        if original_app_user_id is not UNSET:
            field_dict["original_app_user_id"] = original_app_user_id
        if original_application_version is not UNSET:
            field_dict["original_application_version"] = original_application_version
        if original_purchase_date is not UNSET:
            field_dict["original_purchase_date"] = original_purchase_date
        if other_purchases is not UNSET:
            field_dict["other_purchases"] = other_purchases
        if subscriber_attributes is not UNSET:
            field_dict["subscriber_attributes"] = subscriber_attributes
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscriber_subscriber_entitlements import SubscriberSubscriberEntitlements
        from ..models.subscriber_subscriber_non_subscriptions import SubscriberSubscriberNonSubscriptions
        from ..models.subscriber_subscriber_other_purchases import SubscriberSubscriberOtherPurchases
        from ..models.subscriber_subscriber_subscriber_attributes import SubscriberSubscriberSubscriberAttributes
        from ..models.subscriber_subscriber_subscriptions import SubscriberSubscriberSubscriptions

        d = dict(src_dict)
        _entitlements = d.pop("entitlements", UNSET)
        entitlements: SubscriberSubscriberEntitlements | Unset
        if isinstance(_entitlements, Unset):
            entitlements = UNSET
        else:
            entitlements = SubscriberSubscriberEntitlements.from_dict(_entitlements)

        first_seen = d.pop("first_seen", UNSET)

        last_seen = d.pop("last_seen", UNSET)

        management_url = d.pop("management_url", UNSET)

        _non_subscriptions = d.pop("non_subscriptions", UNSET)
        non_subscriptions: SubscriberSubscriberNonSubscriptions | Unset
        if isinstance(_non_subscriptions, Unset):
            non_subscriptions = UNSET
        else:
            non_subscriptions = SubscriberSubscriberNonSubscriptions.from_dict(_non_subscriptions)

        original_app_user_id = d.pop("original_app_user_id", UNSET)

        original_application_version = d.pop("original_application_version", UNSET)

        original_purchase_date = d.pop("original_purchase_date", UNSET)

        _other_purchases = d.pop("other_purchases", UNSET)
        other_purchases: SubscriberSubscriberOtherPurchases | Unset
        if isinstance(_other_purchases, Unset):
            other_purchases = UNSET
        else:
            other_purchases = SubscriberSubscriberOtherPurchases.from_dict(_other_purchases)

        _subscriber_attributes = d.pop("subscriber_attributes", UNSET)
        subscriber_attributes: SubscriberSubscriberSubscriberAttributes | Unset
        if isinstance(_subscriber_attributes, Unset):
            subscriber_attributes = UNSET
        else:
            subscriber_attributes = SubscriberSubscriberSubscriberAttributes.from_dict(_subscriber_attributes)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: SubscriberSubscriberSubscriptions | Unset
        if isinstance(_subscriptions, Unset):
            subscriptions = UNSET
        else:
            subscriptions = SubscriberSubscriberSubscriptions.from_dict(_subscriptions)

        subscriber_subscriber = cls(
            entitlements=entitlements,
            first_seen=first_seen,
            last_seen=last_seen,
            management_url=management_url,
            non_subscriptions=non_subscriptions,
            original_app_user_id=original_app_user_id,
            original_application_version=original_application_version,
            original_purchase_date=original_purchase_date,
            other_purchases=other_purchases,
            subscriber_attributes=subscriber_attributes,
            subscriptions=subscriptions,
        )

        subscriber_subscriber.additional_properties = d
        return subscriber_subscriber

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
