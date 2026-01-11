from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.invoice_object import InvoiceObject

if TYPE_CHECKING:
    from ..models.invoice_line_item import InvoiceLineItem
    from ..models.monetary_amount import MonetaryAmount


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        object_ (InvoiceObject): String representing the object's type. Objects of the same type share the same value.
        id (str): The id of the invoice Example: rcbin1a2b3c4d5e.
        total_amount (MonetaryAmount):
        line_items (list[InvoiceLineItem]): List of line items that are part of the invoice. Each line item represents a
            product that was purchased.
        issued_at (int): The date when the invoiced was issued in ms since epoch Example: 1658399423658.
        paid_at (int | None): The date when the invoiced was paid in ms since epoch Example: 1658399423658.
        invoice_url (None | str): URL to download the invoice pdf Example:
            https://api.revenuecat.com/v2/projects/proj1ab2c3d4/customers/cust1ab2c3d4/invoices/inv1ab2c3d4/file.
    """

    object_: InvoiceObject
    id: str
    total_amount: MonetaryAmount
    line_items: list[InvoiceLineItem]
    issued_at: int
    paid_at: int | None
    invoice_url: None | str

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        total_amount = self.total_amount.to_dict()

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)

        issued_at = self.issued_at

        paid_at: int | None
        paid_at = self.paid_at

        invoice_url: None | str
        invoice_url = self.invoice_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "total_amount": total_amount,
                "line_items": line_items,
                "issued_at": issued_at,
                "paid_at": paid_at,
                "invoice_url": invoice_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_line_item import InvoiceLineItem
        from ..models.monetary_amount import MonetaryAmount

        d = dict(src_dict)
        object_ = InvoiceObject(d.pop("object"))

        id = d.pop("id")

        total_amount = MonetaryAmount.from_dict(d.pop("total_amount"))

        line_items = []
        _line_items = d.pop("line_items")
        for line_items_item_data in _line_items:
            line_items_item = InvoiceLineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        issued_at = d.pop("issued_at")

        def _parse_paid_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        paid_at = _parse_paid_at(d.pop("paid_at"))

        def _parse_invoice_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        invoice_url = _parse_invoice_url(d.pop("invoice_url"))

        invoice = cls(
            object_=object_,
            id=id,
            total_amount=total_amount,
            line_items=line_items,
            issued_at=issued_at,
            paid_at=paid_at,
            invoice_url=invoice_url,
        )

        return invoice
