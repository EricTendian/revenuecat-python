from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.products_from_package_list_object import ProductsFromPackageListObject

if TYPE_CHECKING:
    from ..models.package_product_association import PackageProductAssociation


T = TypeVar("T", bound="ProductsFromPackageList")


@_attrs_define
class ProductsFromPackageList:
    """
    Attributes:
        object_ (ProductsFromPackageListObject): String representing the object's type. Objects of the same type share
            the same value. Always has the value `list`.
        items (list[PackageProductAssociation]): Details about each object.
        next_page (None | str): URL to access the next page of the entitlement's products. If not present / null, there
            is no next page Example: /v2/projects/proj1ab2c3d4/packages/pkge1a2b3c4d5/products?starting_after=prod1a2b3c4d5.
        url (str): The URL where this list can be accessed. Example:
            /v2/projects/proj1ab2c3d4/packages/pkge1a2b3c4d5/products.
    """

    object_: ProductsFromPackageListObject
    items: list[PackageProductAssociation]
    next_page: None | str
    url: str

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_page: None | str
        next_page = self.next_page

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "items": items,
                "next_page": next_page,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_product_association import PackageProductAssociation

        d = dict(src_dict)
        object_ = ProductsFromPackageListObject(d.pop("object"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = PackageProductAssociation.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_page(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_page = _parse_next_page(d.pop("next_page"))

        url = d.pop("url")

        products_from_package_list = cls(
            object_=object_,
            items=items,
            next_page=next_page,
            url=url,
        )

        return products_from_package_list
