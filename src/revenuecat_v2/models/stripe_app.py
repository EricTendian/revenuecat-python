from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stripe_app_stripe import StripeAppStripe


T = TypeVar("T", bound="StripeApp")


@_attrs_define
class StripeApp:
    """
    Attributes:
        stripe (StripeAppStripe | Unset): Stripe type details
    """

    stripe: StripeAppStripe | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stripe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stripe, Unset):
            stripe = self.stripe.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stripe is not UNSET:
            field_dict["stripe"] = stripe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stripe_app_stripe import StripeAppStripe

        d = dict(src_dict)
        _stripe = d.pop("stripe", UNSET)
        stripe: StripeAppStripe | Unset
        if isinstance(_stripe, Unset):
            stripe = UNSET
        else:
            stripe = StripeAppStripe.from_dict(_stripe)

        stripe_app = cls(
            stripe=stripe,
        )

        stripe_app.additional_properties = d
        return stripe_app

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
