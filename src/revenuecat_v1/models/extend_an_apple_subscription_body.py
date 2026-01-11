from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExtendAnAppleSubscriptionBody")


@_attrs_define
class ExtendAnAppleSubscriptionBody:
    """
    Attributes:
        extend_by_days (int): The number of days to extend the subscription renewal date. Must be between 1 and 90.
            Example: 30.
        extend_reason_code (int): The reason code for the subscription extension. See Apple's
            [extendReasonCode](https://developer.apple.com/documentation/appstoreserverapi/extendreasoncode) documentation.
            - `0`: Undeclared - The renewal-date extension reason is undeclared.
            - `1`: Customer Satisfaction - The renewal-date extension is for customer satisfaction.
            - `2`: Other - The renewal-date extension is for a reason other than the ones listed.
            - `3`: Service Issue or Outage - The renewal-date extension is due to a service issue or outage.
             Example: 1.
    """

    extend_by_days: int
    extend_reason_code: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extend_by_days = self.extend_by_days

        extend_reason_code = self.extend_reason_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extend_by_days": extend_by_days,
                "extend_reason_code": extend_reason_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extend_by_days = d.pop("extend_by_days")

        extend_reason_code = d.pop("extend_reason_code")

        extend_an_apple_subscription_body = cls(
            extend_by_days=extend_by_days,
            extend_reason_code=extend_reason_code,
        )

        extend_an_apple_subscription_body.additional_properties = d
        return extend_an_apple_subscription_body

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
