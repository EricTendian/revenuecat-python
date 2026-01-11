from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.customer_attribute_reserved_name import CustomerAttributeReservedName

T = TypeVar("T", bound="SetCustomerAttributesBodyAttributesItem")


@_attrs_define
class SetCustomerAttributesBodyAttributesItem:
    """
    Attributes:
        name (CustomerAttributeReservedName | str): The name of the attribute Example: $email.
        value (None | str): The value of the attribute. Use null to delete the attribute.
    """

    name: CustomerAttributeReservedName | str
    value: None | str

    def to_dict(self) -> dict[str, Any]:
        name: str
        if isinstance(self.name, CustomerAttributeReservedName):
            name = self.name.value
        else:
            name = self.name

        value: None | str
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

        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))

        set_customer_attributes_body_attributes_item = cls(
            name=name,
            value=value,
        )

        return set_customer_attributes_body_attributes_item
