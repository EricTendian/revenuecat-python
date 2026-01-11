from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscribersattributionBodyData")


@_attrs_define
class SubscribersattributionBodyData:
    """The data returned by the attribution network callbacks.

    Attributes:
        rc_idfa (str | Unset): The idfa from AdSupport on iOS. (iOS Only)
        rc_gps_adid (str | Unset): The Google Play Services Advertising identifier. (Android Only)
    """

    rc_idfa: str | Unset = UNSET
    rc_gps_adid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rc_idfa = self.rc_idfa

        rc_gps_adid = self.rc_gps_adid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rc_idfa is not UNSET:
            field_dict["rc_idfa"] = rc_idfa
        if rc_gps_adid is not UNSET:
            field_dict["rc_gps_adid"] = rc_gps_adid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rc_idfa = d.pop("rc_idfa", UNSET)

        rc_gps_adid = d.pop("rc_gps_adid", UNSET)

        subscribersattribution_body_data = cls(
            rc_idfa=rc_idfa,
            rc_gps_adid=rc_gps_adid,
        )

        subscribersattribution_body_data.additional_properties = d
        return subscribersattribution_body_data

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
