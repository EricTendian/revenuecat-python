from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.customer_attribute_reserved_name import CustomerAttributeReservedName

T = TypeVar("T", bound="CreateCustomerBodyAttributesItem")


@_attrs_define
class CreateCustomerBodyAttributesItem:
    """
    Attributes:
        name (CustomerAttributeReservedName | str): The name of the attribute Example: $email.
        value (str): The value of the attribute Example: cat@revenuecat.com.
    """

    name: CustomerAttributeReservedName | str
    value: str

    def to_dict(self) -> dict[str, Any]:
        name: str
        if isinstance(self.name, CustomerAttributeReservedName):
            name = self.name.value
        else:
            name = self.name

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> CustomerAttributeReservedName | str:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                name_type_0 = CustomerAttributeReservedName(data)

                return name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomerAttributeReservedName | str, data)

        name = _parse_name(d.pop("name"))

        value = d.pop("value")

        create_customer_body_attributes_item = cls(
            name=name,
            value=value,
        )

        return create_customer_body_attributes_item
