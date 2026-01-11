from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.subscriber_subscriber_subscriber_attributes_additional_property import (
        SubscriberSubscriberSubscriberAttributesAdditionalProperty,
    )


T = TypeVar("T", bound="SubscriberSubscriberSubscriberAttributes")


@_attrs_define
class SubscriberSubscriberSubscriberAttributes:
    """A dictionary of any Attributes set on this Customer. **Only included in responses to requests made with a secret API
    key**.

    """

    additional_properties: dict[str, SubscriberSubscriberSubscriberAttributesAdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscriber_subscriber_subscriber_attributes_additional_property import (
            SubscriberSubscriberSubscriberAttributesAdditionalProperty,
        )

        d = dict(src_dict)
        subscriber_subscriber_subscriber_attributes = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = SubscriberSubscriberSubscriberAttributesAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        subscriber_subscriber_subscriber_attributes.additional_properties = additional_properties
        return subscriber_subscriber_subscriber_attributes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> SubscriberSubscriberSubscriberAttributesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: SubscriberSubscriberSubscriberAttributesAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
