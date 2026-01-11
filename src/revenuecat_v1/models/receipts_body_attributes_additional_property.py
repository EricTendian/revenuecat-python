from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReceiptsBodyAttributesAdditionalProperty")


@_attrs_define
class ReceiptsBodyAttributesAdditionalProperty:
    """A single Attribute to be set.

    Attributes:
        value (str): The value of the attribute. If the value is `null` or an empty string, the attribute will be
            deleted.
        updated_at_ms (int | Unset): UNIX epoch in milliseconds of when the attribute was updated. This value is used to
            resolve conflicts, an attribute will only be updated if the new `updated_at_ms` value is newer than the value
            for the stored attribute. Example: 1709195668093.
    """

    value: str
    updated_at_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        updated_at_ms = self.updated_at_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if updated_at_ms is not UNSET:
            field_dict["updated_at_ms"] = updated_at_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        updated_at_ms = d.pop("updated_at_ms", UNSET)

        receipts_body_attributes_additional_property = cls(
            value=value,
            updated_at_ms=updated_at_ms,
        )

        receipts_body_attributes_additional_property.additional_properties = d
        return receipts_body_attributes_additional_property

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
