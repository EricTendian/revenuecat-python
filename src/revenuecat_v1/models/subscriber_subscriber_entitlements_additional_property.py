from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriberSubscriberEntitlementsAdditionalProperty")


@_attrs_define
class SubscriberSubscriberEntitlementsAdditionalProperty:
    """One entitlement granted to this Customer. If the customer was granted this entitlement through multiple purchases,
    then the information about the purchase with the furthest-out expiration date is included.

        Attributes:
            expires_date (None | str | Unset): Date when the entitlement expires / expired (in ISO 8601 format, may be in
                the past). `null` if it is a lifetime entitlement. Example: 2024-12-12T14:04:03Z.
            grace_period_expires_date (None | str | Unset): Date when any potential grace period of the entitlement expires
                / expired (in ISO 8601 format, may be in the past). `null` if the Customer has never been in a grace period.
                Example: 2024-12-12T14:04:03Z.
            product_identifier (str | Unset): The identifier of the product that is responsible for this entitlement being
                granted.<br><br>Please note: in some cases, if there are problems with validating the purchase with the store,
                the correct product identifier might temporarily be unavailable.
                 Example: onetime.
            purchase_date (str | Unset): Time of the last purchase or renewal of the product that grants this entitlement
                (in ISO 8601 format). Example: 2019-04-05T21:52:45Z.
    """

    expires_date: None | str | Unset = UNSET
    grace_period_expires_date: None | str | Unset = UNSET
    product_identifier: str | Unset = UNSET
    purchase_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_date: None | str | Unset
        if isinstance(self.expires_date, Unset):
            expires_date = UNSET
        else:
            expires_date = self.expires_date

        grace_period_expires_date: None | str | Unset
        if isinstance(self.grace_period_expires_date, Unset):
            grace_period_expires_date = UNSET
        else:
            grace_period_expires_date = self.grace_period_expires_date

        product_identifier = self.product_identifier

        purchase_date = self.purchase_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_date is not UNSET:
            field_dict["expires_date"] = expires_date
        if grace_period_expires_date is not UNSET:
            field_dict["grace_period_expires_date"] = grace_period_expires_date
        if product_identifier is not UNSET:
            field_dict["product_identifier"] = product_identifier
        if purchase_date is not UNSET:
            field_dict["purchase_date"] = purchase_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expires_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_date = _parse_expires_date(d.pop("expires_date", UNSET))

        def _parse_grace_period_expires_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grace_period_expires_date = _parse_grace_period_expires_date(d.pop("grace_period_expires_date", UNSET))

        product_identifier = d.pop("product_identifier", UNSET)

        purchase_date = d.pop("purchase_date", UNSET)

        subscriber_subscriber_entitlements_additional_property = cls(
            expires_date=expires_date,
            grace_period_expires_date=grace_period_expires_date,
            product_identifier=product_identifier,
            purchase_date=purchase_date,
        )

        subscriber_subscriber_entitlements_additional_property.additional_properties = d
        return subscriber_subscriber_entitlements_additional_property

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
