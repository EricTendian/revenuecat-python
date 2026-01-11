from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rc_billing_app_create_rc_billing_type_0 import RCBillingAppCreateRcBillingType0


T = TypeVar("T", bound="RCBillingAppCreate")


@_attrs_define
class RCBillingAppCreate:
    """
    Attributes:
        rc_billing (None | RCBillingAppCreateRcBillingType0 | Unset): Revenue Cat Billing Store type details
    """

    rc_billing: None | RCBillingAppCreateRcBillingType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rc_billing_app_create_rc_billing_type_0 import RCBillingAppCreateRcBillingType0

        rc_billing: dict[str, Any] | None | Unset
        if isinstance(self.rc_billing, Unset):
            rc_billing = UNSET
        elif isinstance(self.rc_billing, RCBillingAppCreateRcBillingType0):
            rc_billing = self.rc_billing.to_dict()
        else:
            rc_billing = self.rc_billing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rc_billing is not UNSET:
            field_dict["rc_billing"] = rc_billing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rc_billing_app_create_rc_billing_type_0 import RCBillingAppCreateRcBillingType0

        d = dict(src_dict)

        def _parse_rc_billing(data: object) -> None | RCBillingAppCreateRcBillingType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rc_billing_type_0 = RCBillingAppCreateRcBillingType0.from_dict(data)

                return rc_billing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RCBillingAppCreateRcBillingType0 | Unset, data)

        rc_billing = _parse_rc_billing(d.pop("rc_billing", UNSET))

        rc_billing_app_create = cls(
            rc_billing=rc_billing,
        )

        rc_billing_app_create.additional_properties = d
        return rc_billing_app_create

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
