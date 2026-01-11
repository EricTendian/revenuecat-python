from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_subscriber import SubscriberSubscriber


T = TypeVar("T", bound="Subscriber")


@_attrs_define
class Subscriber:
    """Snapshot of information about a Customer.

    Example:
        {'value': {'request_date': '2019-07-26T17:40:10Z', 'request_date_ms': 1564162810884, 'subscriber':
            {'entitlements': {'pro_cat': {'expires_date': None, 'grace_period_expires_date': None, 'product_identifier':
            'onetime', 'purchase_date': '2019-04-05T21:52:45Z'}}, 'first_seen': '2019-02-21T00:08:41Z', 'management_url':
            'https://apps.apple.com/account/subscriptions', 'non_subscriptions': {'onetime': [{'id': 'cadba0c81b',
            'is_sandbox': True, 'purchase_date': '2019-04-05T21:52:45Z', 'store': 'app_store'}]}, 'original_app_user_id':
            'XXX-XXXXX-XXXXX-XX', 'original_application_version': '1.0', 'original_purchase_date': '2019-01-30T23:54:10Z',
            'other_purchases': {}, 'subscriptions': {'annual': {'auto_resume_date': None, 'billing_issues_detected_at':
            None, 'expires_date': '2019-08-14T21:07:40Z', 'grace_period_expires_date': None, 'is_sandbox': True,
            'original_purchase_date': '2019-02-21T00:42:05Z', 'ownership_type': 'PURCHASED', 'period_type': 'normal',
            'purchase_date': '2019-07-14T20:07:40Z', 'refunded_at': None, 'store': 'play_store', 'store_transaction_id':
            'GPA.6801-7988-0152-76034..5', 'unsubscribe_detected_at': '2019-07-17T22:48:38Z'}, 'onemonth':
            {'auto_resume_date': None, 'billing_issues_detected_at': None, 'expires_date': '2019-06-17T22:47:55Z',
            'grace_period_expires_date': None, 'is_sandbox': True, 'original_purchase_date': '2019-02-21T00:42:05Z',
            'ownership_type': 'PURCHASED', 'period_type': 'normal', 'purchase_date': '2019-06-17T22:42:55Z', 'refunded_at':
            None, 'store': 'app_store', 'store_transaction_id': 1000000652379790, 'unsubscribe_detected_at':
            '2019-06-17T22:48:38Z'}, 'rc_promo_pro_cat_monthly': {'auto_resume_date': None, 'billing_issues_detected_at':
            None, 'expires_date': '2019-08-26T01:02:16Z', 'grace_period_expires_date': None, 'is_sandbox': False,
            'original_purchase_date': '2019-07-26T01:02:16Z', 'ownership_type': 'FAMILY_SHARED', 'period_type': 'normal',
            'purchase_date': '2019-07-26T01:02:16Z', 'refunded_at': None, 'store': 'promotional', 'store_transaction_id':
            'a42db3af39530cb82b17eaf9c6576393', 'unsubscribe_detected_at': None}}}}}

    Attributes:
        request_date (str | Unset): Date of the request in ISO 8601 format. Example: 2019-07-26T17:40:10Z.
        request_date_ms (int | Unset): Date of the request in milliseconds since Epoch. Example: 1564162810884.
        subscriber (SubscriberSubscriber | Unset): Information about the Customer.
    """

    request_date: str | Unset = UNSET
    request_date_ms: int | Unset = UNSET
    subscriber: SubscriberSubscriber | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_date = self.request_date

        request_date_ms = self.request_date_ms

        subscriber: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscriber, Unset):
            subscriber = self.subscriber.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_date is not UNSET:
            field_dict["request_date"] = request_date
        if request_date_ms is not UNSET:
            field_dict["request_date_ms"] = request_date_ms
        if subscriber is not UNSET:
            field_dict["subscriber"] = subscriber

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscriber_subscriber import SubscriberSubscriber

        d = dict(src_dict)
        request_date = d.pop("request_date", UNSET)

        request_date_ms = d.pop("request_date_ms", UNSET)

        _subscriber = d.pop("subscriber", UNSET)
        subscriber: SubscriberSubscriber | Unset
        if isinstance(_subscriber, Unset):
            subscriber = UNSET
        else:
            subscriber = SubscriberSubscriber.from_dict(_subscriber)

        subscriber = cls(
            request_date=request_date,
            request_date_ms=request_date_ms,
            subscriber=subscriber,
        )

        subscriber.additional_properties = d
        return subscriber

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
