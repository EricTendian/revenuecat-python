from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offerings_offerings_item import OfferingsOfferingsItem


T = TypeVar("T", bound="Offerings")


@_attrs_define
class Offerings:
    """Your app's [Offerings and Packages](/getting-started/entitlements).

    Example:
        {'value': {'current_offering_id': 'default', 'offerings': [{'description': 'The default offering', 'identifier':
            'default', 'packages': [{'identifier': '$rc_monthly', 'platform_product_identifier': 'monthly_free_trial'},
            {'identifier': 'consumable', 'platform_product_identifier': 'consumable1'}, {'identifier': '$rc_annual',
            'platform_product_identifier': 'yearly_free_trial'}]}, {'description': 'The sale offeringg', 'identifier':
            'sale_offering', 'packages': [{'identifier': '$rc_monthly', 'platform_product_identifier':
            'monthly_free_trial_sale'}, {'identifier': 'consumable', 'platform_product_identifier': 'consumable1_sale'},
            {'identifier': '$rc_annual', 'platform_product_identifier': 'yearly_free_trial_sale'}]}]}}

    Attributes:
        current_offering_id (str | Unset): The identifier of the current Offering for this Customer.
            [Targeting](/docs/tools/targeting), [Offering overrides](#tag/offerings/operation/override-offering), and
            [Experiments](/docs/tools/experiments-v1) affect this identifier depending on the App User ID. Example: default.
        offerings (list[OfferingsOfferingsItem] | Unset): A list of available Offerings.
    """

    current_offering_id: str | Unset = UNSET
    offerings: list[OfferingsOfferingsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_offering_id = self.current_offering_id

        offerings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.offerings, Unset):
            offerings = []
            for offerings_item_data in self.offerings:
                offerings_item = offerings_item_data.to_dict()
                offerings.append(offerings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_offering_id is not UNSET:
            field_dict["current_offering_id"] = current_offering_id
        if offerings is not UNSET:
            field_dict["offerings"] = offerings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offerings_offerings_item import OfferingsOfferingsItem

        d = dict(src_dict)
        current_offering_id = d.pop("current_offering_id", UNSET)

        _offerings = d.pop("offerings", UNSET)
        offerings: list[OfferingsOfferingsItem] | Unset = UNSET
        if _offerings is not UNSET:
            offerings = []
            for offerings_item_data in _offerings:
                offerings_item = OfferingsOfferingsItem.from_dict(offerings_item_data)

                offerings.append(offerings_item)

        offerings = cls(
            current_offering_id=current_offering_id,
            offerings=offerings,
        )

        offerings.additional_properties = d
        return offerings

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
