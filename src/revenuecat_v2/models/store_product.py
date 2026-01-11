from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.store_product_object import StoreProductObject
from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreProduct")


@_attrs_define
class StoreProduct:
    """
    Attributes:
        object_ (StoreProductObject): String representing the object's type. Objects of the same type share the same
            value.
        id (str): The unique identifier of the product in the store (e.g., App Store Connect product ID) Example:
            1234567890.
        product_identifier (str): The product identifier used in the store Example: com.example.premium_monthly.
        name (None | str | Unset): The name of the store product Example: Premium Monthly Subscription.
    """

    object_: StoreProductObject
    id: str
    product_identifier: str
    name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        product_identifier = self.product_identifier

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "product_identifier": product_identifier,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = StoreProductObject(d.pop("object"))

        id = d.pop("id")

        product_identifier = d.pop("product_identifier")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        store_product = cls(
            object_=object_,
            id=id,
            product_identifier=product_identifier,
            name=name,
        )

        return store_product
