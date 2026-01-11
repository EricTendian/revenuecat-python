from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.customer import Customer


T = TypeVar("T", bound="TransferResult")


@_attrs_define
class TransferResult:
    """
    Attributes:
        source_customer (Customer):
        target_customer (Customer):
    """

    source_customer: Customer
    target_customer: Customer
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_customer = self.source_customer.to_dict()

        target_customer = self.target_customer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_customer": source_customer,
                "target_customer": target_customer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer import Customer

        d = dict(src_dict)
        source_customer = Customer.from_dict(d.pop("source_customer"))

        target_customer = Customer.from_dict(d.pop("target_customer"))

        transfer_result = cls(
            source_customer=source_customer,
            target_customer=target_customer,
        )

        transfer_result.additional_properties = d
        return transfer_result

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
