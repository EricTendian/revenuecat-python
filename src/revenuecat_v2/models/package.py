from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.package_object import PackageObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_product_list import PackageProductList


T = TypeVar("T", bound="Package")


@_attrs_define
class Package:
    """
    Attributes:
        object_ (PackageObject): String representing the object's type. Objects of the same type share the same value.
        id (str): The id of the package Example: pkge1a2b3c4d5.
        lookup_key (str): The lookup_key of the package Example: monthly.
        display_name (str): The display name of the package Example: Monthly discounted with 3-day trial.
        position (int | None): The position of the package within the offering Example: 1.
        created_at (int): The date the package was created at in ms since epoch Example: 1658399423658.
        products (PackageProductList | Unset):
    """

    object_: PackageObject
    id: str
    lookup_key: str
    display_name: str
    position: int | None
    created_at: int
    products: PackageProductList | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        lookup_key = self.lookup_key

        display_name = self.display_name

        position: int | None
        position = self.position

        created_at = self.created_at

        products: dict[str, Any] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = self.products.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "lookup_key": lookup_key,
                "display_name": display_name,
                "position": position,
                "created_at": created_at,
            }
        )
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_product_list import PackageProductList

        d = dict(src_dict)
        object_ = PackageObject(d.pop("object"))

        id = d.pop("id")

        lookup_key = d.pop("lookup_key")

        display_name = d.pop("display_name")

        def _parse_position(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        position = _parse_position(d.pop("position"))

        created_at = d.pop("created_at")

        _products = d.pop("products", UNSET)
        products: PackageProductList | Unset
        if isinstance(_products, Unset):
            products = UNSET
        else:
            products = PackageProductList.from_dict(_products)

        package = cls(
            object_=object_,
            id=id,
            lookup_key=lookup_key,
            display_name=display_name,
            position=position,
            created_at=created_at,
            products=products,
        )

        return package
