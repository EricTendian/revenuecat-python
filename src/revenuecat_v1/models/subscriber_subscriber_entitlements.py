from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.subscriber_subscriber_entitlements_additional_property import (
        SubscriberSubscriberEntitlementsAdditionalProperty,
    )


T = TypeVar("T", bound="SubscriberSubscriberEntitlements")


@_attrs_define
class SubscriberSubscriberEntitlements:
    """Dictionary of the entitlements of this Customer (including any expired entitlements)."""

    additional_properties: dict[str, SubscriberSubscriberEntitlementsAdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscriber_subscriber_entitlements_additional_property import (
            SubscriberSubscriberEntitlementsAdditionalProperty,
        )

        d = dict(src_dict)
        subscriber_subscriber_entitlements = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = SubscriberSubscriberEntitlementsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        subscriber_subscriber_entitlements.additional_properties = additional_properties
        return subscriber_subscriber_entitlements

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> SubscriberSubscriberEntitlementsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: SubscriberSubscriberEntitlementsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
