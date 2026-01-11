from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AssignCustomerOfferingBody")


@_attrs_define
class AssignCustomerOfferingBody:
    """
    Attributes:
        offering_id (None | str): The ID of the offering to assign to the customer. Set to null to clear any existing
            override. Example: offrng1b2c3d4e5.
    """

    offering_id: None | str

    def to_dict(self) -> dict[str, Any]:
        offering_id: None | str
        offering_id = self.offering_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offering_id": offering_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_offering_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        offering_id = _parse_offering_id(d.pop("offering_id"))

        assign_customer_offering_body = cls(
            offering_id=offering_id,
        )

        return assign_customer_offering_body
