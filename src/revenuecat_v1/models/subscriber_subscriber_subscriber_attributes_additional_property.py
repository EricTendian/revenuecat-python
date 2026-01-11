from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriberSubscriberSubscriberAttributesAdditionalProperty")


@_attrs_define
class SubscriberSubscriberSubscriberAttributesAdditionalProperty:
    """An Attribute set on the Customer object.

    Example:
        {'favorite_color': {'value': 'red', 'updated_at_ms': 1564162810884}}

    Attributes:
        value (str | Unset): The value of the attribute. Example: red.
        updated_at_ms (int | Unset): The time that the Attribute was last updated, in milliseconds since Epoch. Example:
            1564162810884.
    """

    value: str | Unset = UNSET
    updated_at_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        updated_at_ms = self.updated_at_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if updated_at_ms is not UNSET:
            field_dict["updated_at_ms"] = updated_at_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        updated_at_ms = d.pop("updated_at_ms", UNSET)

        subscriber_subscriber_subscriber_attributes_additional_property = cls(
            value=value,
            updated_at_ms=updated_at_ms,
        )

        subscriber_subscriber_subscriber_attributes_additional_property.additional_properties = d
        return subscriber_subscriber_subscriber_attributes_additional_property

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
