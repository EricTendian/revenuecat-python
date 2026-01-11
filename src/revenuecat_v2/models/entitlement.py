from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.entitlement_object import EntitlementObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entitlement_products_list import EntitlementProductsList


T = TypeVar("T", bound="Entitlement")


@_attrs_define
class Entitlement:
    """
    Attributes:
        object_ (EntitlementObject): String representing the object's type. Objects of the same type share the same
            value.
        project_id (str): ID of the project to which the entitlement belongs Example: proj1ab2c3d4.
        id (str): The id of the entitlement Example: entla1b2c3d4e5.
        lookup_key (str): A custom identifier of the entitlement Example: premium.
        display_name (str): The display name of the entitlement Example: Premium.
        created_at (int): The date when the entitlement was created in ms since epoch Example: 1658399423658.
        products (EntitlementProductsList | None | Unset): List of products attached to the entitlement
    """

    object_: EntitlementObject
    project_id: str
    id: str
    lookup_key: str
    display_name: str
    created_at: int
    products: EntitlementProductsList | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.entitlement_products_list import EntitlementProductsList

        object_ = self.object_.value

        project_id = self.project_id

        id = self.id

        lookup_key = self.lookup_key

        display_name = self.display_name

        created_at = self.created_at

        products: dict[str, Any] | None | Unset
        if isinstance(self.products, Unset):
            products = UNSET
        elif isinstance(self.products, EntitlementProductsList):
            products = self.products.to_dict()
        else:
            products = self.products

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "project_id": project_id,
                "id": id,
                "lookup_key": lookup_key,
                "display_name": display_name,
                "created_at": created_at,
            }
        )
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entitlement_products_list import EntitlementProductsList

        d = dict(src_dict)
        object_ = EntitlementObject(d.pop("object"))

        project_id = d.pop("project_id")

        id = d.pop("id")

        lookup_key = d.pop("lookup_key")

        display_name = d.pop("display_name")

        created_at = d.pop("created_at")

        def _parse_products(data: object) -> EntitlementProductsList | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                products_type_0 = EntitlementProductsList.from_dict(data)

                return products_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EntitlementProductsList | None | Unset, data)

        products = _parse_products(d.pop("products", UNSET))

        entitlement = cls(
            object_=object_,
            project_id=project_id,
            id=id,
            lookup_key=lookup_key,
            display_name=display_name,
            created_at=created_at,
            products=products,
        )

        return entitlement
