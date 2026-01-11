from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeferAGoogleSubscriptionBody")


@_attrs_define
class DeferAGoogleSubscriptionBody:
    """
    Attributes:
        expiry_time_ms (int | Unset): The desired next expiry time to assign to the subscription, in milliseconds since
            the Epoch. The given time must be later/greater than the current expiry time for the subscription. Either
            `expiry_time_ms` or `extend_by_days` must be provided. Example: 1708417962662.
        extend_by_days (int | Unset): The number of days to extend the subscription renewal date. Must be between 1 and
            365. Either `expiry_time_ms` or `extend_by_days` must be provided. Example: 30.
    """

    expiry_time_ms: int | Unset = UNSET
    extend_by_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiry_time_ms = self.expiry_time_ms

        extend_by_days = self.extend_by_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiry_time_ms is not UNSET:
            field_dict["expiry_time_ms"] = expiry_time_ms
        if extend_by_days is not UNSET:
            field_dict["extend_by_days"] = extend_by_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expiry_time_ms = d.pop("expiry_time_ms", UNSET)

        extend_by_days = d.pop("extend_by_days", UNSET)

        defer_a_google_subscription_body = cls(
            expiry_time_ms=expiry_time_ms,
            extend_by_days=extend_by_days,
        )

        defer_a_google_subscription_body.additional_properties = d
        return defer_a_google_subscription_body

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
