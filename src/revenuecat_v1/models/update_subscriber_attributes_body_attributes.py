from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_subscriber_attributes_body_attributes_key_name import (
        UpdateSubscriberAttributesBodyAttributesKeyName,
    )


T = TypeVar("T", bound="UpdateSubscriberAttributesBodyAttributes")


@_attrs_define
class UpdateSubscriberAttributesBodyAttributes:
    """
    Attributes:
        key_name (UpdateSubscriberAttributesBodyAttributesKeyName): Mapping of keys to attribute values.
    """

    key_name: UpdateSubscriberAttributesBodyAttributesKeyName
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_name = self.key_name.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_name": key_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_subscriber_attributes_body_attributes_key_name import (
            UpdateSubscriberAttributesBodyAttributesKeyName,
        )

        d = dict(src_dict)
        key_name = UpdateSubscriberAttributesBodyAttributesKeyName.from_dict(d.pop("key_name"))

        update_subscriber_attributes_body_attributes = cls(
            key_name=key_name,
        )

        update_subscriber_attributes_body_attributes.additional_properties = d
        return update_subscriber_attributes_body_attributes

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
