from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.invoice_line_item_object import InvoiceLineItemObject

if TYPE_CHECKING:
    from ..models.monetary_amount import MonetaryAmount


T = TypeVar("T", bound="InvoiceLineItem")


@_attrs_define
class InvoiceLineItem:
    """
    Attributes:
        object_ (InvoiceLineItemObject): String representing the object's type. Objects of the same type share the same
            value.
        product_identifier (str): The product identifier Example: rc_1w_199.
        product_display_name (None | str): The display name of the product Example: Premium Monthly 2023.
        product_duration (None | str): The duration of the subscription in ISO-8601 standard Example: P1M.
        quantity (int): Total purchased items Example: 1.
        unit_amount (MonetaryAmount):
    """

    object_: InvoiceLineItemObject
    product_identifier: str
    product_display_name: None | str
    product_duration: None | str
    quantity: int
    unit_amount: MonetaryAmount

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        product_identifier = self.product_identifier

        product_display_name: None | str
        product_display_name = self.product_display_name

        product_duration: None | str
        product_duration = self.product_duration

        quantity = self.quantity

        unit_amount = self.unit_amount.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "product_identifier": product_identifier,
                "product_display_name": product_display_name,
                "product_duration": product_duration,
                "quantity": quantity,
                "unit_amount": unit_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monetary_amount import MonetaryAmount

        d = dict(src_dict)
        object_ = InvoiceLineItemObject(d.pop("object"))

        product_identifier = d.pop("product_identifier")

        def _parse_product_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        product_display_name = _parse_product_display_name(d.pop("product_display_name"))

        def _parse_product_duration(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        product_duration = _parse_product_duration(d.pop("product_duration"))

        quantity = d.pop("quantity")

        unit_amount = MonetaryAmount.from_dict(d.pop("unit_amount"))

        invoice_line_item = cls(
            object_=object_,
            product_identifier=product_identifier,
            product_display_name=product_display_name,
            product_duration=product_duration,
            quantity=quantity,
            unit_amount=unit_amount,
        )

        return invoice_line_item
