from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offerings_offerings_item_packages_item import OfferingsOfferingsItemPackagesItem


T = TypeVar("T", bound="OfferingsOfferingsItem")


@_attrs_define
class OfferingsOfferingsItem:
    """An Offering.

    Attributes:
        description (str | Unset): The Offering's description. Example: The default offering.
        identifier (str | Unset): The Offering's identifier. Example: default.
        packages (list[OfferingsOfferingsItemPackagesItem] | Unset): The Packages of this Offering.
    """

    description: str | Unset = UNSET
    identifier: str | Unset = UNSET
    packages: list[OfferingsOfferingsItemPackagesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        identifier = self.identifier

        packages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if packages is not UNSET:
            field_dict["packages"] = packages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offerings_offerings_item_packages_item import OfferingsOfferingsItemPackagesItem

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        identifier = d.pop("identifier", UNSET)

        _packages = d.pop("packages", UNSET)
        packages: list[OfferingsOfferingsItemPackagesItem] | Unset = UNSET
        if _packages is not UNSET:
            packages = []
            for packages_item_data in _packages:
                packages_item = OfferingsOfferingsItemPackagesItem.from_dict(packages_item_data)

                packages.append(packages_item)

        offerings_offerings_item = cls(
            description=description,
            identifier=identifier,
            packages=packages,
        )

        offerings_offerings_item.additional_properties = d
        return offerings_offerings_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
