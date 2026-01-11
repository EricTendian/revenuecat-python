from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferingsOfferingsItemPackagesItem")


@_attrs_define
class OfferingsOfferingsItemPackagesItem:
    """The Offering's packages.

    Attributes:
        identifier (str | Unset): The package's identifier. If you used one of RevenueCat's default identifiers, it will
            be prefixed by `$rc_`. Example: $rc_monthly.
        platform_product_identifier (str | Unset): The identifier of the product in the store. This should be used to
            fetch the product from Apple, Google, Amazon, or Stripe depending on the platform. This field will be populated
            only for the current app based on the API key used and the `X-Platform` header. Example: monthly_free_trial.
    """

    identifier: str | Unset = UNSET
    platform_product_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        platform_product_identifier = self.platform_product_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if platform_product_identifier is not UNSET:
            field_dict["platform_product_identifier"] = platform_product_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        platform_product_identifier = d.pop("platform_product_identifier", UNSET)

        offerings_offerings_item_packages_item = cls(
            identifier=identifier,
            platform_product_identifier=platform_product_identifier,
        )

        offerings_offerings_item_packages_item.additional_properties = d
        return offerings_offerings_item_packages_item

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
