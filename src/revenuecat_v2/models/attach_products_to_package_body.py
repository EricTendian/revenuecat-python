from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.package_product_id_association import PackageProductIDAssociation


T = TypeVar("T", bound="AttachProductsToPackageBody")


@_attrs_define
class AttachProductsToPackageBody:
    """
    Attributes:
        products (list[PackageProductIDAssociation]): Product association list
    """

    products: list[PackageProductIDAssociation]

    def to_dict(self) -> dict[str, Any]:
        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "products": products,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_product_id_association import PackageProductIDAssociation

        d = dict(src_dict)
        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = PackageProductIDAssociation.from_dict(products_item_data)

            products.append(products_item)

        attach_products_to_package_body = cls(
            products=products,
        )

        return attach_products_to_package_body
