from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteSubscriberResponse200")


@_attrs_define
class DeleteSubscriberResponse200:
    """
    Attributes:
        app_user_id (str): The App User ID of the customer that was requested to be deleted Example: XXX-XXXXX-XXXXX-XX.
        deleted (bool): Whether or not the customer was successfully deleted Example: True.
    """

    app_user_id: str
    deleted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_user_id = self.app_user_id

        deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_user_id": app_user_id,
                "deleted": deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_user_id = d.pop("app_user_id")

        deleted = d.pop("deleted")

        delete_subscriber_response_200 = cls(
            app_user_id=app_user_id,
            deleted=deleted,
        )

        delete_subscriber_response_200.additional_properties = d
        return delete_subscriber_response_200

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
