from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_subscriber_attributes_response_400_attribute_errors_item import (
        UpdateSubscriberAttributesResponse400AttributeErrorsItem,
    )


T = TypeVar("T", bound="UpdateSubscriberAttributesResponse400")


@_attrs_define
class UpdateSubscriberAttributesResponse400:
    """
    Attributes:
        code (int | Unset):  Example: 7263.
        message (str | Unset):  Example: Some customer attribute keys were unable to be saved..
        attribute_errors (list[UpdateSubscriberAttributesResponse400AttributeErrorsItem] | Unset):
    """

    code: int | Unset = UNSET
    message: str | Unset = UNSET
    attribute_errors: list[UpdateSubscriberAttributesResponse400AttributeErrorsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        attribute_errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attribute_errors, Unset):
            attribute_errors = []
            for attribute_errors_item_data in self.attribute_errors:
                attribute_errors_item = attribute_errors_item_data.to_dict()
                attribute_errors.append(attribute_errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if attribute_errors is not UNSET:
            field_dict["attribute_errors"] = attribute_errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_subscriber_attributes_response_400_attribute_errors_item import (
            UpdateSubscriberAttributesResponse400AttributeErrorsItem,
        )

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        _attribute_errors = d.pop("attribute_errors", UNSET)
        attribute_errors: list[UpdateSubscriberAttributesResponse400AttributeErrorsItem] | Unset = UNSET
        if _attribute_errors is not UNSET:
            attribute_errors = []
            for attribute_errors_item_data in _attribute_errors:
                attribute_errors_item = UpdateSubscriberAttributesResponse400AttributeErrorsItem.from_dict(
                    attribute_errors_item_data
                )

                attribute_errors.append(attribute_errors_item)

        update_subscriber_attributes_response_400 = cls(
            code=code,
            message=message,
            attribute_errors=attribute_errors,
        )

        update_subscriber_attributes_response_400.additional_properties = d
        return update_subscriber_attributes_response_400

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
