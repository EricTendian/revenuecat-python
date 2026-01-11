from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AttachProductsToEntitlementBody")


@_attrs_define
class AttachProductsToEntitlementBody:
    """
    Attributes:
        product_ids (list[str]): IDs of the products to be attached to the entitlement.
    """

    product_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        product_ids = self.product_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "product_ids": product_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_ids = cast(list[str], d.pop("product_ids"))

        attach_products_to_entitlement_body = cls(
            product_ids=product_ids,
        )

        return attach_products_to_entitlement_body
