from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StripeAppStripe")


@_attrs_define
class StripeAppStripe:
    """Stripe type details

    Attributes:
        stripe_account_id (None | str | Unset): Stripe account connected to your RevenueCat account.
    """

    stripe_account_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stripe_account_id: None | str | Unset
        if isinstance(self.stripe_account_id, Unset):
            stripe_account_id = UNSET
        else:
            stripe_account_id = self.stripe_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stripe_account_id is not UNSET:
            field_dict["stripe_account_id"] = stripe_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_stripe_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_account_id = _parse_stripe_account_id(d.pop("stripe_account_id", UNSET))

        stripe_app_stripe = cls(
            stripe_account_id=stripe_account_id,
        )

        stripe_app_stripe.additional_properties = d
        return stripe_app_stripe

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
