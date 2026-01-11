from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.set_customer_attributes_body_attributes_item import SetCustomerAttributesBodyAttributesItem


T = TypeVar("T", bound="SetCustomerAttributesBody")


@_attrs_define
class SetCustomerAttributesBody:
    """
    Example:
        {'attributes': [{'name': '$email', 'value': 'support@revenuecat.com'}, {'name': '$displayName', 'value': 'John
            Appleseed'}, {'name': 'my_custom_attr', 'value': 'custom value'}]}

    Attributes:
        attributes (list[SetCustomerAttributesBodyAttributesItem]):
    """

    attributes: list[SetCustomerAttributesBodyAttributesItem]

    def to_dict(self) -> dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.set_customer_attributes_body_attributes_item import SetCustomerAttributesBodyAttributesItem

        d = dict(src_dict)
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = SetCustomerAttributesBodyAttributesItem.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        set_customer_attributes_body = cls(
            attributes=attributes,
        )

        return set_customer_attributes_body
