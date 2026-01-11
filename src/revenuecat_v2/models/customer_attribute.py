from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.customer_attribute_object import CustomerAttributeObject

T = TypeVar("T", bound="CustomerAttribute")


@_attrs_define
class CustomerAttribute:
    """
    Attributes:
        object_ (CustomerAttributeObject): String representing the object's type. Objects of the same type share the
            same value.
        name (str): The name of the attribute. Reserved attributes are prefixed with a `$`. Example: $email.
        value (None | str): The value of the attribute. Example: garfield@revenuecat.com.
        updated_at (int): The time when the attribute was last updated. Example: 1658399423658.
    """

    object_: CustomerAttributeObject
    name: str
    value: None | str
    updated_at: int

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        name = self.name

        value: None | str
        value = self.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "name": name,
                "value": value,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = CustomerAttributeObject(d.pop("object"))

        name = d.pop("name")

        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))

        updated_at = d.pop("updated_at")

        customer_attribute = cls(
            object_=object_,
            name=name,
            value=value,
            updated_at=updated_at,
        )

        return customer_attribute
