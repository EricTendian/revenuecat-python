from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_customer_body_attributes_item import CreateCustomerBodyAttributesItem


T = TypeVar("T", bound="CreateCustomerBody")


@_attrs_define
class CreateCustomerBody:
    """
    Attributes:
        id (str): The ID of the customer Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        attributes (list[CreateCustomerBodyAttributesItem] | Unset):
    """

    id: str
    attributes: list[CreateCustomerBodyAttributesItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_customer_body_attributes_item import CreateCustomerBodyAttributesItem

        d = dict(src_dict)
        id = d.pop("id")

        _attributes = d.pop("attributes", UNSET)
        attributes: list[CreateCustomerBodyAttributesItem] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = CreateCustomerBodyAttributesItem.from_dict(attributes_item_data)

                attributes.append(attributes_item)

        create_customer_body = cls(
            id=id,
            attributes=attributes,
        )

        return create_customer_body
